"""Generated component: ValueDec.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueDecBase(GeneratedComponent):
    """Base class for ValueDec<T> variants."""

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
class ValueDecBool(ValueDecBase):
    """ValueDec<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueDecByte(ValueDecBase):
    """ValueDec<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueDecUshort(ValueDecBase):
    """ValueDec<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueDecUint(ValueDecBase):
    """ValueDec<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueDecUlong(ValueDecBase):
    """ValueDec<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueDecSbyte(ValueDecBase):
    """ValueDec<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueDecShort(ValueDecBase):
    """ValueDec<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueDecInt(ValueDecBase):
    """ValueDec<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueDecLong(ValueDecBase):
    """ValueDec<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueDecFloat(ValueDecBase):
    """ValueDec<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueDecDouble(ValueDecBase):
    """ValueDec<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueDecDecimal(ValueDecBase):
    """ValueDec<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueDecChar(ValueDecBase):
    """ValueDec<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueDecString(ValueDecBase):
    """ValueDec<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueDecUri(ValueDecBase):
    """ValueDec<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueDecBool2(ValueDecBase):
    """ValueDec<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueDecByte2(ValueDecBase):
    """ValueDec<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueDecUshort2(ValueDecBase):
    """ValueDec<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueDecUint2(ValueDecBase):
    """ValueDec<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueDecUlong2(ValueDecBase):
    """ValueDec<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueDecSbyte2(ValueDecBase):
    """ValueDec<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueDecShort2(ValueDecBase):
    """ValueDec<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueDecInt2(ValueDecBase):
    """ValueDec<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueDecLong2(ValueDecBase):
    """ValueDec<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueDecFloat2(ValueDecBase):
    """ValueDec<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueDecDouble2(ValueDecBase):
    """ValueDec<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueDecBool3(ValueDecBase):
    """ValueDec<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueDecByte3(ValueDecBase):
    """ValueDec<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueDecUshort3(ValueDecBase):
    """ValueDec<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueDecUint3(ValueDecBase):
    """ValueDec<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueDecUlong3(ValueDecBase):
    """ValueDec<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueDecSbyte3(ValueDecBase):
    """ValueDec<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueDecShort3(ValueDecBase):
    """ValueDec<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueDecInt3(ValueDecBase):
    """ValueDec<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueDecLong3(ValueDecBase):
    """ValueDec<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueDecFloat3(ValueDecBase):
    """ValueDec<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueDecDouble3(ValueDecBase):
    """ValueDec<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueDecBool4(ValueDecBase):
    """ValueDec<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueDecByte4(ValueDecBase):
    """ValueDec<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueDecUshort4(ValueDecBase):
    """ValueDec<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueDecUint4(ValueDecBase):
    """ValueDec<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueDecUlong4(ValueDecBase):
    """ValueDec<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueDecSbyte4(ValueDecBase):
    """ValueDec<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueDecShort4(ValueDecBase):
    """ValueDec<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueDecInt4(ValueDecBase):
    """ValueDec<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueDecLong4(ValueDecBase):
    """ValueDec<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueDecFloat4(ValueDecBase):
    """ValueDec<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueDecDouble4(ValueDecBase):
    """ValueDec<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueDecFloat_2x2(ValueDecBase):
    """ValueDec<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueDecDouble_2x2(ValueDecBase):
    """ValueDec<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueDecFloat_3x3(ValueDecBase):
    """ValueDec<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueDecDouble_3x3(ValueDecBase):
    """ValueDec<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueDecFloat_4x4(ValueDecBase):
    """ValueDec<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueDecDouble_4x4(ValueDecBase):
    """ValueDec<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueDecFloatQ(ValueDecBase):
    """ValueDec<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueDecDoubleQ(ValueDecBase):
    """ValueDec<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueDecDateTime(ValueDecBase):
    """ValueDec<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueDecTimeSpan(ValueDecBase):
    """ValueDec<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueDecColor(ValueDecBase):
    """ValueDec<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueDecColorX(ValueDecBase):
    """ValueDec<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueDecShadowCastMode(ValueDecBase):
    """ValueDec<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueDecLightType(ValueDecBase):
    """ValueDec<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueDecSessionAccessLevel(ValueDecBase):
    """ValueDec<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueDecKey(ValueDecBase):
    """ValueDec<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueDecHttpStatusCode(ValueDecBase):
    """ValueDec<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueDecHeadOutputDevice(ValueDecBase):
    """ValueDec<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueDecReflectionProbeClear(ValueDecBase):
    """ValueDec<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueDecReflectionProbeType(ValueDecBase):
    """ValueDec<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueDecReflectionProbeTimeSlicingMode(ValueDecBase):
    """ValueDec<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueDecCameraClearMode(ValueDecBase):
    """ValueDec<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueDecCameraPositioningMode(ValueDecBase):
    """ValueDec<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueDecCameraProjection(ValueDecBase):
    """ValueDec<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueDecZWrite(ValueDecBase):
    """ValueDec<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueDecZTest(ValueDecBase):
    """ValueDec<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueDecBlend(ValueDecBase):
    """ValueDec<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueDecBlendMode(ValueDecBase):
    """ValueDec<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueDecCulling(ValueDecBase):
    """ValueDec<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueDecBodyNode(ValueDecBase):
    """ValueDec<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueDecChirality(ValueDecBase):
    """ValueDec<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueDecDummyEnum(ValueDecBase):
    """ValueDec<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueDec<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueDec variant
ValueDec = (
    ValueDecBool |
    ValueDecByte |
    ValueDecUshort |
    ValueDecUint |
    ValueDecUlong |
    ValueDecSbyte |
    ValueDecShort |
    ValueDecInt |
    ValueDecLong |
    ValueDecFloat |
    ValueDecDouble |
    ValueDecDecimal |
    ValueDecChar |
    ValueDecString |
    ValueDecUri |
    ValueDecBool2 |
    ValueDecByte2 |
    ValueDecUshort2 |
    ValueDecUint2 |
    ValueDecUlong2 |
    ValueDecSbyte2 |
    ValueDecShort2 |
    ValueDecInt2 |
    ValueDecLong2 |
    ValueDecFloat2 |
    ValueDecDouble2 |
    ValueDecBool3 |
    ValueDecByte3 |
    ValueDecUshort3 |
    ValueDecUint3 |
    ValueDecUlong3 |
    ValueDecSbyte3 |
    ValueDecShort3 |
    ValueDecInt3 |
    ValueDecLong3 |
    ValueDecFloat3 |
    ValueDecDouble3 |
    ValueDecBool4 |
    ValueDecByte4 |
    ValueDecUshort4 |
    ValueDecUint4 |
    ValueDecUlong4 |
    ValueDecSbyte4 |
    ValueDecShort4 |
    ValueDecInt4 |
    ValueDecLong4 |
    ValueDecFloat4 |
    ValueDecDouble4 |
    ValueDecFloat_2x2 |
    ValueDecDouble_2x2 |
    ValueDecFloat_3x3 |
    ValueDecDouble_3x3 |
    ValueDecFloat_4x4 |
    ValueDecDouble_4x4 |
    ValueDecFloatQ |
    ValueDecDoubleQ |
    ValueDecDateTime |
    ValueDecTimeSpan |
    ValueDecColor |
    ValueDecColorX |
    ValueDecShadowCastMode |
    ValueDecLightType |
    ValueDecSessionAccessLevel |
    ValueDecKey |
    ValueDecHttpStatusCode |
    ValueDecHeadOutputDevice |
    ValueDecReflectionProbeClear |
    ValueDecReflectionProbeType |
    ValueDecReflectionProbeTimeSlicingMode |
    ValueDecCameraClearMode |
    ValueDecCameraPositioningMode |
    ValueDecCameraProjection |
    ValueDecZWrite |
    ValueDecZTest |
    ValueDecBlend |
    ValueDecBlendMode |
    ValueDecCulling |
    ValueDecBodyNode |
    ValueDecChirality |
    ValueDecDummyEnum
)