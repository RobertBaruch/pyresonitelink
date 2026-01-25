"""Generated component: ValueMaxMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueMaxMultiBase(GeneratedComponent):
    """Base class for ValueMaxMulti<T> variants."""

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
class ValueMaxMultiBool(ValueMaxMultiBase):
    """ValueMaxMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiByte(ValueMaxMultiBase):
    """ValueMaxMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUshort(ValueMaxMultiBase):
    """ValueMaxMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUint(ValueMaxMultiBase):
    """ValueMaxMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUlong(ValueMaxMultiBase):
    """ValueMaxMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiSbyte(ValueMaxMultiBase):
    """ValueMaxMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiShort(ValueMaxMultiBase):
    """ValueMaxMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiInt(ValueMaxMultiBase):
    """ValueMaxMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiLong(ValueMaxMultiBase):
    """ValueMaxMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat(ValueMaxMultiBase):
    """ValueMaxMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble(ValueMaxMultiBase):
    """ValueMaxMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDecimal(ValueMaxMultiBase):
    """ValueMaxMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiChar(ValueMaxMultiBase):
    """ValueMaxMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiString(ValueMaxMultiBase):
    """ValueMaxMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUri(ValueMaxMultiBase):
    """ValueMaxMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBool2(ValueMaxMultiBase):
    """ValueMaxMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiByte2(ValueMaxMultiBase):
    """ValueMaxMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUshort2(ValueMaxMultiBase):
    """ValueMaxMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUint2(ValueMaxMultiBase):
    """ValueMaxMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUlong2(ValueMaxMultiBase):
    """ValueMaxMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiSbyte2(ValueMaxMultiBase):
    """ValueMaxMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiShort2(ValueMaxMultiBase):
    """ValueMaxMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiInt2(ValueMaxMultiBase):
    """ValueMaxMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiLong2(ValueMaxMultiBase):
    """ValueMaxMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat2(ValueMaxMultiBase):
    """ValueMaxMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble2(ValueMaxMultiBase):
    """ValueMaxMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBool3(ValueMaxMultiBase):
    """ValueMaxMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiByte3(ValueMaxMultiBase):
    """ValueMaxMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUshort3(ValueMaxMultiBase):
    """ValueMaxMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUint3(ValueMaxMultiBase):
    """ValueMaxMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUlong3(ValueMaxMultiBase):
    """ValueMaxMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiSbyte3(ValueMaxMultiBase):
    """ValueMaxMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiShort3(ValueMaxMultiBase):
    """ValueMaxMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiInt3(ValueMaxMultiBase):
    """ValueMaxMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiLong3(ValueMaxMultiBase):
    """ValueMaxMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat3(ValueMaxMultiBase):
    """ValueMaxMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble3(ValueMaxMultiBase):
    """ValueMaxMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBool4(ValueMaxMultiBase):
    """ValueMaxMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiByte4(ValueMaxMultiBase):
    """ValueMaxMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUshort4(ValueMaxMultiBase):
    """ValueMaxMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUint4(ValueMaxMultiBase):
    """ValueMaxMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiUlong4(ValueMaxMultiBase):
    """ValueMaxMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiSbyte4(ValueMaxMultiBase):
    """ValueMaxMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiShort4(ValueMaxMultiBase):
    """ValueMaxMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiInt4(ValueMaxMultiBase):
    """ValueMaxMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiLong4(ValueMaxMultiBase):
    """ValueMaxMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat4(ValueMaxMultiBase):
    """ValueMaxMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble4(ValueMaxMultiBase):
    """ValueMaxMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat_2x2(ValueMaxMultiBase):
    """ValueMaxMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble_2x2(ValueMaxMultiBase):
    """ValueMaxMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat_3x3(ValueMaxMultiBase):
    """ValueMaxMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble_3x3(ValueMaxMultiBase):
    """ValueMaxMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloat_4x4(ValueMaxMultiBase):
    """ValueMaxMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDouble_4x4(ValueMaxMultiBase):
    """ValueMaxMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiFloatQ(ValueMaxMultiBase):
    """ValueMaxMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDoubleQ(ValueMaxMultiBase):
    """ValueMaxMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDateTime(ValueMaxMultiBase):
    """ValueMaxMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiTimeSpan(ValueMaxMultiBase):
    """ValueMaxMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiColor(ValueMaxMultiBase):
    """ValueMaxMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiColorX(ValueMaxMultiBase):
    """ValueMaxMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiShadowCastMode(ValueMaxMultiBase):
    """ValueMaxMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiLightType(ValueMaxMultiBase):
    """ValueMaxMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiSessionAccessLevel(ValueMaxMultiBase):
    """ValueMaxMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiKey(ValueMaxMultiBase):
    """ValueMaxMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiHttpStatusCode(ValueMaxMultiBase):
    """ValueMaxMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiHeadOutputDevice(ValueMaxMultiBase):
    """ValueMaxMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiReflectionProbeClear(ValueMaxMultiBase):
    """ValueMaxMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiReflectionProbeType(ValueMaxMultiBase):
    """ValueMaxMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiReflectionProbeTimeSlicingMode(ValueMaxMultiBase):
    """ValueMaxMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiCameraClearMode(ValueMaxMultiBase):
    """ValueMaxMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiCameraPositioningMode(ValueMaxMultiBase):
    """ValueMaxMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiCameraProjection(ValueMaxMultiBase):
    """ValueMaxMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiZWrite(ValueMaxMultiBase):
    """ValueMaxMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiZTest(ValueMaxMultiBase):
    """ValueMaxMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBlend(ValueMaxMultiBase):
    """ValueMaxMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBlendMode(ValueMaxMultiBase):
    """ValueMaxMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiCulling(ValueMaxMultiBase):
    """ValueMaxMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiBodyNode(ValueMaxMultiBase):
    """ValueMaxMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiChirality(ValueMaxMultiBase):
    """ValueMaxMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMaxMultiDummyEnum(ValueMaxMultiBase):
    """ValueMaxMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMaxMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


# Type alias for any ValueMaxMulti variant
ValueMaxMulti = (
    ValueMaxMultiBool |
    ValueMaxMultiByte |
    ValueMaxMultiUshort |
    ValueMaxMultiUint |
    ValueMaxMultiUlong |
    ValueMaxMultiSbyte |
    ValueMaxMultiShort |
    ValueMaxMultiInt |
    ValueMaxMultiLong |
    ValueMaxMultiFloat |
    ValueMaxMultiDouble |
    ValueMaxMultiDecimal |
    ValueMaxMultiChar |
    ValueMaxMultiString |
    ValueMaxMultiUri |
    ValueMaxMultiBool2 |
    ValueMaxMultiByte2 |
    ValueMaxMultiUshort2 |
    ValueMaxMultiUint2 |
    ValueMaxMultiUlong2 |
    ValueMaxMultiSbyte2 |
    ValueMaxMultiShort2 |
    ValueMaxMultiInt2 |
    ValueMaxMultiLong2 |
    ValueMaxMultiFloat2 |
    ValueMaxMultiDouble2 |
    ValueMaxMultiBool3 |
    ValueMaxMultiByte3 |
    ValueMaxMultiUshort3 |
    ValueMaxMultiUint3 |
    ValueMaxMultiUlong3 |
    ValueMaxMultiSbyte3 |
    ValueMaxMultiShort3 |
    ValueMaxMultiInt3 |
    ValueMaxMultiLong3 |
    ValueMaxMultiFloat3 |
    ValueMaxMultiDouble3 |
    ValueMaxMultiBool4 |
    ValueMaxMultiByte4 |
    ValueMaxMultiUshort4 |
    ValueMaxMultiUint4 |
    ValueMaxMultiUlong4 |
    ValueMaxMultiSbyte4 |
    ValueMaxMultiShort4 |
    ValueMaxMultiInt4 |
    ValueMaxMultiLong4 |
    ValueMaxMultiFloat4 |
    ValueMaxMultiDouble4 |
    ValueMaxMultiFloat_2x2 |
    ValueMaxMultiDouble_2x2 |
    ValueMaxMultiFloat_3x3 |
    ValueMaxMultiDouble_3x3 |
    ValueMaxMultiFloat_4x4 |
    ValueMaxMultiDouble_4x4 |
    ValueMaxMultiFloatQ |
    ValueMaxMultiDoubleQ |
    ValueMaxMultiDateTime |
    ValueMaxMultiTimeSpan |
    ValueMaxMultiColor |
    ValueMaxMultiColorX |
    ValueMaxMultiShadowCastMode |
    ValueMaxMultiLightType |
    ValueMaxMultiSessionAccessLevel |
    ValueMaxMultiKey |
    ValueMaxMultiHttpStatusCode |
    ValueMaxMultiHeadOutputDevice |
    ValueMaxMultiReflectionProbeClear |
    ValueMaxMultiReflectionProbeType |
    ValueMaxMultiReflectionProbeTimeSlicingMode |
    ValueMaxMultiCameraClearMode |
    ValueMaxMultiCameraPositioningMode |
    ValueMaxMultiCameraProjection |
    ValueMaxMultiZWrite |
    ValueMaxMultiZTest |
    ValueMaxMultiBlend |
    ValueMaxMultiBlendMode |
    ValueMaxMultiCulling |
    ValueMaxMultiBodyNode |
    ValueMaxMultiChirality |
    ValueMaxMultiDummyEnum
)