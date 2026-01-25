"""Code generator for Resonite component classes."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .schema_parser import ParsedComponent, ParsedMember, SchemaParser
from .type_mapper import MemberType, TypeMapper


@dataclass
class GeneratedFile:
    """Represents a generated Python file."""

    filename: str
    content: str


class CodeGenerator:
    """Generates Python dataclass code from parsed component schemas."""

    def __init__(self, schema_parser: SchemaParser):
        """Initialize the generator.

        Args:
            schema_parser: Parser instance for resolving schemas.
        """
        self.parser = schema_parser
        self.type_mapper = TypeMapper()

    def generate_from_schema(self, schema_path: Path) -> GeneratedFile:
        """Generate Python code from a schema file.

        Args:
            schema_path: Path to the component schema JSON file.

        Returns:
            GeneratedFile with the output filename and content.
        """
        components = self.parser.parse_schema(schema_path)

        if not components:
            raise ValueError(f"No components found in schema: {schema_path}")

        # Determine output filename from schema
        filename = self._schema_to_filename(schema_path.stem)

        # Generate code
        if len(components) == 1 and not components[0].is_generic:
            # Single non-generic component
            content = self._generate_single_component(components[0], schema_path.name)
        else:
            # Generic component with variants
            content = self._generate_generic_component(components, schema_path.name)

        return GeneratedFile(filename=filename, content=content)

    def generate_from_component(
        self, component: ParsedComponent, schema_filename: str
    ) -> GeneratedFile:
        """Generate Python code from a parsed component.

        This is useful for generating code from components parsed from
        multi-component schema files.

        Args:
            component: The parsed component to generate code for.
            schema_filename: The schema filename to reference in the generated code.

        Returns:
            GeneratedFile with the output filename and content.
        """
        # Determine output filename from component's schema_id
        filename = self._schema_to_filename(component.schema_id.replace(".schema.json", ""))

        # Generate code for the single component
        content = self._generate_single_component(component, schema_filename)

        return GeneratedFile(filename=filename, content=content)

    def generate_from_components(
        self, components: list[ParsedComponent], schema_filename: str
    ) -> GeneratedFile:
        """Generate Python code from a list of parsed components.

        For single non-generic components, generates a single class.
        For multiple components (generic variants), generates a base class
        and variant classes.

        Args:
            components: List of parsed components to generate code for.
            schema_filename: The schema filename to reference in the generated code.

        Returns:
            GeneratedFile with the output filename and content.
        """
        if not components:
            raise ValueError("No components provided")

        # Determine output filename from first component's schema_id
        filename = self._schema_to_filename(
            components[0].schema_id.replace(".schema.json", "")
        )

        # Generate code
        if len(components) == 1 and not components[0].is_generic:
            # Single non-generic component
            content = self._generate_single_component(components[0], schema_filename)
        else:
            # Generic component with variants
            content = self._generate_generic_component(components, schema_filename)

        return GeneratedFile(filename=filename, content=content)

    def _schema_to_filename(self, schema_stem: str) -> str:
        """Convert schema filename stem to Python module path.

        For ProtoFlux components, creates a nested module structure under protoflux/.

        Examples:
            "FrooxEngine.StaticLocaleProvider.schema" -> "static_locale_provider.py"
            "FrooxEngine.BooleanValueDriver_1.schema" -> "boolean_value_driver.py"
            "FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.ClipLengthDouble.schema"
                -> "protoflux/froox_engine/playback/clip_length_double.py"
            "FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Add.schema"
                -> "protoflux/math/add.py"
        """
        # Remove .schema suffix if present
        name = schema_stem.replace(".schema", "")

        # Check for ProtoFlux prefix
        protoflux_prefix = "FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes."
        if name.startswith(protoflux_prefix):
            # Extract the path after the prefix
            remainder = name[len(protoflux_prefix):]
            # Split into parts (e.g., "FrooxEngine.Playback.ClipLengthDouble" -> ["FrooxEngine", "Playback", "ClipLengthDouble"])
            parts = remainder.split(".")
            # Convert each part to snake_case
            snake_parts = [self.type_mapper.to_python_name(p) for p in parts]
            # Remove _1, _2 suffixes from the last part (generic arity markers)
            snake_parts[-1] = re.sub(r"_\d+$", "", snake_parts[-1])
            # Build path: protoflux/submodule/.../filename.py
            return "protoflux/" + "/".join(snake_parts[:-1] + [f"{snake_parts[-1]}.py"]).lstrip("/")

        # Remove FrooxEngine. prefix
        if name.startswith("FrooxEngine."):
            name = name[len("FrooxEngine."):]

        # Remove other ProtoFlux prefix variations (non-standard paths)
        name = re.sub(r"^ProtoFlux\..*?\.Nodes\.", "", name)

        # Remove _1, _2 suffixes (generic arity markers)
        name = re.sub(r"_\d+$", "", name)

        # Convert to snake_case
        name = self.type_mapper.to_python_name(name)

        return f"{name}.py"

    def _generate_single_component(
        self, component: ParsedComponent, schema_filename: str
    ) -> str:
        """Generate code for a single non-generic component."""
        lines: list[str] = []

        # File header
        lines.append(f'"""Generated component: {component.title}.')
        lines.append("")
        lines.append(f"Auto-generated from {schema_filename}")
        lines.append('"""')
        lines.append("")
        lines.append("from __future__ import annotations")
        lines.append("")

        # Imports
        imports = self._collect_imports([component])
        lines.extend(imports)
        lines.append("")
        lines.append("")

        # Class definition
        class_lines = self._generate_class(component, schema_filename)
        lines.extend(class_lines)

        return "\n".join(lines)

    def _generate_generic_component(
        self, components: list[ParsedComponent], schema_filename: str
    ) -> str:
        """Generate code for a generic component with variants."""
        if not components:
            return ""

        lines: list[str] = []
        base_name = components[0].base_name

        # File header
        lines.append(f'"""Generated component: {base_name}.')
        lines.append("")
        lines.append(f"Auto-generated from {schema_filename}")
        lines.append('"""')
        lines.append("")
        lines.append("from __future__ import annotations")
        lines.append("")

        # Imports
        imports = self._collect_imports(components)
        lines.extend(imports)
        lines.append("")
        lines.append("")

        # Generate base class with common members
        base_class_lines = self._generate_base_class(components, schema_filename)
        lines.extend(base_class_lines)
        lines.append("")
        lines.append("")

        # Generate variant classes
        variant_class_names: list[str] = []
        for component in components:
            variant_lines = self._generate_variant_class(
                component, base_name, schema_filename
            )
            lines.extend(variant_lines)
            lines.append("")
            lines.append("")
            variant_class_names.append(self._variant_class_name(base_name, component))

        # Generate type alias for all variants
        lines.append(f"# Type alias for any {base_name} variant")
        if len(variant_class_names) <= 3:
            lines.append(
                f"{base_name} = {' | '.join(variant_class_names)}"
            )
        else:
            lines.append(f"{base_name} = (")
            for name in variant_class_names:
                lines.append(f"    {name}")
                if name != variant_class_names[-1]:
                    lines[-1] += " |"
            lines.append(")")

        return "\n".join(lines)

    def _collect_imports(self, components: list[ParsedComponent]) -> list[str]:
        """Collect all required imports for the components."""
        imports_by_module: dict[str, set[str]] = defaultdict(set)

        # Always need these
        imports_by_module["dataclasses"].add("dataclass")
        imports_by_module["typing"].add("ClassVar")
        imports_by_module["typing"].add("Any")
        imports_by_module["pyresonitelink.components.generated._base"].add(
            "GeneratedComponent"
        )

        # Collect types from members
        for component in components:
            for member in component.members:
                if member.type_mapping:
                    imports_by_module[member.type_mapping.module].add(
                        member.type_mapping.class_name
                    )

        # Format import statements
        lines: list[str] = []

        # Standard library first
        stdlib = ["dataclasses", "typing"]
        for module in stdlib:
            if module in imports_by_module:
                classes = sorted(imports_by_module[module])
                lines.append(f"from {module} import {', '.join(classes)}")
        if any(m in imports_by_module for m in stdlib):
            lines.append("")

        # Third-party and local imports
        for module in sorted(imports_by_module.keys()):
            if module not in stdlib:
                classes = sorted(imports_by_module[module])
                lines.append(f"from {module} import {', '.join(classes)}")

        return lines

    def _generate_class(
        self, component: ParsedComponent, schema_filename: str
    ) -> list[str]:
        """Generate a single component class."""
        lines: list[str] = []

        class_name = self._class_name(component.title)

        lines.append("@dataclass")
        lines.append(f"class {class_name}(GeneratedComponent):")
        lines.append(f'    """{component.title} component.')
        if component.description:
            lines.append("")
            lines.append(f"    {component.description}")
        lines.append('    """')
        lines.append("")

        # Class variables
        lines.append(
            f'    COMPONENT_TYPE: ClassVar[str] = "{component.component_type}"'
        )
        lines.append(f'    SCHEMA_FILE: ClassVar[str] = "{schema_filename}"')
        lines.append("")

        # Member name mapping
        member_map = self._generate_member_map(component.members)
        if member_map:
            lines.append("    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {")
            for python_name, json_name in member_map.items():
                lines.append(f'        "{python_name}": "{json_name}",')
            lines.append("    }")
            lines.append("")

        # Members
        for member in component.members:
            member_line = self._generate_member_field(member)
            if member_line:
                lines.append(f"    {member_line}")

        # Ensure class body is not empty
        if not component.members:
            lines.append("    pass")

        return lines

    def _generate_base_class(
        self, components: list[ParsedComponent], schema_filename: str
    ) -> list[str]:
        """Generate a base class for generic component variants."""
        lines: list[str] = []
        base_name = components[0].base_name

        # Find common members across all variants
        common_members = self._find_common_members(components)

        class_name = f"{self._class_name(base_name)}Base"

        lines.append("@dataclass")
        lines.append(f"class {class_name}(GeneratedComponent):")
        lines.append(f'    """Base class for {base_name}<T> variants."""')
        lines.append("")
        lines.append(f'    SCHEMA_FILE: ClassVar[str] = "{schema_filename}"')
        lines.append("")

        # Member name mapping for common members
        member_map = self._generate_member_map(common_members)
        if member_map:
            lines.append("    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {")
            for python_name, json_name in member_map.items():
                lines.append(f'        "{python_name}": "{json_name}",')
            lines.append("    }")
            lines.append("")

        # Common members
        for member in common_members:
            member_line = self._generate_member_field(member)
            if member_line:
                lines.append(f"    {member_line}")

        if not common_members:
            lines.append("    pass")

        return lines

    def _generate_variant_class(
        self, component: ParsedComponent, base_name: str, schema_filename: str
    ) -> list[str]:
        """Generate a variant class for a generic component."""
        lines: list[str] = []

        class_name = self._variant_class_name(base_name, component)
        base_class_name = f"{self._class_name(base_name)}Base"

        lines.append("@dataclass")
        lines.append(f"class {class_name}({base_class_name}):")
        lines.append(f'    """{component.title} component."""')
        lines.append("")
        lines.append(
            f'    COMPONENT_TYPE: ClassVar[str] = "{component.component_type}"'
        )
        lines.append("")

        # Find variant-specific members (not in common members)
        common_names = {"persistent", "UpdateOrder", "Enabled"}
        variant_members = [m for m in component.members if m.name not in common_names]

        # Member name mapping for variant-specific members
        member_map = self._generate_member_map(variant_members)
        if member_map:
            lines.append("    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {")
            for python_name, json_name in member_map.items():
                lines.append(f'        "{python_name}": "{json_name}",')
            lines.append("    }")
            lines.append("")

        # Variant-specific members
        for member in variant_members:
            member_line = self._generate_member_field(member)
            if member_line:
                lines.append(f"    {member_line}")

        if not variant_members:
            lines.append("    pass")

        return lines

    def _find_common_members(
        self, components: list[ParsedComponent]
    ) -> list[ParsedMember]:
        """Find members common to all component variants."""
        if not components:
            return []

        # Start with first component's members
        common_names = {m.name for m in components[0].members}

        # Intersect with other components
        for component in components[1:]:
            component_names = {m.name for m in component.members}
            common_names &= component_names

        # Return members from first component that are in common set
        # Only include truly common ones (persistent, UpdateOrder, Enabled)
        standard_common = {"persistent", "UpdateOrder", "Enabled"}
        return [
            m for m in components[0].members if m.name in (common_names & standard_common)
        ]

    def _generate_member_field(self, member: ParsedMember) -> str | None:
        """Generate a dataclass field for a member."""
        if not member.type_mapping:
            return None

        type_annotation = member.type_mapping.type_annotation
        field_def = f"{member.python_name}: {type_annotation} = None"

        # Add comment for enums with their allowed values
        if member.member_type == MemberType.ENUM and member.enum_type:
            field_def += f"  # {member.enum_type}"

        # Add comment for references with target type
        if member.member_type == MemberType.REFERENCE and member.target_type:
            # Shorten the target type for readability
            short_type = member.target_type
            if short_type.startswith("[FrooxEngine]"):
                short_type = short_type.replace("[FrooxEngine]", "")
            field_def += f"  # -> {short_type}"

        return field_def

    def _generate_member_map(
        self, members: list[ParsedMember]
    ) -> dict[str, str]:
        """Generate mapping from Python names to JSON names.

        We need to include ALL members in the map because the default
        conversion in _python_to_member_name uses PascalCase, which
        would break fields that are already lowercase (like 'persistent').
        """
        mapping: dict[str, str] = {}
        for member in members:
            # Always add to ensure correct round-tripping
            mapping[member.python_name] = member.name
        return mapping

    def _class_name(self, title: str) -> str:
        """Convert component title to Python class name.

        Examples:
            "StaticLocaleProvider" -> "StaticLocaleProvider"
            "ValueField<bool>" -> "ValueFieldBool"
        """
        # Remove angle brackets and type params for base name
        name = re.sub(r"<[^>]+>", "", title)
        # Ensure PascalCase
        return name

    def _variant_class_name(self, base_name: str, component: ParsedComponent) -> str:
        """Generate class name for a variant.

        Examples:
            "BooleanValueDriver", type_param="bool" -> "BooleanValueDriverBool"
            "ValueField", type_param="float3" -> "ValueFieldFloat3"
            "ValueField", type_param="[System.Private.CoreLib]System.DateTime" -> "ValueFieldDateTime"
        """
        if component.type_parameter:
            type_param = component.type_parameter

            # Handle fully qualified type names like [Assembly]Namespace.TypeName
            # Extract just the type name
            if "]" in type_param:
                # Remove assembly prefix [Assembly]
                type_param = type_param.split("]")[-1]
            if "." in type_param:
                # Take last part after dot
                type_param = type_param.split(".")[-1]

            # Handle common patterns
            type_param = type_param.replace("2x2", "_2x2")
            type_param = type_param.replace("3x3", "_3x3")
            type_param = type_param.replace("4x4", "_4x4")
            # Capitalize first letter
            if type_param and type_param[0].islower():
                type_param = type_param[0].upper() + type_param[1:]
            # Handle numeric suffixes (float2, int3, etc.)
            type_param = re.sub(r"([a-zA-Z])(\d)", r"\1\2", type_param)
            return f"{self._class_name(base_name)}{type_param}"
        return self._class_name(base_name)
