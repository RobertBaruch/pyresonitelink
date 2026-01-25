"""Generated component: ValueInput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldBool2, FieldBool3, FieldBool4, FieldByte, FieldByte2, FieldByte3, FieldByte4, FieldChar, FieldColor, FieldColorX, FieldDateTime, FieldDecimal, FieldDouble, FieldDouble2, FieldDouble2x2, FieldDouble3, FieldDouble3x3, FieldDouble4, FieldDouble4x4, FieldDoubleQ, FieldFloat, FieldFloat2, FieldFloat2x2, FieldFloat3, FieldFloat3x3, FieldFloat4, FieldFloat4x4, FieldFloatQ, FieldInt, FieldInt2, FieldInt3, FieldInt4, FieldLong, FieldLong2, FieldLong3, FieldLong4, FieldSbyte, FieldSbyte2, FieldSbyte3, FieldSbyte4, FieldShort, FieldShort2, FieldShort3, FieldShort4, FieldString, FieldTimeSpan, FieldUint, FieldUint2, FieldUint3, FieldUint4, FieldUlong, FieldUlong2, FieldUlong3, FieldUlong4, FieldUri, FieldUshort, FieldUshort2, FieldUshort3, FieldUshort4


@dataclass
class ValueInputBase(GeneratedComponent):
    """Base class for ValueInput<T> variants."""

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
class ValueInputBool(ValueInputBase):
    """ValueInput<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool | None = None


@dataclass
class ValueInputByte(ValueInputBase):
    """ValueInput<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte | None = None


@dataclass
class ValueInputUshort(ValueInputBase):
    """ValueInput<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort | None = None


@dataclass
class ValueInputUint(ValueInputBase):
    """ValueInput<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint | None = None


@dataclass
class ValueInputUlong(ValueInputBase):
    """ValueInput<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong | None = None


@dataclass
class ValueInputSbyte(ValueInputBase):
    """ValueInput<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte | None = None


@dataclass
class ValueInputShort(ValueInputBase):
    """ValueInput<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort | None = None


@dataclass
class ValueInputInt(ValueInputBase):
    """ValueInput<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt | None = None


@dataclass
class ValueInputLong(ValueInputBase):
    """ValueInput<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong | None = None


@dataclass
class ValueInputFloat(ValueInputBase):
    """ValueInput<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat | None = None


@dataclass
class ValueInputDouble(ValueInputBase):
    """ValueInput<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble | None = None


@dataclass
class ValueInputDecimal(ValueInputBase):
    """ValueInput<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDecimal | None = None


@dataclass
class ValueInputChar(ValueInputBase):
    """ValueInput<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldChar | None = None


@dataclass
class ValueInputString(ValueInputBase):
    """ValueInput<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldString | None = None


@dataclass
class ValueInputUri(ValueInputBase):
    """ValueInput<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUri | None = None


@dataclass
class ValueInputBool2(ValueInputBase):
    """ValueInput<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool2 | None = None


@dataclass
class ValueInputByte2(ValueInputBase):
    """ValueInput<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte2 | None = None


@dataclass
class ValueInputUshort2(ValueInputBase):
    """ValueInput<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort2 | None = None


@dataclass
class ValueInputUint2(ValueInputBase):
    """ValueInput<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint2 | None = None


@dataclass
class ValueInputUlong2(ValueInputBase):
    """ValueInput<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong2 | None = None


@dataclass
class ValueInputSbyte2(ValueInputBase):
    """ValueInput<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte2 | None = None


@dataclass
class ValueInputShort2(ValueInputBase):
    """ValueInput<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort2 | None = None


@dataclass
class ValueInputInt2(ValueInputBase):
    """ValueInput<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt2 | None = None


@dataclass
class ValueInputLong2(ValueInputBase):
    """ValueInput<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong2 | None = None


@dataclass
class ValueInputFloat2(ValueInputBase):
    """ValueInput<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2 | None = None


@dataclass
class ValueInputDouble2(ValueInputBase):
    """ValueInput<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2 | None = None


@dataclass
class ValueInputBool3(ValueInputBase):
    """ValueInput<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool3 | None = None


