"""Generated component: ValueAddMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueAddMultiBase(GeneratedComponent):
    """Base class for ValueAddMulti<T> variants."""

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
class ValueAddMultiBool(ValueAddMultiBase):
    """ValueAddMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiByte(ValueAddMultiBase):
    """ValueAddMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUshort(ValueAddMultiBase):
    """ValueAddMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUint(ValueAddMultiBase):
    """ValueAddMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUlong(ValueAddMultiBase):
    """ValueAddMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiSbyte(ValueAddMultiBase):
    """ValueAddMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiShort(ValueAddMultiBase):
    """ValueAddMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiInt(ValueAddMultiBase):
    """ValueAddMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiLong(ValueAddMultiBase):
    """ValueAddMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat(ValueAddMultiBase):
    """ValueAddMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble(ValueAddMultiBase):
    """ValueAddMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDecimal(ValueAddMultiBase):
    """ValueAddMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiChar(ValueAddMultiBase):
    """ValueAddMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiString(ValueAddMultiBase):
    """ValueAddMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUri(ValueAddMultiBase):
    """ValueAddMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBool2(ValueAddMultiBase):
    """ValueAddMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiByte2(ValueAddMultiBase):
    """ValueAddMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUshort2(ValueAddMultiBase):
    """ValueAddMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUint2(ValueAddMultiBase):
    """ValueAddMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUlong2(ValueAddMultiBase):
    """ValueAddMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiSbyte2(ValueAddMultiBase):
    """ValueAddMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiShort2(ValueAddMultiBase):
    """ValueAddMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiInt2(ValueAddMultiBase):
    """ValueAddMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiLong2(ValueAddMultiBase):
    """ValueAddMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat2(ValueAddMultiBase):
    """ValueAddMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble2(ValueAddMultiBase):
    """ValueAddMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBool3(ValueAddMultiBase):
    """ValueAddMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiByte3(ValueAddMultiBase):
    """ValueAddMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUshort3(ValueAddMultiBase):
    """ValueAddMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUint3(ValueAddMultiBase):
    """ValueAddMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUlong3(ValueAddMultiBase):
    """ValueAddMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiSbyte3(ValueAddMultiBase):
    """ValueAddMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiShort3(ValueAddMultiBase):
    """ValueAddMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiInt3(ValueAddMultiBase):
    """ValueAddMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiLong3(ValueAddMultiBase):
    """ValueAddMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat3(ValueAddMultiBase):
    """ValueAddMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble3(ValueAddMultiBase):
    """ValueAddMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBool4(ValueAddMultiBase):
    """ValueAddMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiByte4(ValueAddMultiBase):
    """ValueAddMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUshort4(ValueAddMultiBase):
    """ValueAddMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUint4(ValueAddMultiBase):
    """ValueAddMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiUlong4(ValueAddMultiBase):
    """ValueAddMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiSbyte4(ValueAddMultiBase):
    """ValueAddMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiShort4(ValueAddMultiBase):
    """ValueAddMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiInt4(ValueAddMultiBase):
    """ValueAddMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiLong4(ValueAddMultiBase):
    """ValueAddMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat4(ValueAddMultiBase):
    """ValueAddMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble4(ValueAddMultiBase):
    """ValueAddMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat_2x2(ValueAddMultiBase):
    """ValueAddMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble_2x2(ValueAddMultiBase):
    """ValueAddMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat_3x3(ValueAddMultiBase):
    """ValueAddMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble_3x3(ValueAddMultiBase):
    """ValueAddMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloat_4x4(ValueAddMultiBase):
    """ValueAddMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDouble_4x4(ValueAddMultiBase):
    """ValueAddMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiFloatQ(ValueAddMultiBase):
    """ValueAddMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDoubleQ(ValueAddMultiBase):
    """ValueAddMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDateTime(ValueAddMultiBase):
    """ValueAddMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiTimeSpan(ValueAddMultiBase):
    """ValueAddMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiColor(ValueAddMultiBase):
    """ValueAddMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiColorX(ValueAddMultiBase):
    """ValueAddMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiShadowCastMode(ValueAddMultiBase):
    """ValueAddMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiLightType(ValueAddMultiBase):
    """ValueAddMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiSessionAccessLevel(ValueAddMultiBase):
    """ValueAddMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiKey(ValueAddMultiBase):
    """ValueAddMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiHttpStatusCode(ValueAddMultiBase):
    """ValueAddMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiHeadOutputDevice(ValueAddMultiBase):
    """ValueAddMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiReflectionProbeClear(ValueAddMultiBase):
    """ValueAddMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiReflectionProbeType(ValueAddMultiBase):
    """ValueAddMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiReflectionProbeTimeSlicingMode(ValueAddMultiBase):
    """ValueAddMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiCameraClearMode(ValueAddMultiBase):
    """ValueAddMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiCameraPositioningMode(ValueAddMultiBase):
    """ValueAddMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiCameraProjection(ValueAddMultiBase):
    """ValueAddMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiZWrite(ValueAddMultiBase):
    """ValueAddMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiZTest(ValueAddMultiBase):
    """ValueAddMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBlend(ValueAddMultiBase):
    """ValueAddMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBlendMode(ValueAddMultiBase):
    """ValueAddMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiCulling(ValueAddMultiBase):
    """ValueAddMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiBodyNode(ValueAddMultiBase):
    """ValueAddMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiChirality(ValueAddMultiBase):
    """ValueAddMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueAddMultiDummyEnum(ValueAddMultiBase):
    """ValueAddMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueAddMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


# Type alias for any ValueAddMulti variant
ValueAddMulti = (
    ValueAddMultiBool |
    ValueAddMultiByte |
    ValueAddMultiUshort |
    ValueAddMultiUint |
    ValueAddMultiUlong |
    ValueAddMultiSbyte |
    ValueAddMultiShort |
    ValueAddMultiInt |
    ValueAddMultiLong |
    ValueAddMultiFloat |
    ValueAddMultiDouble |
    ValueAddMultiDecimal |
    ValueAddMultiChar |
    ValueAddMultiString |
    ValueAddMultiUri |
    ValueAddMultiBool2 |
    ValueAddMultiByte2 |
    ValueAddMultiUshort2 |
    ValueAddMultiUint2 |
    ValueAddMultiUlong2 |
    ValueAddMultiSbyte2 |
    ValueAddMultiShort2 |
    ValueAddMultiInt2 |
    ValueAddMultiLong2 |
    ValueAddMultiFloat2 |
    ValueAddMultiDouble2 |
    ValueAddMultiBool3 |
    ValueAddMultiByte3 |
    ValueAddMultiUshort3 |
    ValueAddMultiUint3 |
    ValueAddMultiUlong3 |
    ValueAddMultiSbyte3 |
    ValueAddMultiShort3 |
    ValueAddMultiInt3 |
    ValueAddMultiLong3 |
    ValueAddMultiFloat3 |
    ValueAddMultiDouble3 |
    ValueAddMultiBool4 |
    ValueAddMultiByte4 |
    ValueAddMultiUshort4 |
    ValueAddMultiUint4 |
    ValueAddMultiUlong4 |
    ValueAddMultiSbyte4 |
    ValueAddMultiShort4 |
    ValueAddMultiInt4 |
    ValueAddMultiLong4 |
    ValueAddMultiFloat4 |
    ValueAddMultiDouble4 |
    ValueAddMultiFloat_2x2 |
    ValueAddMultiDouble_2x2 |
    ValueAddMultiFloat_3x3 |
    ValueAddMultiDouble_3x3 |
    ValueAddMultiFloat_4x4 |
    ValueAddMultiDouble_4x4 |
    ValueAddMultiFloatQ |
    ValueAddMultiDoubleQ |
    ValueAddMultiDateTime |
    ValueAddMultiTimeSpan |
    ValueAddMultiColor |
    ValueAddMultiColorX |
    ValueAddMultiShadowCastMode |
    ValueAddMultiLightType |
    ValueAddMultiSessionAccessLevel |
    ValueAddMultiKey |
    ValueAddMultiHttpStatusCode |
    ValueAddMultiHeadOutputDevice |
    ValueAddMultiReflectionProbeClear |
    ValueAddMultiReflectionProbeType |
    ValueAddMultiReflectionProbeTimeSlicingMode |
    ValueAddMultiCameraClearMode |
    ValueAddMultiCameraPositioningMode |
    ValueAddMultiCameraProjection |
    ValueAddMultiZWrite |
    ValueAddMultiZTest |
    ValueAddMultiBlend |
    ValueAddMultiBlendMode |
    ValueAddMultiCulling |
    ValueAddMultiBodyNode |
    ValueAddMultiChirality |
    ValueAddMultiDummyEnum
)