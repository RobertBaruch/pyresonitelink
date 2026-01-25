"""Generated component: ValueDivMulti.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class ValueDivMultiBase(GeneratedComponent):
    """Base class for ValueDivMulti<T> variants."""

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
class ValueDivMultiBool(ValueDivMultiBase):
    """ValueDivMulti<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiByte(ValueDivMultiBase):
    """ValueDivMulti<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUshort(ValueDivMultiBase):
    """ValueDivMulti<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUint(ValueDivMultiBase):
    """ValueDivMulti<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUlong(ValueDivMultiBase):
    """ValueDivMulti<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiSbyte(ValueDivMultiBase):
    """ValueDivMulti<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiShort(ValueDivMultiBase):
    """ValueDivMulti<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiInt(ValueDivMultiBase):
    """ValueDivMulti<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiLong(ValueDivMultiBase):
    """ValueDivMulti<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat(ValueDivMultiBase):
    """ValueDivMulti<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble(ValueDivMultiBase):
    """ValueDivMulti<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDecimal(ValueDivMultiBase):
    """ValueDivMulti<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiChar(ValueDivMultiBase):
    """ValueDivMulti<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiString(ValueDivMultiBase):
    """ValueDivMulti<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUri(ValueDivMultiBase):
    """ValueDivMulti<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBool2(ValueDivMultiBase):
    """ValueDivMulti<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiByte2(ValueDivMultiBase):
    """ValueDivMulti<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUshort2(ValueDivMultiBase):
    """ValueDivMulti<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUint2(ValueDivMultiBase):
    """ValueDivMulti<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUlong2(ValueDivMultiBase):
    """ValueDivMulti<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiSbyte2(ValueDivMultiBase):
    """ValueDivMulti<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiShort2(ValueDivMultiBase):
    """ValueDivMulti<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiInt2(ValueDivMultiBase):
    """ValueDivMulti<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiLong2(ValueDivMultiBase):
    """ValueDivMulti<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat2(ValueDivMultiBase):
    """ValueDivMulti<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble2(ValueDivMultiBase):
    """ValueDivMulti<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBool3(ValueDivMultiBase):
    """ValueDivMulti<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiByte3(ValueDivMultiBase):
    """ValueDivMulti<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUshort3(ValueDivMultiBase):
    """ValueDivMulti<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUint3(ValueDivMultiBase):
    """ValueDivMulti<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUlong3(ValueDivMultiBase):
    """ValueDivMulti<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiSbyte3(ValueDivMultiBase):
    """ValueDivMulti<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiShort3(ValueDivMultiBase):
    """ValueDivMulti<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiInt3(ValueDivMultiBase):
    """ValueDivMulti<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiLong3(ValueDivMultiBase):
    """ValueDivMulti<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat3(ValueDivMultiBase):
    """ValueDivMulti<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble3(ValueDivMultiBase):
    """ValueDivMulti<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBool4(ValueDivMultiBase):
    """ValueDivMulti<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiByte4(ValueDivMultiBase):
    """ValueDivMulti<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUshort4(ValueDivMultiBase):
    """ValueDivMulti<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUint4(ValueDivMultiBase):
    """ValueDivMulti<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiUlong4(ValueDivMultiBase):
    """ValueDivMulti<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiSbyte4(ValueDivMultiBase):
    """ValueDivMulti<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiShort4(ValueDivMultiBase):
    """ValueDivMulti<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiInt4(ValueDivMultiBase):
    """ValueDivMulti<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiLong4(ValueDivMultiBase):
    """ValueDivMulti<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat4(ValueDivMultiBase):
    """ValueDivMulti<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble4(ValueDivMultiBase):
    """ValueDivMulti<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat_2x2(ValueDivMultiBase):
    """ValueDivMulti<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble_2x2(ValueDivMultiBase):
    """ValueDivMulti<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat_3x3(ValueDivMultiBase):
    """ValueDivMulti<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble_3x3(ValueDivMultiBase):
    """ValueDivMulti<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloat_4x4(ValueDivMultiBase):
    """ValueDivMulti<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDouble_4x4(ValueDivMultiBase):
    """ValueDivMulti<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiFloatQ(ValueDivMultiBase):
    """ValueDivMulti<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDoubleQ(ValueDivMultiBase):
    """ValueDivMulti<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDateTime(ValueDivMultiBase):
    """ValueDivMulti<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiTimeSpan(ValueDivMultiBase):
    """ValueDivMulti<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiColor(ValueDivMultiBase):
    """ValueDivMulti<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiColorX(ValueDivMultiBase):
    """ValueDivMulti<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiShadowCastMode(ValueDivMultiBase):
    """ValueDivMulti<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiLightType(ValueDivMultiBase):
    """ValueDivMulti<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiSessionAccessLevel(ValueDivMultiBase):
    """ValueDivMulti<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiKey(ValueDivMultiBase):
    """ValueDivMulti<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiHttpStatusCode(ValueDivMultiBase):
    """ValueDivMulti<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiHeadOutputDevice(ValueDivMultiBase):
    """ValueDivMulti<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiReflectionProbeClear(ValueDivMultiBase):
    """ValueDivMulti<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiReflectionProbeType(ValueDivMultiBase):
    """ValueDivMulti<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiReflectionProbeTimeSlicingMode(ValueDivMultiBase):
    """ValueDivMulti<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiCameraClearMode(ValueDivMultiBase):
    """ValueDivMulti<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiCameraPositioningMode(ValueDivMultiBase):
    """ValueDivMulti<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiCameraProjection(ValueDivMultiBase):
    """ValueDivMulti<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiZWrite(ValueDivMultiBase):
    """ValueDivMulti<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiZTest(ValueDivMultiBase):
    """ValueDivMulti<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBlend(ValueDivMultiBase):
    """ValueDivMulti<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBlendMode(ValueDivMultiBase):
    """ValueDivMulti<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiCulling(ValueDivMultiBase):
    """ValueDivMulti<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiBodyNode(ValueDivMultiBase):
    """ValueDivMulti<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiChirality(ValueDivMultiBase):
    """ValueDivMulti<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