@dataclass
class ValueInputByte3(ValueInputBase):
    """ValueInput<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte3 | None = None


@dataclass
class ValueInputUshort3(ValueInputBase):
    """ValueInput<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort3 | None = None


@dataclass
class ValueInputUint3(ValueInputBase):
    """ValueInput<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint3 | None = None


@dataclass
class ValueInputUlong3(ValueInputBase):
    """ValueInput<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong3 | None = None


@dataclass
class ValueInputSbyte3(ValueInputBase):
    """ValueInput<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte3 | None = None


@dataclass
class ValueInputShort3(ValueInputBase):
    """ValueInput<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort3 | None = None


@dataclass
class ValueInputInt3(ValueInputBase):
    """ValueInput<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt3 | None = None


@dataclass
class ValueInputLong3(ValueInputBase):
    """ValueInput<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong3 | None = None


@dataclass
class ValueInputFloat3(ValueInputBase):
    """ValueInput<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3 | None = None


@dataclass
class ValueInputDouble3(ValueInputBase):
    """ValueInput<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3 | None = None


@dataclass
class ValueInputBool4(ValueInputBase):
    """ValueInput<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool4 | None = None


@dataclass
class ValueInputByte4(ValueInputBase):
    """ValueInput<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldByte4 | None = None


@dataclass
class ValueInputUshort4(ValueInputBase):
    """ValueInput<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUshort4 | None = None


@dataclass
class ValueInputUint4(ValueInputBase):
    """ValueInput<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUint4 | None = None


@dataclass
class ValueInputUlong4(ValueInputBase):
    """ValueInput<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldUlong4 | None = None


@dataclass
class ValueInputSbyte4(ValueInputBase):
    """ValueInput<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldSbyte4 | None = None


@dataclass
class ValueInputShort4(ValueInputBase):
    """ValueInput<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldShort4 | None = None


@dataclass
class ValueInputInt4(ValueInputBase):
    """ValueInput<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldInt4 | None = None


@dataclass
class ValueInputLong4(ValueInputBase):
    """ValueInput<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldLong4 | None = None


@dataclass
class ValueInputFloat4(ValueInputBase):
    """ValueInput<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4 | None = None


@dataclass
class ValueInputDouble4(ValueInputBase):
    """ValueInput<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4 | None = None


@dataclass
class ValueInputFloat_2x2(ValueInputBase):
    """ValueInput<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat2x2 | None = None


@dataclass
class ValueInputDouble_2x2(ValueInputBase):
    """ValueInput<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble2x2 | None = None


@dataclass
class ValueInputFloat_3x3(ValueInputBase):
    """ValueInput<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat3x3 | None = None


@dataclass
class ValueInputDouble_3x3(ValueInputBase):
    """ValueInput<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble3x3 | None = None


@dataclass
class ValueInputFloat_4x4(ValueInputBase):
    """ValueInput<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat4x4 | None = None


@dataclass
class ValueInputDouble_4x4(ValueInputBase):
    """ValueInput<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDouble4x4 | None = None


@dataclass
class ValueInputFloatQ(ValueInputBase):
    """ValueInput<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloatQ | None = None


@dataclass
class ValueInputDoubleQ(ValueInputBase):
    """ValueInput<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDoubleQ | None = None


@dataclass
class ValueInputDateTime(ValueInputBase):
    """ValueInput<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldDateTime | None = None


@dataclass
class ValueInputTimeSpan(ValueInputBase):
    """ValueInput<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldTimeSpan | None = None


@dataclass
class ValueInputColor(ValueInputBase):
    """ValueInput<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColor | None = None


