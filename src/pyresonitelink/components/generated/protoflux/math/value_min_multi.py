"""Generated component: ValueMinMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueMinMultiBase(GeneratedComponent):
    """Base class for ValueMinMulti<T> variants."""

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
class ValueMinMultiBool(ValueMinMultiBase):
    """ValueMinMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiByte(ValueMinMultiBase):
    """ValueMinMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUshort(ValueMinMultiBase):
    """ValueMinMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUint(ValueMinMultiBase):
    """ValueMinMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUlong(ValueMinMultiBase):
    """ValueMinMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiSbyte(ValueMinMultiBase):
    """ValueMinMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiShort(ValueMinMultiBase):
    """ValueMinMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiInt(ValueMinMultiBase):
    """ValueMinMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiLong(ValueMinMultiBase):
    """ValueMinMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat(ValueMinMultiBase):
    """ValueMinMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble(ValueMinMultiBase):
    """ValueMinMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDecimal(ValueMinMultiBase):
    """ValueMinMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiChar(ValueMinMultiBase):
    """ValueMinMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiString(ValueMinMultiBase):
    """ValueMinMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUri(ValueMinMultiBase):
    """ValueMinMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBool2(ValueMinMultiBase):
    """ValueMinMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiByte2(ValueMinMultiBase):
    """ValueMinMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUshort2(ValueMinMultiBase):
    """ValueMinMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUint2(ValueMinMultiBase):
    """ValueMinMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUlong2(ValueMinMultiBase):
    """ValueMinMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiSbyte2(ValueMinMultiBase):
    """ValueMinMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiShort2(ValueMinMultiBase):
    """ValueMinMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiInt2(ValueMinMultiBase):
    """ValueMinMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiLong2(ValueMinMultiBase):
    """ValueMinMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat2(ValueMinMultiBase):
    """ValueMinMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble2(ValueMinMultiBase):
    """ValueMinMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBool3(ValueMinMultiBase):
    """ValueMinMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiByte3(ValueMinMultiBase):
    """ValueMinMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUshort3(ValueMinMultiBase):
    """ValueMinMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUint3(ValueMinMultiBase):
    """ValueMinMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUlong3(ValueMinMultiBase):
    """ValueMinMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiSbyte3(ValueMinMultiBase):
    """ValueMinMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiShort3(ValueMinMultiBase):
    """ValueMinMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiInt3(ValueMinMultiBase):
    """ValueMinMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiLong3(ValueMinMultiBase):
    """ValueMinMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat3(ValueMinMultiBase):
    """ValueMinMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble3(ValueMinMultiBase):
    """ValueMinMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBool4(ValueMinMultiBase):
    """ValueMinMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiByte4(ValueMinMultiBase):
    """ValueMinMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUshort4(ValueMinMultiBase):
    """ValueMinMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUint4(ValueMinMultiBase):
    """ValueMinMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiUlong4(ValueMinMultiBase):
    """ValueMinMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiSbyte4(ValueMinMultiBase):
    """ValueMinMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiShort4(ValueMinMultiBase):
    """ValueMinMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiInt4(ValueMinMultiBase):
    """ValueMinMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiLong4(ValueMinMultiBase):
    """ValueMinMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat4(ValueMinMultiBase):
    """ValueMinMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble4(ValueMinMultiBase):
    """ValueMinMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat_2x2(ValueMinMultiBase):
    """ValueMinMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble_2x2(ValueMinMultiBase):
    """ValueMinMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat_3x3(ValueMinMultiBase):
    """ValueMinMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble_3x3(ValueMinMultiBase):
    """ValueMinMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloat_4x4(ValueMinMultiBase):
    """ValueMinMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDouble_4x4(ValueMinMultiBase):
    """ValueMinMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiFloatQ(ValueMinMultiBase):
    """ValueMinMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDoubleQ(ValueMinMultiBase):
    """ValueMinMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDateTime(ValueMinMultiBase):
    """ValueMinMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiTimeSpan(ValueMinMultiBase):
    """ValueMinMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiColor(ValueMinMultiBase):
    """ValueMinMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiColorX(ValueMinMultiBase):
    """ValueMinMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiShadowCastMode(ValueMinMultiBase):
    """ValueMinMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiLightType(ValueMinMultiBase):
    """ValueMinMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiSessionAccessLevel(ValueMinMultiBase):
    """ValueMinMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiKey(ValueMinMultiBase):
    """ValueMinMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiHttpStatusCode(ValueMinMultiBase):
    """ValueMinMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiHeadOutputDevice(ValueMinMultiBase):
    """ValueMinMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiReflectionProbeClear(ValueMinMultiBase):
    """ValueMinMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiReflectionProbeType(ValueMinMultiBase):
    """ValueMinMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiReflectionProbeTimeSlicingMode(ValueMinMultiBase):
    """ValueMinMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiCameraClearMode(ValueMinMultiBase):
    """ValueMinMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiCameraPositioningMode(ValueMinMultiBase):
    """ValueMinMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiCameraProjection(ValueMinMultiBase):
    """ValueMinMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiZWrite(ValueMinMultiBase):
    """ValueMinMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiZTest(ValueMinMultiBase):
    """ValueMinMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBlend(ValueMinMultiBase):
    """ValueMinMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBlendMode(ValueMinMultiBase):
    """ValueMinMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiCulling(ValueMinMultiBase):
    """ValueMinMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiBodyNode(ValueMinMultiBase):
    """ValueMinMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiChirality(ValueMinMultiBase):
    """ValueMinMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


