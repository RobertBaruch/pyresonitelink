"""Generated component: ValueSquare.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueSquareBase(GeneratedComponent):
    """Base class for ValueSquare<T> variants."""

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
class ValueSquareBool(ValueSquareBase):
    """ValueSquare<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueSquareByte(ValueSquareBase):
    """ValueSquare<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueSquareUshort(ValueSquareBase):
    """ValueSquare<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueSquareUint(ValueSquareBase):
    """ValueSquare<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueSquareUlong(ValueSquareBase):
    """ValueSquare<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueSquareSbyte(ValueSquareBase):
    """ValueSquare<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueSquareShort(ValueSquareBase):
    """ValueSquare<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueSquareInt(ValueSquareBase):
    """ValueSquare<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueSquareLong(ValueSquareBase):
    """ValueSquare<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueSquareFloat(ValueSquareBase):
    """ValueSquare<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSquareDouble(ValueSquareBase):
    """ValueSquare<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueSquareDecimal(ValueSquareBase):
    """ValueSquare<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueSquareChar(ValueSquareBase):
    """ValueSquare<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueSquareString(ValueSquareBase):
    """ValueSquare<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueSquareUri(ValueSquareBase):
    """ValueSquare<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueSquareBool2(ValueSquareBase):
    """ValueSquare<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueSquareByte2(ValueSquareBase):
    """ValueSquare<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueSquareUshort2(ValueSquareBase):
    """ValueSquare<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueSquareUint2(ValueSquareBase):
    """ValueSquare<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueSquareUlong2(ValueSquareBase):
    """ValueSquare<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueSquareSbyte2(ValueSquareBase):
    """ValueSquare<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueSquareShort2(ValueSquareBase):
    """ValueSquare<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueSquareInt2(ValueSquareBase):
    """ValueSquare<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueSquareLong2(ValueSquareBase):
    """ValueSquare<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueSquareFloat2(ValueSquareBase):
    """ValueSquare<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueSquareDouble2(ValueSquareBase):
    """ValueSquare<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueSquareBool3(ValueSquareBase):
    """ValueSquare<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueSquareByte3(ValueSquareBase):
    """ValueSquare<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueSquareUshort3(ValueSquareBase):
    """ValueSquare<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueSquareUint3(ValueSquareBase):
    """ValueSquare<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueSquareUlong3(ValueSquareBase):
    """ValueSquare<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueSquareSbyte3(ValueSquareBase):
    """ValueSquare<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueSquareShort3(ValueSquareBase):
    """ValueSquare<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueSquareInt3(ValueSquareBase):
    """ValueSquare<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueSquareLong3(ValueSquareBase):
    """ValueSquare<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueSquareFloat3(ValueSquareBase):
    """ValueSquare<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueSquareDouble3(ValueSquareBase):
    """ValueSquare<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueSquareBool4(ValueSquareBase):
    """ValueSquare<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueSquareByte4(ValueSquareBase):
    """ValueSquare<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueSquareUshort4(ValueSquareBase):
    """ValueSquare<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueSquareUint4(ValueSquareBase):
    """ValueSquare<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueSquareUlong4(ValueSquareBase):
    """ValueSquare<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueSquareSbyte4(ValueSquareBase):
    """ValueSquare<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueSquareShort4(ValueSquareBase):
    """ValueSquare<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueSquareInt4(ValueSquareBase):
    """ValueSquare<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueSquareLong4(ValueSquareBase):
    """ValueSquare<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueSquareFloat4(ValueSquareBase):
    """ValueSquare<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueSquareDouble4(ValueSquareBase):
    """ValueSquare<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueSquareFloat_2x2(ValueSquareBase):
    """ValueSquare<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueSquareDouble_2x2(ValueSquareBase):
    """ValueSquare<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueSquareFloat_3x3(ValueSquareBase):
    """ValueSquare<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueSquareDouble_3x3(ValueSquareBase):
    """ValueSquare<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueSquareFloat_4x4(ValueSquareBase):
    """ValueSquare<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueSquareDouble_4x4(ValueSquareBase):
    """ValueSquare<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueSquareFloatQ(ValueSquareBase):
    """ValueSquare<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueSquareDoubleQ(ValueSquareBase):
    """ValueSquare<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueSquareDateTime(ValueSquareBase):
    """ValueSquare<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueSquareTimeSpan(ValueSquareBase):
    """ValueSquare<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueSquareColor(ValueSquareBase):
    """ValueSquare<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueSquareColorX(ValueSquareBase):
    """ValueSquare<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueSquareShadowCastMode(ValueSquareBase):
    """ValueSquare<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueSquareLightType(ValueSquareBase):
    """ValueSquare<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueSquareSessionAccessLevel(ValueSquareBase):
    """ValueSquare<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueSquareKey(ValueSquareBase):
    """ValueSquare<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueSquareHttpStatusCode(ValueSquareBase):
    """ValueSquare<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueSquareHeadOutputDevice(ValueSquareBase):
    """ValueSquare<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueSquareReflectionProbeClear(ValueSquareBase):
    """ValueSquare<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueSquareReflectionProbeType(ValueSquareBase):
    """ValueSquare<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueSquareReflectionProbeTimeSlicingMode(ValueSquareBase):
    """ValueSquare<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueSquareCameraClearMode(ValueSquareBase):
    """ValueSquare<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueSquareCameraPositioningMode(ValueSquareBase):
    """ValueSquare<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueSquareCameraProjection(ValueSquareBase):
    """ValueSquare<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueSquareZWrite(ValueSquareBase):
    """ValueSquare<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueSquareZTest(ValueSquareBase):
    """ValueSquare<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueSquareBlend(ValueSquareBase):
    """ValueSquare<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueSquareBlendMode(ValueSquareBase):
    """ValueSquare<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueSquareCulling(ValueSquareBase):
    """ValueSquare<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueSquareBodyNode(ValueSquareBase):
    """ValueSquare<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueSquareChirality(ValueSquareBase):
    """ValueSquare<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueSquareDummyEnum(ValueSquareBase):
    """ValueSquare<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueSquare<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueSquare variant
ValueSquare = (
    ValueSquareBool |
    ValueSquareByte |
    ValueSquareUshort |
    ValueSquareUint |
    ValueSquareUlong |
    ValueSquareSbyte |
    ValueSquareShort |
    ValueSquareInt |
    ValueSquareLong |
    ValueSquareFloat |
    ValueSquareDouble |
    ValueSquareDecimal |
    ValueSquareChar |
    ValueSquareString |
    ValueSquareUri |
    ValueSquareBool2 |
    ValueSquareByte2 |
    ValueSquareUshort2 |
    ValueSquareUint2 |
    ValueSquareUlong2 |
    ValueSquareSbyte2 |
    ValueSquareShort2 |
    ValueSquareInt2 |
    ValueSquareLong2 |
    ValueSquareFloat2 |
    ValueSquareDouble2 |
    ValueSquareBool3 |
    ValueSquareByte3 |
    ValueSquareUshort3 |
    ValueSquareUint3 |
    ValueSquareUlong3 |
    ValueSquareSbyte3 |
    ValueSquareShort3 |
    ValueSquareInt3 |
    ValueSquareLong3 |
    ValueSquareFloat3 |
    ValueSquareDouble3 |
    ValueSquareBool4 |
    ValueSquareByte4 |
    ValueSquareUshort4 |
    ValueSquareUint4 |
    ValueSquareUlong4 |
    ValueSquareSbyte4 |
    ValueSquareShort4 |
    ValueSquareInt4 |
    ValueSquareLong4 |
    ValueSquareFloat4 |
    ValueSquareDouble4 |
    ValueSquareFloat_2x2 |
    ValueSquareDouble_2x2 |
    ValueSquareFloat_3x3 |
    ValueSquareDouble_3x3 |
    ValueSquareFloat_4x4 |
    ValueSquareDouble_4x4 |
    ValueSquareFloatQ |
    ValueSquareDoubleQ |
    ValueSquareDateTime |
    ValueSquareTimeSpan |
    ValueSquareColor |
    ValueSquareColorX |
    ValueSquareShadowCastMode |
    ValueSquareLightType |
    ValueSquareSessionAccessLevel |
    ValueSquareKey |
    ValueSquareHttpStatusCode |
    ValueSquareHeadOutputDevice |
    ValueSquareReflectionProbeClear |
    ValueSquareReflectionProbeType |
    ValueSquareReflectionProbeTimeSlicingMode |
    ValueSquareCameraClearMode |
    ValueSquareCameraPositioningMode |
    ValueSquareCameraProjection |
    ValueSquareZWrite |
    ValueSquareZTest |
    ValueSquareBlend |
    ValueSquareBlendMode |
    ValueSquareCulling |
    ValueSquareBodyNode |
    ValueSquareChirality |
    ValueSquareDummyEnum
)