@dataclass
class ValueInputColorX(ValueInputBase):
    """ValueInput<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldColorX | None = None


@dataclass
class ValueInputShadowCastMode(ValueInputBase):
    """ValueInput<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class ValueInputLightType(ValueInputBase):
    """ValueInput<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class ValueInputSessionAccessLevel(ValueInputBase):
    """ValueInput<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class ValueInputKey(ValueInputBase):
    """ValueInput<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class ValueInputHttpStatusCode(ValueInputBase):
    """ValueInput<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class ValueInputHeadOutputDevice(ValueInputBase):
    """ValueInput<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class ValueInputReflectionProbeClear(ValueInputBase):
    """ValueInput<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class ValueInputReflectionProbeType(ValueInputBase):
    """ValueInput<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class ValueInputReflectionProbeTimeSlicingMode(ValueInputBase):
    """ValueInput<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class ValueInputCameraClearMode(ValueInputBase):
    """ValueInput<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class ValueInputCameraPositioningMode(ValueInputBase):
    """ValueInput<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class ValueInputCameraProjection(ValueInputBase):
    """ValueInput<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class ValueInputZWrite(ValueInputBase):
    """ValueInput<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class ValueInputZTest(ValueInputBase):
    """ValueInput<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class ValueInputBlend(ValueInputBase):
    """ValueInput<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class ValueInputBlendMode(ValueInputBase):
    """ValueInput<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class ValueInputCulling(ValueInputBase):
    """ValueInput<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class ValueInputBodyNode(ValueInputBase):
    """ValueInput<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class ValueInputChirality(ValueInputBase):
    """ValueInput<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class ValueInputDummyEnum(ValueInputBase):
    """ValueInput<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueInput<DummyEnum>"

    pass


# Type alias for any ValueInput variant
ValueInput = (
    ValueInputBool |
    ValueInputByte |
    ValueInputUshort |
    ValueInputUint |
    ValueInputUlong |
    ValueInputSbyte |
    ValueInputShort |
    ValueInputInt |
    ValueInputLong |
    ValueInputFloat |
    ValueInputDouble |
    ValueInputDecimal |
    ValueInputChar |
    ValueInputString |
    ValueInputUri |
    ValueInputBool2 |
    ValueInputByte2 |
    ValueInputUshort2 |
    ValueInputUint2 |
    ValueInputUlong2 |
    ValueInputSbyte2 |
    ValueInputShort2 |
    ValueInputInt2 |
    ValueInputLong2 |
    ValueInputFloat2 |
    ValueInputDouble2 |
    ValueInputBool3 |
    ValueInputByte3 |
    ValueInputUshort3 |
    ValueInputUint3 |
    ValueInputUlong3 |
    ValueInputSbyte3 |
    ValueInputShort3 |
    ValueInputInt3 |
    ValueInputLong3 |
    ValueInputFloat3 |
    ValueInputDouble3 |
    ValueInputBool4 |
    ValueInputByte4 |
    ValueInputUshort4 |
    ValueInputUint4 |
    ValueInputUlong4 |
    ValueInputSbyte4 |
    ValueInputShort4 |
    ValueInputInt4 |
    ValueInputLong4 |
    ValueInputFloat4 |
    ValueInputDouble4 |
    ValueInputFloat_2x2 |
    ValueInputDouble_2x2 |
    ValueInputFloat_3x3 |
    ValueInputDouble_3x3 |
    ValueInputFloat_4x4 |
    ValueInputDouble_4x4 |
    ValueInputFloatQ |
    ValueInputDoubleQ |
    ValueInputDateTime |
    ValueInputTimeSpan |
    ValueInputColor |
    ValueInputColorX |
    ValueInputShadowCastMode |
    ValueInputLightType |
    ValueInputSessionAccessLevel |
    ValueInputKey |
    ValueInputHttpStatusCode |
    ValueInputHeadOutputDevice |
    ValueInputReflectionProbeClear |
    ValueInputReflectionProbeType |
    ValueInputReflectionProbeTimeSlicingMode |
    ValueInputCameraClearMode |
    ValueInputCameraPositioningMode |
    ValueInputCameraProjection |
    ValueInputZWrite |
    ValueInputZTest |
    ValueInputBlend |
    ValueInputBlendMode |
    ValueInputCulling |
    ValueInputBodyNode |
    ValueInputChirality |
    ValueInputDummyEnum
)