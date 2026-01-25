"""Generated component: PickRandomValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class PickRandomValueBase(GeneratedComponent):
    """Base class for PickRandomValue<T> variants."""

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
class PickRandomValueBool(PickRandomValueBase):
    """PickRandomValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueByte(PickRandomValueBase):
    """PickRandomValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUshort(PickRandomValueBase):
    """PickRandomValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUint(PickRandomValueBase):
    """PickRandomValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUlong(PickRandomValueBase):
    """PickRandomValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueSbyte(PickRandomValueBase):
    """PickRandomValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueShort(PickRandomValueBase):
    """PickRandomValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueInt(PickRandomValueBase):
    """PickRandomValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueLong(PickRandomValueBase):
    """PickRandomValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat(PickRandomValueBase):
    """PickRandomValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble(PickRandomValueBase):
    """PickRandomValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDecimal(PickRandomValueBase):
    """PickRandomValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueChar(PickRandomValueBase):
    """PickRandomValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueString(PickRandomValueBase):
    """PickRandomValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUri(PickRandomValueBase):
    """PickRandomValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBool2(PickRandomValueBase):
    """PickRandomValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueByte2(PickRandomValueBase):
    """PickRandomValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUshort2(PickRandomValueBase):
    """PickRandomValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUint2(PickRandomValueBase):
    """PickRandomValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUlong2(PickRandomValueBase):
    """PickRandomValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueSbyte2(PickRandomValueBase):
    """PickRandomValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueShort2(PickRandomValueBase):
    """PickRandomValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueInt2(PickRandomValueBase):
    """PickRandomValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueLong2(PickRandomValueBase):
    """PickRandomValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat2(PickRandomValueBase):
    """PickRandomValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble2(PickRandomValueBase):
    """PickRandomValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBool3(PickRandomValueBase):
    """PickRandomValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueByte3(PickRandomValueBase):
    """PickRandomValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUshort3(PickRandomValueBase):
    """PickRandomValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUint3(PickRandomValueBase):
    """PickRandomValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUlong3(PickRandomValueBase):
    """PickRandomValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueSbyte3(PickRandomValueBase):
    """PickRandomValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueShort3(PickRandomValueBase):
    """PickRandomValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueInt3(PickRandomValueBase):
    """PickRandomValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueLong3(PickRandomValueBase):
    """PickRandomValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat3(PickRandomValueBase):
    """PickRandomValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble3(PickRandomValueBase):
    """PickRandomValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBool4(PickRandomValueBase):
    """PickRandomValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueByte4(PickRandomValueBase):
    """PickRandomValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUshort4(PickRandomValueBase):
    """PickRandomValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUint4(PickRandomValueBase):
    """PickRandomValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueUlong4(PickRandomValueBase):
    """PickRandomValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueSbyte4(PickRandomValueBase):
    """PickRandomValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueShort4(PickRandomValueBase):
    """PickRandomValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueInt4(PickRandomValueBase):
    """PickRandomValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueLong4(PickRandomValueBase):
    """PickRandomValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat4(PickRandomValueBase):
    """PickRandomValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble4(PickRandomValueBase):
    """PickRandomValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat_2x2(PickRandomValueBase):
    """PickRandomValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble_2x2(PickRandomValueBase):
    """PickRandomValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat_3x3(PickRandomValueBase):
    """PickRandomValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble_3x3(PickRandomValueBase):
    """PickRandomValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloat_4x4(PickRandomValueBase):
    """PickRandomValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDouble_4x4(PickRandomValueBase):
    """PickRandomValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueFloatQ(PickRandomValueBase):
    """PickRandomValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDoubleQ(PickRandomValueBase):
    """PickRandomValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDateTime(PickRandomValueBase):
    """PickRandomValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueTimeSpan(PickRandomValueBase):
    """PickRandomValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueColor(PickRandomValueBase):
    """PickRandomValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueColorX(PickRandomValueBase):
    """PickRandomValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueShadowCastMode(PickRandomValueBase):
    """PickRandomValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueLightType(PickRandomValueBase):
    """PickRandomValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueSessionAccessLevel(PickRandomValueBase):
    """PickRandomValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueKey(PickRandomValueBase):
    """PickRandomValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueHttpStatusCode(PickRandomValueBase):
    """PickRandomValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueHeadOutputDevice(PickRandomValueBase):
    """PickRandomValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueReflectionProbeClear(PickRandomValueBase):
    """PickRandomValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueReflectionProbeType(PickRandomValueBase):
    """PickRandomValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueReflectionProbeTimeSlicingMode(PickRandomValueBase):
    """PickRandomValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueCameraClearMode(PickRandomValueBase):
    """PickRandomValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueCameraPositioningMode(PickRandomValueBase):
    """PickRandomValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueCameraProjection(PickRandomValueBase):
    """PickRandomValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueZWrite(PickRandomValueBase):
    """PickRandomValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueZTest(PickRandomValueBase):
    """PickRandomValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBlend(PickRandomValueBase):
    """PickRandomValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBlendMode(PickRandomValueBase):
    """PickRandomValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueCulling(PickRandomValueBase):
    """PickRandomValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueBodyNode(PickRandomValueBase):
    """PickRandomValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueChirality(PickRandomValueBase):
    """PickRandomValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class PickRandomValueDummyEnum(PickRandomValueBase):
    """PickRandomValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.PickRandomValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


# Type alias for any PickRandomValue variant
PickRandomValue = (
    PickRandomValueBool |
    PickRandomValueByte |
    PickRandomValueUshort |
    PickRandomValueUint |
    PickRandomValueUlong |
    PickRandomValueSbyte |
    PickRandomValueShort |
    PickRandomValueInt |
    PickRandomValueLong |
    PickRandomValueFloat |
    PickRandomValueDouble |
    PickRandomValueDecimal |
    PickRandomValueChar |
    PickRandomValueString |
    PickRandomValueUri |
    PickRandomValueBool2 |
    PickRandomValueByte2 |
    PickRandomValueUshort2 |
    PickRandomValueUint2 |
    PickRandomValueUlong2 |
    PickRandomValueSbyte2 |
    PickRandomValueShort2 |
    PickRandomValueInt2 |
    PickRandomValueLong2 |
    PickRandomValueFloat2 |
    PickRandomValueDouble2 |
    PickRandomValueBool3 |
    PickRandomValueByte3 |
    PickRandomValueUshort3 |
    PickRandomValueUint3 |
    PickRandomValueUlong3 |
    PickRandomValueSbyte3 |
    PickRandomValueShort3 |
    PickRandomValueInt3 |
    PickRandomValueLong3 |
    PickRandomValueFloat3 |
    PickRandomValueDouble3 |
    PickRandomValueBool4 |
    PickRandomValueByte4 |
    PickRandomValueUshort4 |
    PickRandomValueUint4 |
    PickRandomValueUlong4 |
    PickRandomValueSbyte4 |
    PickRandomValueShort4 |
    PickRandomValueInt4 |
    PickRandomValueLong4 |
    PickRandomValueFloat4 |
    PickRandomValueDouble4 |
    PickRandomValueFloat_2x2 |
    PickRandomValueDouble_2x2 |
    PickRandomValueFloat_3x3 |
    PickRandomValueDouble_3x3 |
    PickRandomValueFloat_4x4 |
    PickRandomValueDouble_4x4 |
    PickRandomValueFloatQ |
    PickRandomValueDoubleQ |
    PickRandomValueDateTime |
    PickRandomValueTimeSpan |
    PickRandomValueColor |
    PickRandomValueColorX |
    PickRandomValueShadowCastMode |
    PickRandomValueLightType |
    PickRandomValueSessionAccessLevel |
    PickRandomValueKey |
    PickRandomValueHttpStatusCode |
    PickRandomValueHeadOutputDevice |
    PickRandomValueReflectionProbeClear |
    PickRandomValueReflectionProbeType |
    PickRandomValueReflectionProbeTimeSlicingMode |
    PickRandomValueCameraClearMode |
    PickRandomValueCameraPositioningMode |
    PickRandomValueCameraProjection |
    PickRandomValueZWrite |
    PickRandomValueZTest |
    PickRandomValueBlend |
    PickRandomValueBlendMode |
    PickRandomValueCulling |
    PickRandomValueBodyNode |
    PickRandomValueChirality |
    PickRandomValueDummyEnum
)