@dataclass
class ValueMinMultiDummyEnum(ValueMinMultiBase):
    """ValueMinMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMinMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "operands": "Operands",
    }

    operands: SyncList | None = None


# Type alias for any ValueMinMulti variant
ValueMinMulti = (
    ValueMinMultiBool |
    ValueMinMultiByte |
    ValueMinMultiUshort |
    ValueMinMultiUint |
    ValueMinMultiUlong |
    ValueMinMultiSbyte |
    ValueMinMultiShort |
    ValueMinMultiInt |
    ValueMinMultiLong |
    ValueMinMultiFloat |
    ValueMinMultiDouble |
    ValueMinMultiDecimal |
    ValueMinMultiChar |
    ValueMinMultiString |
    ValueMinMultiUri |
    ValueMinMultiBool2 |
    ValueMinMultiByte2 |
    ValueMinMultiUshort2 |
    ValueMinMultiUint2 |
    ValueMinMultiUlong2 |
    ValueMinMultiSbyte2 |
    ValueMinMultiShort2 |
    ValueMinMultiInt2 |
    ValueMinMultiLong2 |
    ValueMinMultiFloat2 |
    ValueMinMultiDouble2 |
    ValueMinMultiBool3 |
    ValueMinMultiByte3 |
    ValueMinMultiUshort3 |
    ValueMinMultiUint3 |
    ValueMinMultiUlong3 |
    ValueMinMultiSbyte3 |
    ValueMinMultiShort3 |
    ValueMinMultiInt3 |
    ValueMinMultiLong3 |
    ValueMinMultiFloat3 |
    ValueMinMultiDouble3 |
    ValueMinMultiBool4 |
    ValueMinMultiByte4 |
    ValueMinMultiUshort4 |
    ValueMinMultiUint4 |
    ValueMinMultiUlong4 |
    ValueMinMultiSbyte4 |
    ValueMinMultiShort4 |
    ValueMinMultiInt4 |
    ValueMinMultiLong4 |
    ValueMinMultiFloat4 |
    ValueMinMultiDouble4 |
    ValueMinMultiFloat_2x2 |
    ValueMinMultiDouble_2x2 |
    ValueMinMultiFloat_3x3 |
    ValueMinMultiDouble_3x3 |
    ValueMinMultiFloat_4x4 |
    ValueMinMultiDouble_4x4 |
    ValueMinMultiFloatQ |
    ValueMinMultiDoubleQ |
    ValueMinMultiDateTime |
    ValueMinMultiTimeSpan |
    ValueMinMultiColor |
    ValueMinMultiColorX |
    ValueMinMultiShadowCastMode |
    ValueMinMultiLightType |
    ValueMinMultiSessionAccessLevel |
    ValueMinMultiKey |
    ValueMinMultiHttpStatusCode |
    ValueMinMultiHeadOutputDevice |
    ValueMinMultiReflectionProbeClear |
    ValueMinMultiReflectionProbeType |
    ValueMinMultiReflectionProbeTimeSlicingMode |
    ValueMinMultiCameraClearMode |
    ValueMinMultiCameraPositioningMode |
    ValueMinMultiCameraProjection |
    ValueMinMultiZWrite |
    ValueMinMultiZTest |
    ValueMinMultiBlend |
    ValueMinMultiBlendMode |
    ValueMinMultiCulling |
    ValueMinMultiBodyNode |
    ValueMinMultiChirality |
    ValueMinMultiDummyEnum
)