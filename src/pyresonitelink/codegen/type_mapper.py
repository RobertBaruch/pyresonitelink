"""Type mapping from JSON Schema to Python types."""

import re
from dataclasses import dataclass
from enum import Enum


class MemberType(Enum):
    """Types of component members."""

    VALUE = "value"
    REFERENCE = "reference"
    SYNC_LIST = "syncList"
    LIST = "list"
    ENUM = "enum"
    EMPTY = "empty"


@dataclass
class TypeMapping:
    """Mapping from schema type to Python type."""

    module: str
    class_name: str
    type_annotation: str

    @property
    def import_statement(self) -> str:
        """Get the import statement for this type."""
        return f"from {self.module} import {self.class_name}"


# Maps common.schema.json $defs names to Python Field classes
COMMON_REF_TO_FIELD: dict[str, TypeMapping] = {
    # Boolean
    "bool_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldBool", "FieldBool | None"
    ),
    "nullable_bool_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableBool", "FieldNullableBool | None"
    ),
    # Byte
    "byte_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldByte", "FieldByte | None"
    ),
    "nullable_byte_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableByte", "FieldNullableByte | None"
    ),
    # Unsigned short
    "ushort_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUshort", "FieldUshort | None"
    ),
    "nullable_ushort_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUshort",
        "FieldNullableUshort | None",
    ),
    # Unsigned int
    "uint_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUint", "FieldUint | None"
    ),
    "nullable_uint_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableUint", "FieldNullableUint | None"
    ),
    # Unsigned long
    "ulong_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUlong", "FieldUlong | None"
    ),
    "nullable_ulong_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableUlong", "FieldNullableUlong | None"
    ),
    # Signed byte
    "sbyte_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldSbyte", "FieldSbyte | None"
    ),
    "nullable_sbyte_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableSbyte", "FieldNullableSbyte | None"
    ),
    # Short
    "short_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldShort", "FieldShort | None"
    ),
    "nullable_short_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableShort", "FieldNullableShort | None"
    ),
    # Int
    "int_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldInt", "FieldInt | None"
    ),
    "nullable_int_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableInt", "FieldNullableInt | None"
    ),
    # Long
    "long_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldLong", "FieldLong | None"
    ),
    "nullable_long_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableLong", "FieldNullableLong | None"
    ),
    # Float
    "float_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat", "FieldFloat | None"
    ),
    "nullable_float_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableFloat", "FieldNullableFloat | None"
    ),
    # Double
    "double_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble", "FieldDouble | None"
    ),
    "nullable_double_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble",
        "FieldNullableDouble | None",
    ),
    # Decimal
    "decimal_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDecimal", "FieldDecimal | None"
    ),
    "nullable_decimal_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDecimal",
        "FieldNullableDecimal | None",
    ),
    # Char
    "char_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldChar", "FieldChar | None"
    ),
    "nullable_char_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableChar", "FieldNullableChar | None"
    ),
    # String
    "string_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldString", "FieldString | None"
    ),
    # Uri
    "Uri_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUri", "FieldUri | None"
    ),
    # TimeSpan
    "TimeSpan_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldTimeSpan", "FieldTimeSpan | None"
    ),
    "nullable_TimeSpan_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableTimeSpan",
        "FieldNullableTimeSpan | None",
    ),
    # DateTime
    "DateTime_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDateTime", "FieldDateTime | None"
    ),
    "nullable_DateTime_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDateTime",
        "FieldNullableDateTime | None",
    ),
    # Color
    "color_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldColor", "FieldColor | None"
    ),
    "nullable_color_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableColor", "FieldNullableColor | None"
    ),
    "colorX_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldColorX", "FieldColorX | None"
    ),
    "nullable_colorX_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableColorX",
        "FieldNullableColorX | None",
    ),
    "color32_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldColor32", "FieldColor32 | None"
    ),
    "nullable_color32_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableColor32",
        "FieldNullableColor32 | None",
    ),
    # 2D Vectors
    "float2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat2", "FieldFloat2 | None"
    ),
    "nullable_float2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat2",
        "FieldNullableFloat2 | None",
    ),
    "double2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble2", "FieldDouble2 | None"
    ),
    "nullable_double2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble2",
        "FieldNullableDouble2 | None",
    ),
    "byte2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldByte2", "FieldByte2 | None"
    ),
    "nullable_byte2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableByte2", "FieldNullableByte2 | None"
    ),
    "ushort2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUshort2", "FieldUshort2 | None"
    ),
    "nullable_ushort2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUshort2",
        "FieldNullableUshort2 | None",
    ),
    "uint2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUint2", "FieldUint2 | None"
    ),
    "nullable_uint2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableUint2", "FieldNullableUint2 | None"
    ),
    "ulong2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUlong2", "FieldUlong2 | None"
    ),
    "nullable_ulong2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUlong2",
        "FieldNullableUlong2 | None",
    ),
    "sbyte2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldSbyte2", "FieldSbyte2 | None"
    ),
    "nullable_sbyte2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableSbyte2",
        "FieldNullableSbyte2 | None",
    ),
    "short2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldShort2", "FieldShort2 | None"
    ),
    "nullable_short2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableShort2",
        "FieldNullableShort2 | None",
    ),
    "int2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldInt2", "FieldInt2 | None"
    ),
    "nullable_int2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableInt2", "FieldNullableInt2 | None"
    ),
    "long2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldLong2", "FieldLong2 | None"
    ),
    "nullable_long2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableLong2", "FieldNullableLong2 | None"
    ),
    "bool2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldBool2", "FieldBool2 | None"
    ),
    "nullable_bool2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableBool2", "FieldNullableBool2 | None"
    ),
    # 3D Vectors
    "float3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat3", "FieldFloat3 | None"
    ),
    "nullable_float3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat3",
        "FieldNullableFloat3 | None",
    ),
    "double3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble3", "FieldDouble3 | None"
    ),
    "nullable_double3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble3",
        "FieldNullableDouble3 | None",
    ),
    "byte3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldByte3", "FieldByte3 | None"
    ),
    "nullable_byte3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableByte3", "FieldNullableByte3 | None"
    ),
    "ushort3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUshort3", "FieldUshort3 | None"
    ),
    "nullable_ushort3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUshort3",
        "FieldNullableUshort3 | None",
    ),
    "uint3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUint3", "FieldUint3 | None"
    ),
    "nullable_uint3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableUint3", "FieldNullableUint3 | None"
    ),
    "ulong3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUlong3", "FieldUlong3 | None"
    ),
    "nullable_ulong3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUlong3",
        "FieldNullableUlong3 | None",
    ),
    "sbyte3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldSbyte3", "FieldSbyte3 | None"
    ),
    "nullable_sbyte3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableSbyte3",
        "FieldNullableSbyte3 | None",
    ),
    "short3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldShort3", "FieldShort3 | None"
    ),
    "nullable_short3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableShort3",
        "FieldNullableShort3 | None",
    ),
    "int3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldInt3", "FieldInt3 | None"
    ),
    "nullable_int3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableInt3", "FieldNullableInt3 | None"
    ),
    "long3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldLong3", "FieldLong3 | None"
    ),
    "nullable_long3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableLong3", "FieldNullableLong3 | None"
    ),
    "bool3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldBool3", "FieldBool3 | None"
    ),
    "nullable_bool3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableBool3", "FieldNullableBool3 | None"
    ),
    # 4D Vectors
    "float4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat4", "FieldFloat4 | None"
    ),
    "nullable_float4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat4",
        "FieldNullableFloat4 | None",
    ),
    "double4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble4", "FieldDouble4 | None"
    ),
    "nullable_double4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble4",
        "FieldNullableDouble4 | None",
    ),
    "byte4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldByte4", "FieldByte4 | None"
    ),
    "nullable_byte4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableByte4", "FieldNullableByte4 | None"
    ),
    "ushort4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUshort4", "FieldUshort4 | None"
    ),
    "nullable_ushort4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUshort4",
        "FieldNullableUshort4 | None",
    ),
    "uint4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUint4", "FieldUint4 | None"
    ),
    "nullable_uint4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableUint4", "FieldNullableUint4 | None"
    ),
    "ulong4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldUlong4", "FieldUlong4 | None"
    ),
    "nullable_ulong4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableUlong4",
        "FieldNullableUlong4 | None",
    ),
    "sbyte4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldSbyte4", "FieldSbyte4 | None"
    ),
    "nullable_sbyte4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableSbyte4",
        "FieldNullableSbyte4 | None",
    ),
    "short4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldShort4", "FieldShort4 | None"
    ),
    "nullable_short4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableShort4",
        "FieldNullableShort4 | None",
    ),
    "int4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldInt4", "FieldInt4 | None"
    ),
    "nullable_int4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableInt4", "FieldNullableInt4 | None"
    ),
    "long4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldLong4", "FieldLong4 | None"
    ),
    "nullable_long4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableLong4", "FieldNullableLong4 | None"
    ),
    "bool4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldBool4", "FieldBool4 | None"
    ),
    "nullable_bool4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldNullableBool4", "FieldNullableBool4 | None"
    ),
    # Quaternions
    "floatQ_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloatQ", "FieldFloatQ | None"
    ),
    "nullable_floatQ_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloatQ",
        "FieldNullableFloatQ | None",
    ),
    "doubleQ_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDoubleQ", "FieldDoubleQ | None"
    ),
    "nullable_doubleQ_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDoubleQ",
        "FieldNullableDoubleQ | None",
    ),
    # Matrices
    "float2x2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat2x2", "FieldFloat2x2 | None"
    ),
    "nullable_float2x2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat2x2",
        "FieldNullableFloat2x2 | None",
    ),
    "double2x2_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble2x2", "FieldDouble2x2 | None"
    ),
    "nullable_double2x2_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble2x2",
        "FieldNullableDouble2x2 | None",
    ),
    "float3x3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat3x3", "FieldFloat3x3 | None"
    ),
    "nullable_float3x3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat3x3",
        "FieldNullableFloat3x3 | None",
    ),
    "double3x3_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble3x3", "FieldDouble3x3 | None"
    ),
    "nullable_double3x3_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble3x3",
        "FieldNullableDouble3x3 | None",
    ),
    "float4x4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldFloat4x4", "FieldFloat4x4 | None"
    ),
    "nullable_float4x4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableFloat4x4",
        "FieldNullableFloat4x4 | None",
    ),
    "double4x4_value": TypeMapping(
        "pyresonitelink.data.fields", "FieldDouble4x4", "FieldDouble4x4 | None"
    ),
    "nullable_double4x4_value": TypeMapping(
        "pyresonitelink.data.fields",
        "FieldNullableDouble4x4",
        "FieldNullableDouble4x4 | None",
    ),
}

