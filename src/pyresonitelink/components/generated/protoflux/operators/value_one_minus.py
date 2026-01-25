"""Generated component: ValueOneMinus.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueOneMinusBase(GeneratedComponent):
    """Base class for ValueOneMinus<T> variants."""

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
class ValueOneMinusBool(ValueOneMinusBase):
    """ValueOneMinus<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueOneMinusByte(ValueOneMinusBase):
    """ValueOneMinus<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueOneMinusUshort(ValueOneMinusBase):
    """ValueOneMinus<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueOneMinusUint(ValueOneMinusBase):
    """ValueOneMinus<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueOneMinusUlong(ValueOneMinusBase):
    """ValueOneMinus<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueOneMinusSbyte(ValueOneMinusBase):
    """ValueOneMinus<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueOneMinusShort(ValueOneMinusBase):
    """ValueOneMinus<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueOneMinusInt(ValueOneMinusBase):
    """ValueOneMinus<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueOneMinusLong(ValueOneMinusBase):
    """ValueOneMinus<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueOneMinusFloat(ValueOneMinusBase):
    """ValueOneMinus<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueOneMinusDouble(ValueOneMinusBase):
    """ValueOneMinus<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueOneMinusDecimal(ValueOneMinusBase):
    """ValueOneMinus<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueOneMinusChar(ValueOneMinusBase):
    """ValueOneMinus<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueOneMinusString(ValueOneMinusBase):
    """ValueOneMinus<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueOneMinusUri(ValueOneMinusBase):
    """ValueOneMinus<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueOneMinusBool2(ValueOneMinusBase):
    """ValueOneMinus<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueOneMinusByte2(ValueOneMinusBase):
    """ValueOneMinus<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueOneMinusUshort2(ValueOneMinusBase):
    """ValueOneMinus<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueOneMinusUint2(ValueOneMinusBase):
    """ValueOneMinus<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueOneMinusUlong2(ValueOneMinusBase):
    """ValueOneMinus<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueOneMinusSbyte2(ValueOneMinusBase):
    """ValueOneMinus<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueOneMinusShort2(ValueOneMinusBase):
    """ValueOneMinus<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueOneMinusInt2(ValueOneMinusBase):
    """ValueOneMinus<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueOneMinusLong2(ValueOneMinusBase):
    """ValueOneMinus<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueOneMinusFloat2(ValueOneMinusBase):
    """ValueOneMinus<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueOneMinusDouble2(ValueOneMinusBase):
    """ValueOneMinus<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueOneMinusBool3(ValueOneMinusBase):
    """ValueOneMinus<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueOneMinusByte3(ValueOneMinusBase):
    """ValueOneMinus<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueOneMinusUshort3(ValueOneMinusBase):
    """ValueOneMinus<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueOneMinusUint3(ValueOneMinusBase):
    """ValueOneMinus<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueOneMinusUlong3(ValueOneMinusBase):
    """ValueOneMinus<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueOneMinusSbyte3(ValueOneMinusBase):
    """ValueOneMinus<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueOneMinusShort3(ValueOneMinusBase):
    """ValueOneMinus<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueOneMinusInt3(ValueOneMinusBase):
    """ValueOneMinus<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueOneMinusLong3(ValueOneMinusBase):
    """ValueOneMinus<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueOneMinusFloat3(ValueOneMinusBase):
    """ValueOneMinus<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueOneMinusDouble3(ValueOneMinusBase):
    """ValueOneMinus<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueOneMinusBool4(ValueOneMinusBase):
    """ValueOneMinus<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueOneMinusByte4(ValueOneMinusBase):
    """ValueOneMinus<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueOneMinusUshort4(ValueOneMinusBase):
    """ValueOneMinus<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueOneMinusUint4(ValueOneMinusBase):
    """ValueOneMinus<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueOneMinusUlong4(ValueOneMinusBase):
    """ValueOneMinus<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueOneMinusSbyte4(ValueOneMinusBase):
    """ValueOneMinus<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueOneMinusShort4(ValueOneMinusBase):
    """ValueOneMinus<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueOneMinusInt4(ValueOneMinusBase):
    """ValueOneMinus<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueOneMinusLong4(ValueOneMinusBase):
    """ValueOneMinus<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueOneMinusFloat4(ValueOneMinusBase):
    """ValueOneMinus<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueOneMinusDouble4(ValueOneMinusBase):
    """ValueOneMinus<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueOneMinusFloat_2x2(ValueOneMinusBase):
    """ValueOneMinus<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueOneMinusDouble_2x2(ValueOneMinusBase):
    """ValueOneMinus<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueOneMinusFloat_3x3(ValueOneMinusBase):
    """ValueOneMinus<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueOneMinusDouble_3x3(ValueOneMinusBase):
    """ValueOneMinus<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueOneMinusFloat_4x4(ValueOneMinusBase):
    """ValueOneMinus<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueOneMinusDouble_4x4(ValueOneMinusBase):
    """ValueOneMinus<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueOneMinusFloatQ(ValueOneMinusBase):
    """ValueOneMinus<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueOneMinusDoubleQ(ValueOneMinusBase):
    """ValueOneMinus<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueOneMinusDateTime(ValueOneMinusBase):
    """ValueOneMinus<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueOneMinusTimeSpan(ValueOneMinusBase):
    """ValueOneMinus<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueOneMinusColor(ValueOneMinusBase):
    """ValueOneMinus<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueOneMinusColorX(ValueOneMinusBase):
    """ValueOneMinus<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueOneMinusShadowCastMode(ValueOneMinusBase):
    """ValueOneMinus<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueOneMinusLightType(ValueOneMinusBase):
    """ValueOneMinus<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueOneMinusSessionAccessLevel(ValueOneMinusBase):
    """ValueOneMinus<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueOneMinusKey(ValueOneMinusBase):
    """ValueOneMinus<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueOneMinusHttpStatusCode(ValueOneMinusBase):
    """ValueOneMinus<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueOneMinusHeadOutputDevice(ValueOneMinusBase):
    """ValueOneMinus<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueOneMinusReflectionProbeClear(ValueOneMinusBase):
    """ValueOneMinus<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueOneMinusReflectionProbeType(ValueOneMinusBase):
    """ValueOneMinus<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueOneMinusReflectionProbeTimeSlicingMode(ValueOneMinusBase):
    """ValueOneMinus<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueOneMinusCameraClearMode(ValueOneMinusBase):
    """ValueOneMinus<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueOneMinusCameraPositioningMode(ValueOneMinusBase):
    """ValueOneMinus<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueOneMinusCameraProjection(ValueOneMinusBase):
    """ValueOneMinus<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueOneMinusZWrite(ValueOneMinusBase):
    """ValueOneMinus<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueOneMinusZTest(ValueOneMinusBase):
    """ValueOneMinus<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueOneMinusBlend(ValueOneMinusBase):
    """ValueOneMinus<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueOneMinusBlendMode(ValueOneMinusBase):
    """ValueOneMinus<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueOneMinusCulling(ValueOneMinusBase):
    """ValueOneMinus<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueOneMinusBodyNode(ValueOneMinusBase):
    """ValueOneMinus<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueOneMinusChirality(ValueOneMinusBase):
    """ValueOneMinus<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueOneMinusDummyEnum(ValueOneMinusBase):
    """ValueOneMinus<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "x": "X",
    }

    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueOneMinus variant
ValueOneMinus = (
    ValueOneMinusBool |
    ValueOneMinusByte |
    ValueOneMinusUshort |
    ValueOneMinusUint |
    ValueOneMinusUlong |
    ValueOneMinusSbyte |
    ValueOneMinusShort |
    ValueOneMinusInt |
    ValueOneMinusLong |
    ValueOneMinusFloat |
    ValueOneMinusDouble |
    ValueOneMinusDecimal |
    ValueOneMinusChar |
    ValueOneMinusString |
    ValueOneMinusUri |
    ValueOneMinusBool2 |
    ValueOneMinusByte2 |
    ValueOneMinusUshort2 |
    ValueOneMinusUint2 |
    ValueOneMinusUlong2 |
    ValueOneMinusSbyte2 |
    ValueOneMinusShort2 |
    ValueOneMinusInt2 |
    ValueOneMinusLong2 |
    ValueOneMinusFloat2 |
    ValueOneMinusDouble2 |
    ValueOneMinusBool3 |
    ValueOneMinusByte3 |
    ValueOneMinusUshort3 |
    ValueOneMinusUint3 |
    ValueOneMinusUlong3 |
    ValueOneMinusSbyte3 |
    ValueOneMinusShort3 |
    ValueOneMinusInt3 |
    ValueOneMinusLong3 |
    ValueOneMinusFloat3 |
    ValueOneMinusDouble3 |
    ValueOneMinusBool4 |
    ValueOneMinusByte4 |
    ValueOneMinusUshort4 |
    ValueOneMinusUint4 |
    ValueOneMinusUlong4 |
    ValueOneMinusSbyte4 |
    ValueOneMinusShort4 |
    ValueOneMinusInt4 |
    ValueOneMinusLong4 |
    ValueOneMinusFloat4 |
    ValueOneMinusDouble4 |
    ValueOneMinusFloat_2x2 |
    ValueOneMinusDouble_2x2 |
    ValueOneMinusFloat_3x3 |
    ValueOneMinusDouble_3x3 |
    ValueOneMinusFloat_4x4 |
    ValueOneMinusDouble_4x4 |
    ValueOneMinusFloatQ |
    ValueOneMinusDoubleQ |
    ValueOneMinusDateTime |
    ValueOneMinusTimeSpan |
    ValueOneMinusColor |
    ValueOneMinusColorX |
    ValueOneMinusShadowCastMode |
    ValueOneMinusLightType |
    ValueOneMinusSessionAccessLevel |
    ValueOneMinusKey |
    ValueOneMinusHttpStatusCode |
    ValueOneMinusHeadOutputDevice |
    ValueOneMinusReflectionProbeClear |
    ValueOneMinusReflectionProbeType |
    ValueOneMinusReflectionProbeTimeSlicingMode |
    ValueOneMinusCameraClearMode |
    ValueOneMinusCameraPositioningMode |
    ValueOneMinusCameraProjection |
    ValueOneMinusZWrite |
    ValueOneMinusZTest |
    ValueOneMinusBlend |
    ValueOneMinusBlendMode |
    ValueOneMinusCulling |
    ValueOneMinusBodyNode |
    ValueOneMinusChirality |
    ValueOneMinusDummyEnum
)