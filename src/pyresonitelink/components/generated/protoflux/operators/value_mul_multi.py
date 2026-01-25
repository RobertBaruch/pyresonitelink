"""Generated component: ValueMulMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueMulMultiBase(GeneratedComponent):
    """Base class for ValueMulMulti<T> variants."""

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
class ValueMulMultiBool(ValueMulMultiBase):
    """ValueMulMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiByte(ValueMulMultiBase):
    """ValueMulMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUshort(ValueMulMultiBase):
    """ValueMulMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUint(ValueMulMultiBase):
    """ValueMulMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUlong(ValueMulMultiBase):
    """ValueMulMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiSbyte(ValueMulMultiBase):
    """ValueMulMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiShort(ValueMulMultiBase):
    """ValueMulMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiInt(ValueMulMultiBase):
    """ValueMulMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiLong(ValueMulMultiBase):
    """ValueMulMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat(ValueMulMultiBase):
    """ValueMulMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble(ValueMulMultiBase):
    """ValueMulMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDecimal(ValueMulMultiBase):
    """ValueMulMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiChar(ValueMulMultiBase):
    """ValueMulMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiString(ValueMulMultiBase):
    """ValueMulMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUri(ValueMulMultiBase):
    """ValueMulMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBool2(ValueMulMultiBase):
    """ValueMulMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiByte2(ValueMulMultiBase):
    """ValueMulMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUshort2(ValueMulMultiBase):
    """ValueMulMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUint2(ValueMulMultiBase):
    """ValueMulMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUlong2(ValueMulMultiBase):
    """ValueMulMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiSbyte2(ValueMulMultiBase):
    """ValueMulMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiShort2(ValueMulMultiBase):
    """ValueMulMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiInt2(ValueMulMultiBase):
    """ValueMulMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiLong2(ValueMulMultiBase):
    """ValueMulMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat2(ValueMulMultiBase):
    """ValueMulMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble2(ValueMulMultiBase):
    """ValueMulMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBool3(ValueMulMultiBase):
    """ValueMulMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiByte3(ValueMulMultiBase):
    """ValueMulMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUshort3(ValueMulMultiBase):
    """ValueMulMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUint3(ValueMulMultiBase):
    """ValueMulMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUlong3(ValueMulMultiBase):
    """ValueMulMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiSbyte3(ValueMulMultiBase):
    """ValueMulMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiShort3(ValueMulMultiBase):
    """ValueMulMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiInt3(ValueMulMultiBase):
    """ValueMulMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiLong3(ValueMulMultiBase):
    """ValueMulMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat3(ValueMulMultiBase):
    """ValueMulMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble3(ValueMulMultiBase):
    """ValueMulMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBool4(ValueMulMultiBase):
    """ValueMulMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiByte4(ValueMulMultiBase):
    """ValueMulMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUshort4(ValueMulMultiBase):
    """ValueMulMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUint4(ValueMulMultiBase):
    """ValueMulMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiUlong4(ValueMulMultiBase):
    """ValueMulMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiSbyte4(ValueMulMultiBase):
    """ValueMulMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiShort4(ValueMulMultiBase):
    """ValueMulMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiInt4(ValueMulMultiBase):
    """ValueMulMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiLong4(ValueMulMultiBase):
    """ValueMulMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat4(ValueMulMultiBase):
    """ValueMulMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble4(ValueMulMultiBase):
    """ValueMulMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat_2x2(ValueMulMultiBase):
    """ValueMulMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble_2x2(ValueMulMultiBase):
    """ValueMulMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat_3x3(ValueMulMultiBase):
    """ValueMulMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble_3x3(ValueMulMultiBase):
    """ValueMulMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloat_4x4(ValueMulMultiBase):
    """ValueMulMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDouble_4x4(ValueMulMultiBase):
    """ValueMulMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiFloatQ(ValueMulMultiBase):
    """ValueMulMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDoubleQ(ValueMulMultiBase):
    """ValueMulMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDateTime(ValueMulMultiBase):
    """ValueMulMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiTimeSpan(ValueMulMultiBase):
    """ValueMulMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiColor(ValueMulMultiBase):
    """ValueMulMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiColorX(ValueMulMultiBase):
    """ValueMulMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiShadowCastMode(ValueMulMultiBase):
    """ValueMulMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiLightType(ValueMulMultiBase):
    """ValueMulMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiSessionAccessLevel(ValueMulMultiBase):
    """ValueMulMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiKey(ValueMulMultiBase):
    """ValueMulMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiHttpStatusCode(ValueMulMultiBase):
    """ValueMulMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiHeadOutputDevice(ValueMulMultiBase):
    """ValueMulMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiReflectionProbeClear(ValueMulMultiBase):
    """ValueMulMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiReflectionProbeType(ValueMulMultiBase):
    """ValueMulMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiReflectionProbeTimeSlicingMode(ValueMulMultiBase):
    """ValueMulMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiCameraClearMode(ValueMulMultiBase):
    """ValueMulMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiCameraPositioningMode(ValueMulMultiBase):
    """ValueMulMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiCameraProjection(ValueMulMultiBase):
    """ValueMulMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiZWrite(ValueMulMultiBase):
    """ValueMulMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiZTest(ValueMulMultiBase):
    """ValueMulMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBlend(ValueMulMultiBase):
    """ValueMulMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBlendMode(ValueMulMultiBase):
    """ValueMulMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiCulling(ValueMulMultiBase):
    """ValueMulMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiBodyNode(ValueMulMultiBase):
    """ValueMulMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiChirality(ValueMulMultiBase):
    """ValueMulMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueMulMultiDummyEnum(ValueMulMultiBase):
    """ValueMulMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueMulMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


# Type alias for any ValueMulMulti variant
ValueMulMulti = (
    ValueMulMultiBool |
    ValueMulMultiByte |
    ValueMulMultiUshort |
    ValueMulMultiUint |
    ValueMulMultiUlong |
    ValueMulMultiSbyte |
    ValueMulMultiShort |
    ValueMulMultiInt |
    ValueMulMultiLong |
    ValueMulMultiFloat |
    ValueMulMultiDouble |
    ValueMulMultiDecimal |
    ValueMulMultiChar |
    ValueMulMultiString |
    ValueMulMultiUri |
    ValueMulMultiBool2 |
    ValueMulMultiByte2 |
    ValueMulMultiUshort2 |
    ValueMulMultiUint2 |
    ValueMulMultiUlong2 |
    ValueMulMultiSbyte2 |
    ValueMulMultiShort2 |
    ValueMulMultiInt2 |
    ValueMulMultiLong2 |
    ValueMulMultiFloat2 |
    ValueMulMultiDouble2 |
    ValueMulMultiBool3 |
    ValueMulMultiByte3 |
    ValueMulMultiUshort3 |
    ValueMulMultiUint3 |
    ValueMulMultiUlong3 |
    ValueMulMultiSbyte3 |
    ValueMulMultiShort3 |
    ValueMulMultiInt3 |
    ValueMulMultiLong3 |
    ValueMulMultiFloat3 |
    ValueMulMultiDouble3 |
    ValueMulMultiBool4 |
    ValueMulMultiByte4 |
    ValueMulMultiUshort4 |
    ValueMulMultiUint4 |
    ValueMulMultiUlong4 |
    ValueMulMultiSbyte4 |
    ValueMulMultiShort4 |
    ValueMulMultiInt4 |
    ValueMulMultiLong4 |
    ValueMulMultiFloat4 |
    ValueMulMultiDouble4 |
    ValueMulMultiFloat_2x2 |
    ValueMulMultiDouble_2x2 |
    ValueMulMultiFloat_3x3 |
    ValueMulMultiDouble_3x3 |
    ValueMulMultiFloat_4x4 |
    ValueMulMultiDouble_4x4 |
    ValueMulMultiFloatQ |
    ValueMulMultiDoubleQ |
    ValueMulMultiDateTime |
    ValueMulMultiTimeSpan |
    ValueMulMultiColor |
    ValueMulMultiColorX |
    ValueMulMultiShadowCastMode |
    ValueMulMultiLightType |
    ValueMulMultiSessionAccessLevel |
    ValueMulMultiKey |
    ValueMulMultiHttpStatusCode |
    ValueMulMultiHeadOutputDevice |
    ValueMulMultiReflectionProbeClear |
    ValueMulMultiReflectionProbeType |
    ValueMulMultiReflectionProbeTimeSlicingMode |
    ValueMulMultiCameraClearMode |
    ValueMulMultiCameraPositioningMode |
    ValueMulMultiCameraProjection |
    ValueMulMultiZWrite |
    ValueMulMultiZTest |
    ValueMulMultiBlend |
    ValueMulMultiBlendMode |
    ValueMulMultiCulling |
    ValueMulMultiBodyNode |
    ValueMulMultiChirality |
    ValueMulMultiDummyEnum
)