@dataclass
class ValueDivMultiDummyEnum(ValueDivMultiBase):
    """ValueDivMulti<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDivMulti<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "inputs": "Inputs",
    }

    inputs: SyncList | None = None


# Type alias for any ValueDivMulti variant
ValueDivMulti = (
    ValueDivMultiBool |
    ValueDivMultiByte |
    ValueDivMultiUshort |
    ValueDivMultiUint |
    ValueDivMultiUlong |
    ValueDivMultiSbyte |
    ValueDivMultiShort |
    ValueDivMultiInt |
    ValueDivMultiLong |
    ValueDivMultiFloat |
    ValueDivMultiDouble |
    ValueDivMultiDecimal |
    ValueDivMultiChar |
    ValueDivMultiString |
    ValueDivMultiUri |
    ValueDivMultiBool2 |
    ValueDivMultiByte2 |
    ValueDivMultiUshort2 |
    ValueDivMultiUint2 |
    ValueDivMultiUlong2 |
    ValueDivMultiSbyte2 |
    ValueDivMultiShort2 |
    ValueDivMultiInt2 |
    ValueDivMultiLong2 |
    ValueDivMultiFloat2 |
    ValueDivMultiDouble2 |
    ValueDivMultiBool3 |
    ValueDivMultiByte3 |
    ValueDivMultiUshort3 |
    ValueDivMultiUint3 |
    ValueDivMultiUlong3 |
    ValueDivMultiSbyte3 |
    ValueDivMultiShort3 |
    ValueDivMultiInt3 |
    ValueDivMultiLong3 |
    ValueDivMultiFloat3 |
    ValueDivMultiDouble3 |
    ValueDivMultiBool4 |
    ValueDivMultiByte4 |
    ValueDivMultiUshort4 |
    ValueDivMultiUint4 |
    ValueDivMultiUlong4 |
    ValueDivMultiSbyte4 |
    ValueDivMultiShort4 |
    ValueDivMultiInt4 |
    ValueDivMultiLong4 |
    ValueDivMultiFloat4 |
    ValueDivMultiDouble4 |
    ValueDivMultiFloat_2x2 |
    ValueDivMultiDouble_2x2 |
    ValueDivMultiFloat_3x3 |
    ValueDivMultiDouble_3x3 |
    ValueDivMultiFloat_4x4 |
    ValueDivMultiDouble_4x4 |
    ValueDivMultiFloatQ |
    ValueDivMultiDoubleQ |
    ValueDivMultiDateTime |
    ValueDivMultiTimeSpan |
    ValueDivMultiColor |
    ValueDivMultiColorX |
    ValueDivMultiShadowCastMode |
    ValueDivMultiLightType |
    ValueDivMultiSessionAccessLevel |
    ValueDivMultiKey |
    ValueDivMultiHttpStatusCode |
    ValueDivMultiHeadOutputDevice |
    ValueDivMultiReflectionProbeClear |
    ValueDivMultiReflectionProbeType |
    ValueDivMultiReflectionProbeTimeSlicingMode |
    ValueDivMultiCameraClearMode |
    ValueDivMultiCameraPositioningMode |
    ValueDivMultiCameraProjection |
    ValueDivMultiZWrite |
    ValueDivMultiZTest |
    ValueDivMultiBlend |
    ValueDivMultiBlendMode |
    ValueDivMultiCulling |
    ValueDivMultiBodyNode |
    ValueDivMultiChirality |
    ValueDivMultiDummyEnum
)