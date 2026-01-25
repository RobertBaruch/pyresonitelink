"""Generated component: ValueRelay.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueRelayBase(GeneratedComponent):
    """Base class for ValueRelay<T> variants."""

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
class ValueRelayBool(ValueRelayBase):
    """ValueRelay<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueRelayByte(ValueRelayBase):
    """ValueRelay<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueRelayUshort(ValueRelayBase):
    """ValueRelay<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueRelayUint(ValueRelayBase):
    """ValueRelay<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueRelayUlong(ValueRelayBase):
    """ValueRelay<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueRelaySbyte(ValueRelayBase):
    """ValueRelay<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueRelayShort(ValueRelayBase):
    """ValueRelay<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueRelayInt(ValueRelayBase):
    """ValueRelay<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueRelayLong(ValueRelayBase):
    """ValueRelay<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueRelayFloat(ValueRelayBase):
    """ValueRelay<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueRelayDouble(ValueRelayBase):
    """ValueRelay<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueRelayDecimal(ValueRelayBase):
    """ValueRelay<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueRelayChar(ValueRelayBase):
    """ValueRelay<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueRelayString(ValueRelayBase):
    """ValueRelay<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueRelayUri(ValueRelayBase):
    """ValueRelay<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueRelayBool2(ValueRelayBase):
    """ValueRelay<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueRelayByte2(ValueRelayBase):
    """ValueRelay<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueRelayUshort2(ValueRelayBase):
    """ValueRelay<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueRelayUint2(ValueRelayBase):
    """ValueRelay<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueRelayUlong2(ValueRelayBase):
    """ValueRelay<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueRelaySbyte2(ValueRelayBase):
    """ValueRelay<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueRelayShort2(ValueRelayBase):
    """ValueRelay<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueRelayInt2(ValueRelayBase):
    """ValueRelay<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueRelayLong2(ValueRelayBase):
    """ValueRelay<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueRelayFloat2(ValueRelayBase):
    """ValueRelay<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueRelayDouble2(ValueRelayBase):
    """ValueRelay<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueRelayBool3(ValueRelayBase):
    """ValueRelay<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueRelayByte3(ValueRelayBase):
    """ValueRelay<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueRelayUshort3(ValueRelayBase):
    """ValueRelay<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueRelayUint3(ValueRelayBase):
    """ValueRelay<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueRelayUlong3(ValueRelayBase):
    """ValueRelay<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueRelaySbyte3(ValueRelayBase):
    """ValueRelay<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueRelayShort3(ValueRelayBase):
    """ValueRelay<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueRelayInt3(ValueRelayBase):
    """ValueRelay<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueRelayLong3(ValueRelayBase):
    """ValueRelay<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueRelayFloat3(ValueRelayBase):
    """ValueRelay<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueRelayDouble3(ValueRelayBase):
    """ValueRelay<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueRelayBool4(ValueRelayBase):
    """ValueRelay<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueRelayByte4(ValueRelayBase):
    """ValueRelay<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueRelayUshort4(ValueRelayBase):
    """ValueRelay<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueRelayUint4(ValueRelayBase):
    """ValueRelay<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueRelayUlong4(ValueRelayBase):
    """ValueRelay<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueRelaySbyte4(ValueRelayBase):
    """ValueRelay<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueRelayShort4(ValueRelayBase):
    """ValueRelay<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueRelayInt4(ValueRelayBase):
    """ValueRelay<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueRelayLong4(ValueRelayBase):
    """ValueRelay<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueRelayFloat4(ValueRelayBase):
    """ValueRelay<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueRelayDouble4(ValueRelayBase):
    """ValueRelay<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueRelayFloat_2x2(ValueRelayBase):
    """ValueRelay<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueRelayDouble_2x2(ValueRelayBase):
    """ValueRelay<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueRelayFloat_3x3(ValueRelayBase):
    """ValueRelay<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueRelayDouble_3x3(ValueRelayBase):
    """ValueRelay<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueRelayFloat_4x4(ValueRelayBase):
    """ValueRelay<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueRelayDouble_4x4(ValueRelayBase):
    """ValueRelay<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueRelayFloatQ(ValueRelayBase):
    """ValueRelay<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueRelayDoubleQ(ValueRelayBase):
    """ValueRelay<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueRelayDateTime(ValueRelayBase):
    """ValueRelay<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueRelayTimeSpan(ValueRelayBase):
    """ValueRelay<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueRelayColor(ValueRelayBase):
    """ValueRelay<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueRelayColorX(ValueRelayBase):
    """ValueRelay<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueRelayShadowCastMode(ValueRelayBase):
    """ValueRelay<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueRelayLightType(ValueRelayBase):
    """ValueRelay<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueRelaySessionAccessLevel(ValueRelayBase):
    """ValueRelay<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueRelayKey(ValueRelayBase):
    """ValueRelay<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueRelayHttpStatusCode(ValueRelayBase):
    """ValueRelay<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueRelayHeadOutputDevice(ValueRelayBase):
    """ValueRelay<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueRelayReflectionProbeClear(ValueRelayBase):
    """ValueRelay<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueRelayReflectionProbeType(ValueRelayBase):
    """ValueRelay<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueRelayReflectionProbeTimeSlicingMode(ValueRelayBase):
    """ValueRelay<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueRelayCameraClearMode(ValueRelayBase):
    """ValueRelay<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueRelayCameraPositioningMode(ValueRelayBase):
    """ValueRelay<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueRelayCameraProjection(ValueRelayBase):
    """ValueRelay<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueRelayZWrite(ValueRelayBase):
    """ValueRelay<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueRelayZTest(ValueRelayBase):
    """ValueRelay<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueRelayBlend(ValueRelayBase):
    """ValueRelay<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueRelayBlendMode(ValueRelayBase):
    """ValueRelay<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueRelayCulling(ValueRelayBase):
    """ValueRelay<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueRelayBodyNode(ValueRelayBase):
    """ValueRelay<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueRelayChirality(ValueRelayBase):
    """ValueRelay<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueRelayDummyEnum(ValueRelayBase):
    """ValueRelay<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueRelay<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueRelay variant
ValueRelay = (
    ValueRelayBool |
    ValueRelayByte |
    ValueRelayUshort |
    ValueRelayUint |
    ValueRelayUlong |
    ValueRelaySbyte |
    ValueRelayShort |
    ValueRelayInt |
    ValueRelayLong |
    ValueRelayFloat |
    ValueRelayDouble |
    ValueRelayDecimal |
    ValueRelayChar |
    ValueRelayString |
    ValueRelayUri |
    ValueRelayBool2 |
    ValueRelayByte2 |
    ValueRelayUshort2 |
    ValueRelayUint2 |
    ValueRelayUlong2 |
    ValueRelaySbyte2 |
    ValueRelayShort2 |
    ValueRelayInt2 |
    ValueRelayLong2 |
    ValueRelayFloat2 |
    ValueRelayDouble2 |
    ValueRelayBool3 |
    ValueRelayByte3 |
    ValueRelayUshort3 |
    ValueRelayUint3 |
    ValueRelayUlong3 |
    ValueRelaySbyte3 |
    ValueRelayShort3 |
    ValueRelayInt3 |
    ValueRelayLong3 |
    ValueRelayFloat3 |
    ValueRelayDouble3 |
    ValueRelayBool4 |
    ValueRelayByte4 |
    ValueRelayUshort4 |
    ValueRelayUint4 |
    ValueRelayUlong4 |
    ValueRelaySbyte4 |
    ValueRelayShort4 |
    ValueRelayInt4 |
    ValueRelayLong4 |
    ValueRelayFloat4 |
    ValueRelayDouble4 |
    ValueRelayFloat_2x2 |
    ValueRelayDouble_2x2 |
    ValueRelayFloat_3x3 |
    ValueRelayDouble_3x3 |
    ValueRelayFloat_4x4 |
    ValueRelayDouble_4x4 |
    ValueRelayFloatQ |
    ValueRelayDoubleQ |
    ValueRelayDateTime |
    ValueRelayTimeSpan |
    ValueRelayColor |
    ValueRelayColorX |
    ValueRelayShadowCastMode |
    ValueRelayLightType |
    ValueRelaySessionAccessLevel |
    ValueRelayKey |
    ValueRelayHttpStatusCode |
    ValueRelayHeadOutputDevice |
    ValueRelayReflectionProbeClear |
    ValueRelayReflectionProbeType |
    ValueRelayReflectionProbeTimeSlicingMode |
    ValueRelayCameraClearMode |
    ValueRelayCameraPositioningMode |
    ValueRelayCameraProjection |
    ValueRelayZWrite |
    ValueRelayZTest |
    ValueRelayBlend |
    ValueRelayBlendMode |
    ValueRelayCulling |
    ValueRelayBodyNode |
    ValueRelayChirality |
    ValueRelayDummyEnum
)