# Maps inline $type values to member classes
TYPE_TO_MEMBER: dict[str, TypeMapping] = {
    "reference": TypeMapping(
        "pyresonitelink.data.members", "Reference", "Reference | None"
    ),
    "syncList": TypeMapping(
        "pyresonitelink.data.members", "SyncList", "SyncList | None"
    ),
    "list": TypeMapping("pyresonitelink.data.members", "SyncList", "SyncList | None"),
    "empty": TypeMapping(
        "pyresonitelink.data.members", "EmptyElement", "EmptyElement | None"
    ),
    "enum": TypeMapping(
        "pyresonitelink.data.members", "FieldEnum", "FieldEnum | None"
    ),
}


class TypeMapper:
    """Maps schema types to Python types."""

    # Python keywords that need to be escaped
    PYTHON_KEYWORDS = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    def to_python_name(self, member_name: str) -> str:
        """Convert a JSON member name to Python snake_case.

        Examples:
            "UpdateOrder" -> "update_order"
            "URL" -> "url"
            "persistent" -> "persistent"
            "class" -> "class_"
        """
        # Handle already lowercase names
        if member_name.islower():
            result = member_name
        else:
            # Convert PascalCase/camelCase to snake_case
            # Insert underscore before uppercase letters
            result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", member_name)
            # Handle consecutive uppercase (e.g., "URL" -> "url", "URLPath" -> "url_path")
            result = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", result)
            result = result.lower()

        # Escape Python keywords
        if result in self.PYTHON_KEYWORDS:
            result = f"{result}_"

        return result

    def get_common_ref_mapping(self, ref_name: str) -> TypeMapping | None:
        """Get the type mapping for a common.schema.json $ref.

        Args:
            ref_name: The definition name (e.g., "bool_value", "float3_value")

        Returns:
            TypeMapping if found, None otherwise.
        """
        return COMMON_REF_TO_FIELD.get(ref_name)

    def get_inline_type_mapping(self, type_name: str) -> TypeMapping | None:
        """Get the type mapping for an inline $type.

        Args:
            type_name: The $type value (e.g., "reference", "syncList", "empty")

        Returns:
            TypeMapping if found, None otherwise.
        """
        return TYPE_TO_MEMBER.get(type_name)

    def parse_common_ref(self, ref: str) -> str | None:
        """Parse a common.schema.json $ref and return the definition name.

        Args:
            ref: The $ref string (e.g., "common.schema.json#/$defs/bool_value")

        Returns:
            The definition name (e.g., "bool_value") or None if not a common ref.
        """
        if ref.startswith("common.schema.json#/$defs/"):
            return ref.split("/")[-1]
        return None

    def parse_local_ref(self, ref: str) -> str | None:
        """Parse a local $ref and return the definition name.

        Args:
            ref: The $ref string (e.g., "#/$defs/EnumName_value")

        Returns:
            The definition name (e.g., "EnumName_value") or None if not a local ref.
        """
        if ref.startswith("#/$defs/"):
            return ref.split("/")[-1]
        return None
