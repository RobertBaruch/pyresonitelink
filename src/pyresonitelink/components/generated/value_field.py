"""Generated component: ValueField.

Auto-generated from FrooxEngine.ValueField_1.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldBool2, FieldBool3, FieldBool4, FieldByte, FieldByte2, FieldByte3, FieldByte4, FieldChar, FieldColor, FieldColorX, FieldDateTime, FieldDecimal, FieldDouble, FieldDouble2, FieldDouble2x2, FieldDouble3, FieldDouble3x3, FieldDouble4, FieldDouble4x4, FieldDoubleQ, FieldFloat, FieldFloat2, FieldFloat2x2, FieldFloat3, FieldFloat3x3, FieldFloat4, FieldFloat4x4, FieldFloatQ, FieldInt, FieldInt2, FieldInt3, FieldInt4, FieldLong, FieldLong2, FieldLong3, FieldLong4, FieldSbyte, FieldSbyte2, FieldSbyte3, FieldSbyte4, FieldShort, FieldShort2, FieldShort3, FieldShort4, FieldString, FieldTimeSpan, FieldUint, FieldUint2, FieldUint3, FieldUint4, FieldUlong, FieldUlong2, FieldUlong3, FieldUlong4, FieldUri, FieldUshort, FieldUshort2, FieldUshort3, FieldUshort4


@dataclass
class ValueFieldBase(GeneratedComponent):
    """Base class for ValueField<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.ValueField_1.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class ValueFieldBool(ValueFieldBase):
    """ValueField<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool | None = None


@dataclass
class ValueFieldByte(ValueFieldBase):
    """ValueField<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte | None = None


@dataclass
class ValueFieldUshort(ValueFieldBase):
    """ValueField<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort | None = None


@dataclass
class ValueFieldUint(ValueFieldBase):
    """ValueField<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint | None = None


@dataclass
class ValueFieldUlong(ValueFieldBase):
    """ValueField<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong | None = None


@dataclass
class ValueFieldSbyte(ValueFieldBase):
    """ValueField<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte | None = None


@dataclass
class ValueFieldShort(ValueFieldBase):
    """ValueField<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort | None = None


@dataclass
class ValueFieldInt(ValueFieldBase):
    """ValueField<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt | None = None


@dataclass
class ValueFieldLong(ValueFieldBase):
    """ValueField<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong | None = None


@dataclass
class ValueFieldFloat(ValueFieldBase):
    """ValueField<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat | None = None


@dataclass
class ValueFieldDouble(ValueFieldBase):
    """ValueField<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble | None = None


@dataclass
class ValueFieldDecimal(ValueFieldBase):
    """ValueField<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDecimal | None = None


@dataclass
class ValueFieldChar(ValueFieldBase):
    """ValueField<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldChar | None = None


@dataclass
class ValueFieldString(ValueFieldBase):
    """ValueField<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldString | None = None


@dataclass
class ValueFieldUri(ValueFieldBase):
    """ValueField<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUri | None = None


@dataclass
class ValueFieldBool2(ValueFieldBase):
    """ValueField<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool2 | None = None


@dataclass
class ValueFieldByte2(ValueFieldBase):
    """ValueField<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte2 | None = None


@dataclass
class ValueFieldUshort2(ValueFieldBase):
    """ValueField<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort2 | None = None


@dataclass
class ValueFieldUint2(ValueFieldBase):
    """ValueField<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint2 | None = None


@dataclass
class ValueFieldUlong2(ValueFieldBase):
    """ValueField<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong2 | None = None


@dataclass
class ValueFieldSbyte2(ValueFieldBase):
    """ValueField<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte2 | None = None


@dataclass
class ValueFieldShort2(ValueFieldBase):
    """ValueField<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort2 | None = None


@dataclass
class ValueFieldInt2(ValueFieldBase):
    """ValueField<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt2 | None = None


@dataclass
class ValueFieldLong2(ValueFieldBase):
    """ValueField<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong2 | None = None


@dataclass
class ValueFieldFloat2(ValueFieldBase):
    """ValueField<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2 | None = None


@dataclass
class ValueFieldDouble2(ValueFieldBase):
    """ValueField<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2 | None = None


@dataclass
class ValueFieldBool3(ValueFieldBase):
    """ValueField<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool3 | None = None


@dataclass
class ValueFieldByte3(ValueFieldBase):
    """ValueField<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte3 | None = None


@dataclass
class ValueFieldUshort3(ValueFieldBase):
    """ValueField<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort3 | None = None


@dataclass
class ValueFieldUint3(ValueFieldBase):
    """ValueField<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint3 | None = None


@dataclass
class ValueFieldUlong3(ValueFieldBase):
    """ValueField<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong3 | None = None


@dataclass
class ValueFieldSbyte3(ValueFieldBase):
    """ValueField<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte3 | None = None


@dataclass
class ValueFieldShort3(ValueFieldBase):
    """ValueField<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort3 | None = None


@dataclass
class ValueFieldInt3(ValueFieldBase):
    """ValueField<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt3 | None = None


