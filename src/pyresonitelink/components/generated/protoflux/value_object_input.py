"""Generated component: ValueObjectInput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldBool2, FieldBool3, FieldBool4, FieldByte, FieldByte2, FieldByte3, FieldByte4, FieldChar, FieldColor, FieldColorX, FieldDateTime, FieldDecimal, FieldDouble, FieldDouble2, FieldDouble2x2, FieldDouble3, FieldDouble3x3, FieldDouble4, FieldDouble4x4, FieldDoubleQ, FieldFloat, FieldFloat2, FieldFloat2x2, FieldFloat3, FieldFloat3x3, FieldFloat4, FieldFloat4x4, FieldFloatQ, FieldInt, FieldInt2, FieldInt3, FieldInt4, FieldLong, FieldLong2, FieldLong3, FieldLong4, FieldSbyte, FieldSbyte2, FieldSbyte3, FieldSbyte4, FieldShort, FieldShort2, FieldShort3, FieldShort4, FieldString, FieldTimeSpan, FieldUint, FieldUint2, FieldUint3, FieldUint4, FieldUlong, FieldUlong2, FieldUlong3, FieldUlong4, FieldUri, FieldUshort, FieldUshort2, FieldUshort3, FieldUshort4


@dataclass
class ValueObjectInputBase(GeneratedComponent):
    """Base class for ValueObjectInput<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class ValueObjectInputBool(ValueObjectInputBase):
    """ValueObjectInput<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool | None = None


@dataclass
class ValueObjectInputByte(ValueObjectInputBase):
    """ValueObjectInput<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte | None = None


@dataclass
class ValueObjectInputUshort(ValueObjectInputBase):
    """ValueObjectInput<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort | None = None


@dataclass
class ValueObjectInputUint(ValueObjectInputBase):
    """ValueObjectInput<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint | None = None


@dataclass
class ValueObjectInputUlong(ValueObjectInputBase):
    """ValueObjectInput<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong | None = None


@dataclass
class ValueObjectInputSbyte(ValueObjectInputBase):
    """ValueObjectInput<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte | None = None


@dataclass
class ValueObjectInputShort(ValueObjectInputBase):
    """ValueObjectInput<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort | None = None


@dataclass
class ValueObjectInputInt(ValueObjectInputBase):
    """ValueObjectInput<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt | None = None


@dataclass
class ValueObjectInputLong(ValueObjectInputBase):
    """ValueObjectInput<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong | None = None


@dataclass
class ValueObjectInputFloat(ValueObjectInputBase):
    """ValueObjectInput<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat | None = None


@dataclass
class ValueObjectInputDouble(ValueObjectInputBase):
    """ValueObjectInput<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble | None = None


@dataclass
class ValueObjectInputDecimal(ValueObjectInputBase):
    """ValueObjectInput<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDecimal | None = None


@dataclass
class ValueObjectInputChar(ValueObjectInputBase):
    """ValueObjectInput<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldChar | None = None


@dataclass
class ValueObjectInputString(ValueObjectInputBase):
    """ValueObjectInput<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldString | None = None


@dataclass
class ValueObjectInputUri(ValueObjectInputBase):
    """ValueObjectInput<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUri | None = None


@dataclass
class ValueObjectInputBool2(ValueObjectInputBase):
    """ValueObjectInput<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool2 | None = None


@dataclass
class ValueObjectInputByte2(ValueObjectInputBase):
    """ValueObjectInput<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte2 | None = None


@dataclass
class ValueObjectInputUshort2(ValueObjectInputBase):
    """ValueObjectInput<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort2 | None = None


@dataclass
class ValueObjectInputUint2(ValueObjectInputBase):
    """ValueObjectInput<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint2 | None = None


@dataclass
class ValueObjectInputUlong2(ValueObjectInputBase):
    """ValueObjectInput<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong2 | None = None


@dataclass
class ValueObjectInputSbyte2(ValueObjectInputBase):
    """ValueObjectInput<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte2 | None = None


@dataclass
class ValueObjectInputShort2(ValueObjectInputBase):
    """ValueObjectInput<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort2 | None = None


@dataclass
class ValueObjectInputInt2(ValueObjectInputBase):
    """ValueObjectInput<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt2 | None = None


@dataclass
class ValueObjectInputLong2(ValueObjectInputBase):
    """ValueObjectInput<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong2 | None = None


@dataclass
class ValueObjectInputFloat2(ValueObjectInputBase):
    """ValueObjectInput<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2 | None = None


@dataclass
class ValueObjectInputDouble2(ValueObjectInputBase):
    """ValueObjectInput<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2 | None = None


@dataclass
class ValueObjectInputBool3(ValueObjectInputBase):
    """ValueObjectInput<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool3 | None = None


@dataclass
class ValueObjectInputByte3(ValueObjectInputBase):
    """ValueObjectInput<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte3 | None = None


@dataclass
class ValueObjectInputUshort3(ValueObjectInputBase):
    """ValueObjectInput<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort3 | None = None


@dataclass
class ValueObjectInputUint3(ValueObjectInputBase):
    """ValueObjectInput<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint3 | None = None


@dataclass
class ValueObjectInputUlong3(ValueObjectInputBase):
    """ValueObjectInput<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong3 | None = None


@dataclass
class ValueObjectInputSbyte3(ValueObjectInputBase):
    """ValueObjectInput<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte3 | None = None


@dataclass
class ValueObjectInputShort3(ValueObjectInputBase):
    """ValueObjectInput<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort3 | None = None


@dataclass
class ValueObjectInputInt3(ValueObjectInputBase):
    """ValueObjectInput<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt3 | None = None


