"""Generated component: ValueCube.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueCubeBase(GeneratedComponent):
    """Base class for ValueCube<T> variants."""

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
class ValueCubeBool(ValueCubeBase):
    """ValueCube<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueCubeByte(ValueCubeBase):
    """ValueCube<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueCubeUshort(ValueCubeBase):
    """ValueCube<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueCubeUint(ValueCubeBase):
    """ValueCube<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueCubeUlong(ValueCubeBase):
    """ValueCube<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueCubeSbyte(ValueCubeBase):
    """ValueCube<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueCubeShort(ValueCubeBase):
    """ValueCube<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueCubeInt(ValueCubeBase):
    """ValueCube<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueCubeLong(ValueCubeBase):
    """ValueCube<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueCubeFloat(ValueCubeBase):
    """ValueCube<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueCubeDouble(ValueCubeBase):
    """ValueCube<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueCubeDecimal(ValueCubeBase):
    """ValueCube<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueCubeChar(ValueCubeBase):
    """ValueCube<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueCubeString(ValueCubeBase):
    """ValueCube<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueCubeUri(ValueCubeBase):
    """ValueCube<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueCubeBool2(ValueCubeBase):
    """ValueCube<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueCubeByte2(ValueCubeBase):
    """ValueCube<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueCubeUshort2(ValueCubeBase):
    """ValueCube<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueCubeUint2(ValueCubeBase):
    """ValueCube<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueCubeUlong2(ValueCubeBase):
    """ValueCube<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueCubeSbyte2(ValueCubeBase):
    """ValueCube<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueCubeShort2(ValueCubeBase):
    """ValueCube<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueCubeInt2(ValueCubeBase):
    """ValueCube<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueCubeLong2(ValueCubeBase):
    """ValueCube<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueCubeFloat2(ValueCubeBase):
    """ValueCube<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueCubeDouble2(ValueCubeBase):
    """ValueCube<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueCubeBool3(ValueCubeBase):
    """ValueCube<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueCubeByte3(ValueCubeBase):
    """ValueCube<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueCubeUshort3(ValueCubeBase):
    """ValueCube<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueCubeUint3(ValueCubeBase):
    """ValueCube<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueCubeUlong3(ValueCubeBase):
    """ValueCube<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueCubeSbyte3(ValueCubeBase):
    """ValueCube<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueCubeShort3(ValueCubeBase):
    """ValueCube<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueCubeInt3(ValueCubeBase):
    """ValueCube<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueCubeLong3(ValueCubeBase):
    """ValueCube<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueCubeFloat3(ValueCubeBase):
    """ValueCube<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueCubeDouble3(ValueCubeBase):
    """ValueCube<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueCubeBool4(ValueCubeBase):
    """ValueCube<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueCubeByte4(ValueCubeBase):
    """ValueCube<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueCubeUshort4(ValueCubeBase):
    """ValueCube<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueCubeUint4(ValueCubeBase):
    """ValueCube<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueCubeUlong4(ValueCubeBase):
    """ValueCube<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueCubeSbyte4(ValueCubeBase):
    """ValueCube<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueCubeShort4(ValueCubeBase):
    """ValueCube<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueCubeInt4(ValueCubeBase):
    """ValueCube<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueCubeLong4(ValueCubeBase):
    """ValueCube<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueCubeFloat4(ValueCubeBase):
    """ValueCube<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueCubeDouble4(ValueCubeBase):
    """ValueCube<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueCubeFloat_2x2(ValueCubeBase):
    """ValueCube<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueCubeDouble_2x2(ValueCubeBase):
    """ValueCube<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueCubeFloat_3x3(ValueCubeBase):
    """ValueCube<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueCubeDouble_3x3(ValueCubeBase):
    """ValueCube<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueCubeFloat_4x4(ValueCubeBase):
    """ValueCube<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueCubeDouble_4x4(ValueCubeBase):
    """ValueCube<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueCubeFloatQ(ValueCubeBase):
    """ValueCube<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueCubeDoubleQ(ValueCubeBase):
    """ValueCube<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueCubeDateTime(ValueCubeBase):
    """ValueCube<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueCubeTimeSpan(ValueCubeBase):
    """ValueCube<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueCubeColor(ValueCubeBase):
    """ValueCube<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueCubeColorX(ValueCubeBase):
    """ValueCube<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueCubeShadowCastMode(ValueCubeBase):
    """ValueCube<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueCubeLightType(ValueCubeBase):
    """ValueCube<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueCubeSessionAccessLevel(ValueCubeBase):
    """ValueCube<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueCubeKey(ValueCubeBase):
    """ValueCube<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueCubeHttpStatusCode(ValueCubeBase):
    """ValueCube<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueCubeHeadOutputDevice(ValueCubeBase):
    """ValueCube<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueCubeReflectionProbeClear(ValueCubeBase):
    """ValueCube<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueCubeReflectionProbeType(ValueCubeBase):
    """ValueCube<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueCubeReflectionProbeTimeSlicingMode(ValueCubeBase):
    """ValueCube<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueCubeCameraClearMode(ValueCubeBase):
    """ValueCube<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueCubeCameraPositioningMode(ValueCubeBase):
    """ValueCube<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueCubeCameraProjection(ValueCubeBase):
    """ValueCube<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueCubeZWrite(ValueCubeBase):
    """ValueCube<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueCubeZTest(ValueCubeBase):
    """ValueCube<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueCubeBlend(ValueCubeBase):
    """ValueCube<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueCubeBlendMode(ValueCubeBase):
    """ValueCube<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueCubeCulling(ValueCubeBase):
    """ValueCube<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueCubeBodyNode(ValueCubeBase):
    """ValueCube<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueCubeChirality(ValueCubeBase):
    """ValueCube<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueCubeDummyEnum(ValueCubeBase):
    """ValueCube<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueCube<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueCube variant
ValueCube = (
    ValueCubeBool |
    ValueCubeByte |
    ValueCubeUshort |
    ValueCubeUint |
    ValueCubeUlong |
    ValueCubeSbyte |
    ValueCubeShort |
    ValueCubeInt |
    ValueCubeLong |
    ValueCubeFloat |
    ValueCubeDouble |
    ValueCubeDecimal |
    ValueCubeChar |
    ValueCubeString |
    ValueCubeUri |
    ValueCubeBool2 |
    ValueCubeByte2 |
    ValueCubeUshort2 |
    ValueCubeUint2 |
    ValueCubeUlong2 |
    ValueCubeSbyte2 |
    ValueCubeShort2 |
    ValueCubeInt2 |
    ValueCubeLong2 |
    ValueCubeFloat2 |
    ValueCubeDouble2 |
    ValueCubeBool3 |
    ValueCubeByte3 |
    ValueCubeUshort3 |
    ValueCubeUint3 |
    ValueCubeUlong3 |
    ValueCubeSbyte3 |
    ValueCubeShort3 |
    ValueCubeInt3 |
    ValueCubeLong3 |
    ValueCubeFloat3 |
    ValueCubeDouble3 |
    ValueCubeBool4 |
    ValueCubeByte4 |
    ValueCubeUshort4 |
    ValueCubeUint4 |
    ValueCubeUlong4 |
    ValueCubeSbyte4 |
    ValueCubeShort4 |
    ValueCubeInt4 |
    ValueCubeLong4 |
    ValueCubeFloat4 |
    ValueCubeDouble4 |
    ValueCubeFloat_2x2 |
    ValueCubeDouble_2x2 |
    ValueCubeFloat_3x3 |
    ValueCubeDouble_3x3 |
    ValueCubeFloat_4x4 |
    ValueCubeDouble_4x4 |
    ValueCubeFloatQ |
    ValueCubeDoubleQ |
    ValueCubeDateTime |
    ValueCubeTimeSpan |
    ValueCubeColor |
    ValueCubeColorX |
    ValueCubeShadowCastMode |
    ValueCubeLightType |
    ValueCubeSessionAccessLevel |
    ValueCubeKey |
    ValueCubeHttpStatusCode |
    ValueCubeHeadOutputDevice |
    ValueCubeReflectionProbeClear |
    ValueCubeReflectionProbeType |
    ValueCubeReflectionProbeTimeSlicingMode |
    ValueCubeCameraClearMode |
    ValueCubeCameraPositioningMode |
    ValueCubeCameraProjection |
    ValueCubeZWrite |
    ValueCubeZTest |
    ValueCubeBlend |
    ValueCubeBlendMode |
    ValueCubeCulling |
    ValueCubeBodyNode |
    ValueCubeChirality |
    ValueCubeDummyEnum
)