@dataclass
class ValueFieldLong3(ValueFieldBase):
    """ValueField<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong3 | None = None


@dataclass
class ValueFieldFloat3(ValueFieldBase):
    """ValueField<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3 | None = None


@dataclass
class ValueFieldDouble3(ValueFieldBase):
    """ValueField<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3 | None = None


@dataclass
class ValueFieldBool4(ValueFieldBase):
    """ValueField<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool4 | None = None


@dataclass
class ValueFieldByte4(ValueFieldBase):
    """ValueField<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte4 | None = None


@dataclass
class ValueFieldUshort4(ValueFieldBase):
    """ValueField<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort4 | None = None


@dataclass
class ValueFieldUint4(ValueFieldBase):
    """ValueField<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint4 | None = None


@dataclass
class ValueFieldUlong4(ValueFieldBase):
    """ValueField<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong4 | None = None


@dataclass
class ValueFieldSbyte4(ValueFieldBase):
    """ValueField<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte4 | None = None


@dataclass
class ValueFieldShort4(ValueFieldBase):
    """ValueField<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort4 | None = None


@dataclass
class ValueFieldInt4(ValueFieldBase):
    """ValueField<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt4 | None = None


@dataclass
class ValueFieldLong4(ValueFieldBase):
    """ValueField<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong4 | None = None


@dataclass
class ValueFieldFloat4(ValueFieldBase):
    """ValueField<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4 | None = None


@dataclass
class ValueFieldDouble4(ValueFieldBase):
    """ValueField<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4 | None = None


@dataclass
class ValueFieldFloat_2x2(ValueFieldBase):
    """ValueField<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2x2 | None = None


@dataclass
class ValueFieldDouble_2x2(ValueFieldBase):
    """ValueField<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2x2 | None = None


@dataclass
class ValueFieldFloat_3x3(ValueFieldBase):
    """ValueField<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3x3 | None = None


@dataclass
class ValueFieldDouble_3x3(ValueFieldBase):
    """ValueField<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3x3 | None = None


@dataclass
class ValueFieldFloat_4x4(ValueFieldBase):
    """ValueField<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4x4 | None = None


@dataclass
class ValueFieldDouble_4x4(ValueFieldBase):
    """ValueField<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4x4 | None = None


@dataclass
class ValueFieldFloatQ(ValueFieldBase):
    """ValueField<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloatQ | None = None


@dataclass
class ValueFieldDoubleQ(ValueFieldBase):
    """ValueField<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDoubleQ | None = None


@dataclass
class ValueFieldDateTime(ValueFieldBase):
    """ValueField<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDateTime | None = None


@dataclass
class ValueFieldTimeSpan(ValueFieldBase):
    """ValueField<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldTimeSpan | None = None


@dataclass
class ValueFieldColor(ValueFieldBase):
    """ValueField<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColor | None = None


@dataclass
class ValueFieldColorX(ValueFieldBase):
    """ValueField<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColorX | None = None


# Type alias for any ValueField variant
ValueField = (
    ValueFieldBool |
    ValueFieldByte |
    ValueFieldUshort |
    ValueFieldUint |
    ValueFieldUlong |
    ValueFieldSbyte |
    ValueFieldShort |
    ValueFieldInt |
    ValueFieldLong |
    ValueFieldFloat |
    ValueFieldDouble |
    ValueFieldDecimal |
    ValueFieldChar |
    ValueFieldString |
    ValueFieldUri |
    ValueFieldBool2 |
    ValueFieldByte2 |
    ValueFieldUshort2 |
    ValueFieldUint2 |
    ValueFieldUlong2 |
    ValueFieldSbyte2 |
    ValueFieldShort2 |
    ValueFieldInt2 |
    ValueFieldLong2 |
    ValueFieldFloat2 |
    ValueFieldDouble2 |
    ValueFieldBool3 |
    ValueFieldByte3 |
    ValueFieldUshort3 |
    ValueFieldUint3 |
    ValueFieldUlong3 |
    ValueFieldSbyte3 |
    ValueFieldShort3 |
    ValueFieldInt3 |
    ValueFieldLong3 |
    ValueFieldFloat3 |
    ValueFieldDouble3 |
    ValueFieldBool4 |
    ValueFieldByte4 |
    ValueFieldUshort4 |
    ValueFieldUint4 |
    ValueFieldUlong4 |
    ValueFieldSbyte4 |
    ValueFieldShort4 |
    ValueFieldInt4 |
    ValueFieldLong4 |
    ValueFieldFloat4 |
    ValueFieldDouble4 |
    ValueFieldFloat_2x2 |
    ValueFieldDouble_2x2 |
    ValueFieldFloat_3x3 |
    ValueFieldDouble_3x3 |
    ValueFieldFloat_4x4 |
    ValueFieldDouble_4x4 |
    ValueFieldFloatQ |
    ValueFieldDoubleQ |
    ValueFieldDateTime |
    ValueFieldTimeSpan |
    ValueFieldColor |
    ValueFieldColorX
)