@dataclass
class ValueObjectInputLong3(ValueObjectInputBase):
    """ValueObjectInput<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong3 | None = None


@dataclass
class ValueObjectInputFloat3(ValueObjectInputBase):
    """ValueObjectInput<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3 | None = None


@dataclass
class ValueObjectInputDouble3(ValueObjectInputBase):
    """ValueObjectInput<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3 | None = None


@dataclass
class ValueObjectInputBool4(ValueObjectInputBase):
    """ValueObjectInput<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool4 | None = None


@dataclass
class ValueObjectInputByte4(ValueObjectInputBase):
    """ValueObjectInput<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte4 | None = None


@dataclass
class ValueObjectInputUshort4(ValueObjectInputBase):
    """ValueObjectInput<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort4 | None = None


@dataclass
class ValueObjectInputUint4(ValueObjectInputBase):
    """ValueObjectInput<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint4 | None = None


@dataclass
class ValueObjectInputUlong4(ValueObjectInputBase):
    """ValueObjectInput<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong4 | None = None


@dataclass
class ValueObjectInputSbyte4(ValueObjectInputBase):
    """ValueObjectInput<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte4 | None = None


@dataclass
class ValueObjectInputShort4(ValueObjectInputBase):
    """ValueObjectInput<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort4 | None = None


@dataclass
class ValueObjectInputInt4(ValueObjectInputBase):
    """ValueObjectInput<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt4 | None = None


@dataclass
class ValueObjectInputLong4(ValueObjectInputBase):
    """ValueObjectInput<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong4 | None = None


@dataclass
class ValueObjectInputFloat4(ValueObjectInputBase):
    """ValueObjectInput<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4 | None = None


@dataclass
class ValueObjectInputDouble4(ValueObjectInputBase):
    """ValueObjectInput<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4 | None = None


@dataclass
class ValueObjectInputFloat_2x2(ValueObjectInputBase):
    """ValueObjectInput<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2x2 | None = None


@dataclass
class ValueObjectInputDouble_2x2(ValueObjectInputBase):
    """ValueObjectInput<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2x2 | None = None


@dataclass
class ValueObjectInputFloat_3x3(ValueObjectInputBase):
    """ValueObjectInput<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3x3 | None = None


@dataclass
class ValueObjectInputDouble_3x3(ValueObjectInputBase):
    """ValueObjectInput<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3x3 | None = None


@dataclass
class ValueObjectInputFloat_4x4(ValueObjectInputBase):
    """ValueObjectInput<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4x4 | None = None


@dataclass
class ValueObjectInputDouble_4x4(ValueObjectInputBase):
    """ValueObjectInput<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4x4 | None = None


@dataclass
class ValueObjectInputFloatQ(ValueObjectInputBase):
    """ValueObjectInput<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloatQ | None = None


@dataclass
class ValueObjectInputDoubleQ(ValueObjectInputBase):
    """ValueObjectInput<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDoubleQ | None = None


@dataclass
class ValueObjectInputDateTime(ValueObjectInputBase):
    """ValueObjectInput<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDateTime | None = None


@dataclass
class ValueObjectInputTimeSpan(ValueObjectInputBase):
    """ValueObjectInput<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldTimeSpan | None = None


@dataclass
class ValueObjectInputColor(ValueObjectInputBase):
    """ValueObjectInput<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColor | None = None


@dataclass
class ValueObjectInputColorX(ValueObjectInputBase):
    """ValueObjectInput<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueObjectInput<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColorX | None = None


# Type alias for any ValueObjectInput variant
ValueObjectInput = (
    ValueObjectInputBool |
    ValueObjectInputByte |
    ValueObjectInputUshort |
    ValueObjectInputUint |
    ValueObjectInputUlong |
    ValueObjectInputSbyte |
    ValueObjectInputShort |
    ValueObjectInputInt |
    ValueObjectInputLong |
    ValueObjectInputFloat |
    ValueObjectInputDouble |
    ValueObjectInputDecimal |
    ValueObjectInputChar |
    ValueObjectInputString |
    ValueObjectInputUri |
    ValueObjectInputBool2 |
    ValueObjectInputByte2 |
    ValueObjectInputUshort2 |
    ValueObjectInputUint2 |
    ValueObjectInputUlong2 |
    ValueObjectInputSbyte2 |
    ValueObjectInputShort2 |
    ValueObjectInputInt2 |
    ValueObjectInputLong2 |
    ValueObjectInputFloat2 |
    ValueObjectInputDouble2 |
    ValueObjectInputBool3 |
    ValueObjectInputByte3 |
    ValueObjectInputUshort3 |
    ValueObjectInputUint3 |
    ValueObjectInputUlong3 |
    ValueObjectInputSbyte3 |
    ValueObjectInputShort3 |
    ValueObjectInputInt3 |
    ValueObjectInputLong3 |
    ValueObjectInputFloat3 |
    ValueObjectInputDouble3 |
    ValueObjectInputBool4 |
    ValueObjectInputByte4 |
    ValueObjectInputUshort4 |
    ValueObjectInputUint4 |
    ValueObjectInputUlong4 |
    ValueObjectInputSbyte4 |
    ValueObjectInputShort4 |
    ValueObjectInputInt4 |
    ValueObjectInputLong4 |
    ValueObjectInputFloat4 |
    ValueObjectInputDouble4 |
    ValueObjectInputFloat_2x2 |
    ValueObjectInputDouble_2x2 |
    ValueObjectInputFloat_3x3 |
    ValueObjectInputDouble_3x3 |
    ValueObjectInputFloat_4x4 |
    ValueObjectInputDouble_4x4 |
    ValueObjectInputFloatQ |
    ValueObjectInputDoubleQ |
    ValueObjectInputDateTime |
    ValueObjectInputTimeSpan |
    ValueObjectInputColor |
    ValueObjectInputColorX
)