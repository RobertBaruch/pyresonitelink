"""JSON Schema parsing for Resonite component schemas."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .type_mapper import MemberType, TypeMapper, TypeMapping


@dataclass
class ParsedMember:
    """Represents a parsed component member."""

    name: str  # Original JSON name (e.g., "UpdateOrder")
    python_name: str  # Python snake_case name (e.g., "update_order")
    member_type: MemberType  # VALUE, REFERENCE, SYNC_LIST, ENUM, EMPTY
    type_mapping: TypeMapping | None  # Mapping to Python type
    target_type: str | None = None  # For references: full Resonite type path
    element_schema: dict[str, Any] | None = None  # For lists: element schema
    enum_values: list[str] | None = None  # For enums: allowed values
    enum_type: str | None = None  # For enums: enum type name
    description: str | None = None  # Optional description


@dataclass
class ParsedComponent:
    """Represents a parsed component schema."""

    schema_id: str  # e.g., "FrooxEngine.StaticLocaleProvider.schema.json"
    title: str  # e.g., "StaticLocaleProvider"
    description: str | None
    component_type: str  # e.g., "[FrooxEngine]FrooxEngine.StaticLocaleProvider"
    is_generic: bool  # True if this is a variant of a generic component
    type_parameter: str | None  # For generics: "bool", "float3", etc.
    base_name: str  # e.g., "StaticLocaleProvider" or "BooleanValueDriver"
    members: list[ParsedMember] = field(default_factory=list)
    local_enums: dict[str, list[str]] = field(
        default_factory=dict
    )  # Enum name -> values


class SchemaParser:
    """Parses JSON Schema files for Resonite components."""

    def __init__(self, common_schema_path: Path | None = None):
        """Initialize the parser.

        Args:
            common_schema_path: Path to common.schema.json. If None, $refs to
                common.schema.json will use type mapper defaults.
        """
        self.type_mapper = TypeMapper()
        self.common_defs: dict[str, Any] = {}

        if common_schema_path and common_schema_path.exists():
            with open(common_schema_path, encoding="utf-8") as f:
                common_schema = json.load(f)
                self.common_defs = common_schema.get("$defs", {})

    def parse_schema(self, schema_path: Path) -> list[ParsedComponent]:
        """Parse a schema file.

        Returns one component for non-generic schemas, multiple for generic
        schemas with oneOf.

        Args:
            schema_path: Path to the component schema JSON file.

        Returns:
            List of ParsedComponent objects.
        """
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)

        schema_id = schema.get("$id", schema_path.name)

        # Check if this is a generic component with oneOf
        if "oneOf" in schema:
            return self._parse_generic_schema(schema, schema_id)
        else:
            return [self._parse_single_component(schema, schema_id)]

    def _parse_generic_schema(
        self, schema: dict[str, Any], schema_id: str
    ) -> list[ParsedComponent]:
        """Parse a generic component schema with oneOf variants."""
        components: list[ParsedComponent] = []
        local_defs = schema.get("$defs", {})
        base_title = schema.get("title", "Unknown")

        for one_of_item in schema.get("oneOf", []):
            ref = one_of_item.get("$ref", "")
            def_name = self.type_mapper.parse_local_ref(ref)
            if def_name and def_name in local_defs:
                variant_schema = local_defs[def_name]
                component = self._parse_variant(
                    variant_schema, schema_id, base_title, local_defs
                )
                if component:
                    components.append(component)

        return components

    def _parse_variant(
        self,
        variant_schema: dict[str, Any],
        schema_id: str,
        base_title: str,
        local_defs: dict[str, Any],
    ) -> ParsedComponent | None:
        """Parse a single variant from a generic schema."""
        properties = variant_schema.get("properties", {})

        # Get component type
        component_type_prop = properties.get("componentType", {})
        component_type = component_type_prop.get("const", "")
        if not component_type:
            return None

        # Extract type parameter from component type
        # e.g., "[FrooxEngine]FrooxEngine.BooleanValueDriver<float2>" -> "float2"
        type_param = self._extract_type_parameter(component_type)

        # Get title from variant or construct from base + type param
        title = variant_schema.get("title", f"{base_title}<{type_param}>")

        # Parse members
        members_schema = properties.get("members", {})
        members = self._parse_members(
            members_schema.get("properties", {}), local_defs
        )

        # Extract local enums
        local_enums = self._extract_local_enums(local_defs)

        return ParsedComponent(
            schema_id=schema_id,
            title=title,
            description=variant_schema.get("description"),
            component_type=component_type,
            is_generic=True,
            type_parameter=type_param,
            base_name=base_title,
            members=members,
            local_enums=local_enums,
        )

    def _parse_single_component(
        self, schema: dict[str, Any], schema_id: str
    ) -> ParsedComponent:
        """Parse a non-generic component schema."""
        properties = schema.get("properties", {})
        local_defs = schema.get("$defs", {})

        # Get component type
        component_type_prop = properties.get("componentType", {})
        component_type = component_type_prop.get("const", "")

        title = schema.get("title", "Unknown")

        # Parse members
        members_schema = properties.get("members", {})
        members = self._parse_members(
            members_schema.get("properties", {}), local_defs
        )

        # Extract local enums
        local_enums = self._extract_local_enums(local_defs)

        return ParsedComponent(
            schema_id=schema_id,
            title=title,
            description=schema.get("description"),
            component_type=component_type,
            is_generic=False,
            type_parameter=None,
            base_name=title,
            members=members,
            local_enums=local_enums,
        )

    def _parse_members(
        self, members_props: dict[str, Any], local_defs: dict[str, Any]
    ) -> list[ParsedMember]:
        """Parse component member definitions."""
        members: list[ParsedMember] = []

        for name, member_schema in members_props.items():
            member = self._parse_member(name, member_schema, local_defs)
            if member:
                members.append(member)

        return members

    def _parse_member(
        self, name: str, schema: dict[str, Any], local_defs: dict[str, Any]
    ) -> ParsedMember | None:
        """Parse a single member definition."""
        python_name = self.type_mapper.to_python_name(name)
        description = schema.get("description")

        # Check for $ref
        if "$ref" in schema:
            ref = schema["$ref"]

            # Check if it's a common.schema.json reference
            common_def = self.type_mapper.parse_common_ref(ref)
            if common_def:
                type_mapping = self.type_mapper.get_common_ref_mapping(common_def)
                if type_mapping:
                    return ParsedMember(
                        name=name,
                        python_name=python_name,
                        member_type=MemberType.VALUE,
                        type_mapping=type_mapping,
                        description=description,
                    )

            # Check if it's a local $ref (usually enum)
            local_def = self.type_mapper.parse_local_ref(ref)
            if local_def and local_def in local_defs:
                return self._parse_local_def_member(
                    name, python_name, local_defs[local_def], description
                )

        # Check for inline type definition
        properties = schema.get("properties", {})
        type_prop = properties.get("$type", {})
        type_const = type_prop.get("const", "")

        if type_const == "reference":
            target_type = properties.get("targetType", {}).get("const")
            type_mapping = self.type_mapper.get_inline_type_mapping("reference")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.REFERENCE,
                type_mapping=type_mapping,
                target_type=target_type,
                description=description,
            )

        if type_const == "syncList":
            elements_schema = schema.get("properties", {}).get("elements", {})
            type_mapping = self.type_mapper.get_inline_type_mapping("syncList")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.SYNC_LIST,
                type_mapping=type_mapping,
                element_schema=elements_schema,
                description=description,
            )

        if type_const == "list":
            elements_schema = schema.get("properties", {}).get("elements", {})
            type_mapping = self.type_mapper.get_inline_type_mapping("list")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.LIST,
                type_mapping=type_mapping,
                element_schema=elements_schema,
                description=description,
            )

        if type_const == "empty":
            type_mapping = self.type_mapper.get_inline_type_mapping("empty")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.EMPTY,
                type_mapping=type_mapping,
                description=description,
            )

        if type_const == "enum":
            value_prop = properties.get("value", {})
            enum_values = value_prop.get("enum", [])
            enum_type_prop = properties.get("enumType", {})
            enum_type = enum_type_prop.get("const")
            type_mapping = self.type_mapper.get_inline_type_mapping("enum")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.ENUM,
                type_mapping=type_mapping,
                enum_values=enum_values,
                enum_type=enum_type,
                description=description,
            )

        # Unknown type - return None or create a generic member
        return None

    def _parse_local_def_member(
        self, name: str, python_name: str, def_schema: dict[str, Any], description: str | None
    ) -> ParsedMember | None:
        """Parse a member that references a local $def (usually an enum)."""
        properties = def_schema.get("properties", {})
        type_prop = properties.get("$type", {})
        type_const = type_prop.get("const", "")

        if type_const == "enum":
            value_prop = properties.get("value", {})
            enum_values = value_prop.get("enum", [])
            enum_type_prop = properties.get("enumType", {})
            enum_type = enum_type_prop.get("const")
            type_mapping = self.type_mapper.get_inline_type_mapping("enum")
            return ParsedMember(
                name=name,
                python_name=python_name,
                member_type=MemberType.ENUM,
                type_mapping=type_mapping,
                enum_values=enum_values,
                enum_type=enum_type,
                description=description,
            )

        return None

    def _extract_local_enums(
        self, local_defs: dict[str, Any]
    ) -> dict[str, list[str]]:
        """Extract enum definitions from local $defs."""
        enums: dict[str, list[str]] = {}

        for def_name, def_schema in local_defs.items():
            properties = def_schema.get("properties", {})
            type_prop = properties.get("$type", {})
            if type_prop.get("const") == "enum":
                value_prop = properties.get("value", {})
                enum_values = value_prop.get("enum", [])
                enum_type_prop = properties.get("enumType", {})
                enum_type = enum_type_prop.get("const", def_name)
                if enum_values:
                    enums[enum_type] = enum_values

        return enums

    def _extract_type_parameter(self, component_type: str) -> str | None:
        """Extract type parameter from component type string.

        Examples:
            "[FrooxEngine]FrooxEngine.ValueField<bool>" -> "bool"
            "[FrooxEngine]FrooxEngine.BooleanValueDriver<float2>" -> "float2"
        """
        match = re.search(r"<([^>]+)>", component_type)
        return match.group(1) if match else None
