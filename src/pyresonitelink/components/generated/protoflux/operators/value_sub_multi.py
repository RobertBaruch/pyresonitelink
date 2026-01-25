"""Generated component: ValueSubMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueSubMultiBase(GeneratedComponent):
    """Base class for ValueSubMulti<T> variants."""

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
class ValueSubMultiBool(ValueSubMultiBase):
    """ValueSubMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiByte(ValueSubMultiBase):
    """ValueSubMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUshort(ValueSubMultiBase):
    """ValueSubMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUint(ValueSubMultiBase):
    """ValueSubMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUlong(ValueSubMultiBase):
    """ValueSubMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiSbyte(ValueSubMultiBase):
    """ValueSubMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiShort(ValueSubMultiBase):
    """ValueSubMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiInt(ValueSubMultiBase):
    """ValueSubMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiLong(ValueSubMultiBase):
    """ValueSubMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat(ValueSubMultiBase):
    """ValueSubMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble(ValueSubMultiBase):
    """ValueSubMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDecimal(ValueSubMultiBase):
    """ValueSubMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiChar(ValueSubMultiBase):
    """ValueSubMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiString(ValueSubMultiBase):
    """ValueSubMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUri(ValueSubMultiBase):
    """ValueSubMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBool2(ValueSubMultiBase):
    """ValueSubMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiByte2(ValueSubMultiBase):
    """ValueSubMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUshort2(ValueSubMultiBase):
    """ValueSubMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUint2(ValueSubMultiBase):
    """ValueSubMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUlong2(ValueSubMultiBase):
    """ValueSubMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiSbyte2(ValueSubMultiBase):
    """ValueSubMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiShort2(ValueSubMultiBase):
    """ValueSubMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiInt2(ValueSubMultiBase):
    """ValueSubMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiLong2(ValueSubMultiBase):
    """ValueSubMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat2(ValueSubMultiBase):
    """ValueSubMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble2(ValueSubMultiBase):
    """ValueSubMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBool3(ValueSubMultiBase):
    """ValueSubMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiByte3(ValueSubMultiBase):
    """ValueSubMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUshort3(ValueSubMultiBase):
    """ValueSubMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUint3(ValueSubMultiBase):
    """ValueSubMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUlong3(ValueSubMultiBase):
    """ValueSubMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiSbyte3(ValueSubMultiBase):
    """ValueSubMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiShort3(ValueSubMultiBase):
    """ValueSubMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiInt3(ValueSubMultiBase):
    """ValueSubMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiLong3(ValueSubMultiBase):
    """ValueSubMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat3(ValueSubMultiBase):
    """ValueSubMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble3(ValueSubMultiBase):
    """ValueSubMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBool4(ValueSubMultiBase):
    """ValueSubMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiByte4(ValueSubMultiBase):
    """ValueSubMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUshort4(ValueSubMultiBase):
    """ValueSubMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUint4(ValueSubMultiBase):
    """ValueSubMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiUlong4(ValueSubMultiBase):
    """ValueSubMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiSbyte4(ValueSubMultiBase):
    """ValueSubMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiShort4(ValueSubMultiBase):
    """ValueSubMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiInt4(ValueSubMultiBase):
    """ValueSubMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiLong4(ValueSubMultiBase):
    """ValueSubMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat4(ValueSubMultiBase):
    """ValueSubMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble4(ValueSubMultiBase):
    """ValueSubMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat_2x2(ValueSubMultiBase):
    """ValueSubMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble_2x2(ValueSubMultiBase):
    """ValueSubMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat_3x3(ValueSubMultiBase):
    """ValueSubMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble_3x3(ValueSubMultiBase):
    """ValueSubMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloat_4x4(ValueSubMultiBase):
    """ValueSubMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDouble_4x4(ValueSubMultiBase):
    """ValueSubMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiFloatQ(ValueSubMultiBase):
    """ValueSubMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDoubleQ(ValueSubMultiBase):
    """ValueSubMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDateTime(ValueSubMultiBase):
    """ValueSubMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiTimeSpan(ValueSubMultiBase):
    """ValueSubMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiColor(ValueSubMultiBase):
    """ValueSubMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiColorX(ValueSubMultiBase):
    """ValueSubMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiShadowCastMode(ValueSubMultiBase):
    """ValueSubMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiLightType(ValueSubMultiBase):
    """ValueSubMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiSessionAccessLevel(ValueSubMultiBase):
    """ValueSubMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiKey(ValueSubMultiBase):
    """ValueSubMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiHttpStatusCode(ValueSubMultiBase):
    """ValueSubMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiHeadOutputDevice(ValueSubMultiBase):
    """ValueSubMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiReflectionProbeClear(ValueSubMultiBase):
    """ValueSubMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiReflectionProbeType(ValueSubMultiBase):
    """ValueSubMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiReflectionProbeTimeSlicingMode(ValueSubMultiBase):
    """ValueSubMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiCameraClearMode(ValueSubMultiBase):
    """ValueSubMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiCameraPositioningMode(ValueSubMultiBase):
    """ValueSubMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiCameraProjection(ValueSubMultiBase):
    """ValueSubMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiZWrite(ValueSubMultiBase):
    """ValueSubMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiZTest(ValueSubMultiBase):
    """ValueSubMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBlend(ValueSubMultiBase):
    """ValueSubMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBlendMode(ValueSubMultiBase):
    """ValueSubMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiCulling(ValueSubMultiBase):
    """ValueSubMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiBodyNode(ValueSubMultiBase):
    """ValueSubMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiChirality(ValueSubMultiBase):
    """ValueSubMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueSubMultiDummyEnum(ValueSubMultiBase):
    """ValueSubMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSubMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


# Type alias for any ValueSubMulti variant
ValueSubMulti = (
    ValueSubMultiBool |
    ValueSubMultiByte |
    ValueSubMultiUshort |
    ValueSubMultiUint |
    ValueSubMultiUlong |
    ValueSubMultiSbyte |
    ValueSubMultiShort |
    ValueSubMultiInt |
    ValueSubMultiLong |
    ValueSubMultiFloat |
    ValueSubMultiDouble |
    ValueSubMultiDecimal |
    ValueSubMultiChar |
    ValueSubMultiString |
    ValueSubMultiUri |
    ValueSubMultiBool2 |
    ValueSubMultiByte2 |
    ValueSubMultiUshort2 |
    ValueSubMultiUint2 |
    ValueSubMultiUlong2 |
    ValueSubMultiSbyte2 |
    ValueSubMultiShort2 |
    ValueSubMultiInt2 |
    ValueSubMultiLong2 |
    ValueSubMultiFloat2 |
    ValueSubMultiDouble2 |
    ValueSubMultiBool3 |
    ValueSubMultiByte3 |
    ValueSubMultiUshort3 |
    ValueSubMultiUint3 |
    ValueSubMultiUlong3 |
    ValueSubMultiSbyte3 |
    ValueSubMultiShort3 |
    ValueSubMultiInt3 |
    ValueSubMultiLong3 |
    ValueSubMultiFloat3 |
    ValueSubMultiDouble3 |
    ValueSubMultiBool4 |
    ValueSubMultiByte4 |
    ValueSubMultiUshort4 |
    ValueSubMultiUint4 |
    ValueSubMultiUlong4 |
    ValueSubMultiSbyte4 |
    ValueSubMultiShort4 |
    ValueSubMultiInt4 |
    ValueSubMultiLong4 |
    ValueSubMultiFloat4 |
    ValueSubMultiDouble4 |
    ValueSubMultiFloat_2x2 |
    ValueSubMultiDouble_2x2 |
    ValueSubMultiFloat_3x3 |
    ValueSubMultiDouble_3x3 |
    ValueSubMultiFloat_4x4 |
    ValueSubMultiDouble_4x4 |
    ValueSubMultiFloatQ |
    ValueSubMultiDoubleQ |
    ValueSubMultiDateTime |
    ValueSubMultiTimeSpan |
    ValueSubMultiColor |
    ValueSubMultiColorX |
    ValueSubMultiShadowCastMode |
    ValueSubMultiLightType |
    ValueSubMultiSessionAccessLevel |
    ValueSubMultiKey |
    ValueSubMultiHttpStatusCode |
    ValueSubMultiHeadOutputDevice |
    ValueSubMultiReflectionProbeClear |
    ValueSubMultiReflectionProbeType |
    ValueSubMultiReflectionProbeTimeSlicingMode |
    ValueSubMultiCameraClearMode |
    ValueSubMultiCameraPositioningMode |
    ValueSubMultiCameraProjection |
    ValueSubMultiZWrite |
    ValueSubMultiZTest |
    ValueSubMultiBlend |
    ValueSubMultiBlendMode |
    ValueSubMultiCulling |
    ValueSubMultiBodyNode |
    ValueSubMultiChirality |
    ValueSubMultiDummyEnum
)