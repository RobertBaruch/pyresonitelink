"""Base class for all generated component classes."""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any, ClassVar, Self

import jsonschema
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

from pyresonitelink.data import codec


def _generate_uuid() -> str:
    """Generate a random UUID v4 string.

    Returns:
        A new random UUID v4 as a string.
    """
    return str(uuid.uuid4())


@dataclass
class GeneratedComponent:
    """Base class for generated component classes.

    Provides common serialization/deserialization methods and
    schema validation support. When constructed directly (not through
    deserialization), the id is automatically set to a random UUID v4.
    """

    # Override in subclasses
    COMPONENT_TYPE: ClassVar[str] = ""
    SCHEMA_FILE: ClassVar[str] = ""

    # Mapping of Python field names to JSON member names
    # Override in subclasses for fields where names differ
    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {}

    # Common fields for all components
    id: str = field(default_factory=_generate_uuid)
    is_reference_only: bool = False

    @classmethod
    def _python_to_member_name(cls, python_name: str) -> str:
        """Convert Python snake_case to JSON member name.

        Uses the _MEMBER_NAME_MAP if defined, otherwise converts
        snake_case to PascalCase.
        """
        if python_name in cls._MEMBER_NAME_MAP:
            return cls._MEMBER_NAME_MAP[python_name]

        # Default: convert snake_case to PascalCase
        parts = python_name.split("_")
        return "".join(p.capitalize() for p in parts)

    @classmethod
    def _member_to_python_name(cls, member_name: str) -> str:
        """Convert JSON member name to Python snake_case.

        Uses inverse of _MEMBER_NAME_MAP if defined.
        """
        # Check inverse mapping
        for python_name, json_name in cls._MEMBER_NAME_MAP.items():
            if json_name == member_name:
                return python_name

        # Default: convert PascalCase/camelCase to snake_case
        import re

        result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", member_name)
        result = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", result)
        return result.lower()

    def to_json(self) -> dict[str, Any]:
        """Serialize component to JSON-compatible dict.

        Returns:
            Dictionary ready for JSON serialization, matching the
            JSON Schema format.
        """
        result: dict[str, Any] = {
            "id": self.id,
            "isReferenceOnly": self.is_reference_only,
            "componentType": self.COMPONENT_TYPE,
            "members": {},
        }

        for field in fields(self):
            # Skip base fields
            if field.name in ("id", "is_reference_only"):
                continue

            value = getattr(self, field.name)
            if value is None:
                continue

            # Get JSON member name
            member_name = self._python_to_member_name(field.name)

            # Encode value using codec
            result["members"][member_name] = codec.encode(value)

        return result

    @classmethod
    def from_json(
        cls,
        data: dict[str, Any],
        validate: bool = True,
        schema: dict[str, Any] | None = None,
        schema_dir: Path | None = None,
    ) -> Self:
        """Deserialize from JSON with optional schema validation.

        Args:
            data: JSON dict representing the component.
            validate: If True, validate against JSON Schema before parsing.
            schema: Optional pre-loaded schema dict. If not provided and
                validate=True, attempts to load from SCHEMA_FILE.
            schema_dir: Directory containing schema files for $ref resolution.
                Required if validate=True and schema has external refs.

        Returns:
            Component instance.

        Raises:
            jsonschema.ValidationError: If data doesn't match schema.
            ValueError: If component type doesn't match.
        """
        # Validate against schema if requested
        if validate:
            if schema is None:
                schema = cls.get_schema()
            if schema:
                cls._validate_with_refs(data, schema, schema_dir)

        # Verify component type
        component_type = data.get("componentType", "")
        if component_type != cls.COMPONENT_TYPE:
            raise ValueError(
                f"Component type mismatch: expected {cls.COMPONENT_TYPE}, "
                f"got {component_type}"
            )

        # Extract base fields
        kwargs: dict[str, Any] = {
            "id": data.get("id", ""),
            "is_reference_only": data.get("isReferenceOnly", False),
        }

        # Extract members
        members = data.get("members", {})
        for field in fields(cls):
            if field.name in kwargs:
                continue

            member_name = cls._python_to_member_name(field.name)
            if member_name in members:
                # Decode value using codec
                raw_value = members[member_name]
                kwargs[field.name] = codec.decode(raw_value)

        return cls(**kwargs)

    @classmethod
    def get_schema(cls) -> dict[str, Any] | None:
        """Load and return the JSON Schema for this component.

        Looks for the schema file in the schemas directory relative to
        the package.

        Returns:
            Schema dict if found, None otherwise.
        """
        if not cls.SCHEMA_FILE:
            return None

        # Try to find schema file
        # First, check if there's a schemas directory in the package
        try:
            import importlib.resources as pkg_resources

            try:
                schema_ref = pkg_resources.files("pyresonitelink") / "schemas" / cls.SCHEMA_FILE
                if schema_ref.is_file():
                    schema_text = schema_ref.read_text(encoding="utf-8")
                    return json.loads(schema_text)
            except (FileNotFoundError, TypeError):
                pass
        except ImportError:
            pass

        # Fallback: try relative path from this file
        schema_dir = Path(__file__).parent.parent.parent / "schemas"
        schema_path = schema_dir / cls.SCHEMA_FILE
        if schema_path.exists():
            with open(schema_path, encoding="utf-8") as f:
                return json.load(f)

        return None

    def __repr__(self) -> str:
        """Return a string representation of the component."""
        class_name = self.__class__.__name__
        return f"{class_name}(id={self.id!r}, component_type={self.COMPONENT_TYPE!r})"

    @classmethod
    def _validate_with_refs(
        cls,
        data: dict[str, Any],
        schema: dict[str, Any],
        schema_dir: Path | None = None,
    ) -> None:
        """Validate data against schema, resolving $ref references.

        Args:
            data: Data to validate.
            schema: Main schema.
            schema_dir: Directory to load referenced schemas from.

        Raises:
            jsonschema.ValidationError: If validation fails.
        """
        # Build registry with referenced schemas
        resources: list[tuple[str, Resource[dict[str, Any]]]] = []

        # Add the main schema
        schema_id = schema.get("$id", "")
        if schema_id:
            resources.append((schema_id, Resource.from_contents(schema)))

        # Load common.schema.json if schema_dir provided
        if schema_dir:
            common_path = schema_dir / "common.schema.json"
            if common_path.exists():
                with open(common_path, encoding="utf-8") as f:
                    common_schema = json.load(f)
                common_id = common_schema.get("$id", "common.schema.json")
                resources.append((common_id, Resource.from_contents(common_schema)))

        # Create registry
        registry = Registry().with_resources(resources)

        # Create validator with registry
        validator_cls = jsonschema.validators.validator_for(schema)
        validator = validator_cls(schema, registry=registry)

        # Validate
        validator.validate(data)
