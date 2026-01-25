"""Generated component: ValueNegate.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueNegateBase(GeneratedComponent):
    """Base class for ValueNegate<T> variants."""

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
class ValueNegateBool(ValueNegateBase):
    """ValueNegate<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueNegateByte(ValueNegateBase):
    """ValueNegate<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueNegateUshort(ValueNegateBase):
    """ValueNegate<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueNegateUint(ValueNegateBase):
    """ValueNegate<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueNegateUlong(ValueNegateBase):
    """ValueNegate<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueNegateSbyte(ValueNegateBase):
    """ValueNegate<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueNegateShort(ValueNegateBase):
    """ValueNegate<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueNegateInt(ValueNegateBase):
    """ValueNegate<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueNegateLong(ValueNegateBase):
    """ValueNegate<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueNegateFloat(ValueNegateBase):
    """ValueNegate<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueNegateDouble(ValueNegateBase):
    """ValueNegate<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueNegateDecimal(ValueNegateBase):
    """ValueNegate<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueNegateChar(ValueNegateBase):
    """ValueNegate<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueNegateString(ValueNegateBase):
    """ValueNegate<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueNegateUri(ValueNegateBase):
    """ValueNegate<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueNegateBool2(ValueNegateBase):
    """ValueNegate<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueNegateByte2(ValueNegateBase):
    """ValueNegate<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueNegateUshort2(ValueNegateBase):
    """ValueNegate<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueNegateUint2(ValueNegateBase):
    """ValueNegate<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueNegateUlong2(ValueNegateBase):
    """ValueNegate<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueNegateSbyte2(ValueNegateBase):
    """ValueNegate<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueNegateShort2(ValueNegateBase):
    """ValueNegate<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueNegateInt2(ValueNegateBase):
    """ValueNegate<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueNegateLong2(ValueNegateBase):
    """ValueNegate<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueNegateFloat2(ValueNegateBase):
    """ValueNegate<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueNegateDouble2(ValueNegateBase):
    """ValueNegate<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueNegateBool3(ValueNegateBase):
    """ValueNegate<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueNegateByte3(ValueNegateBase):
    """ValueNegate<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueNegateUshort3(ValueNegateBase):
    """ValueNegate<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueNegateUint3(ValueNegateBase):
    """ValueNegate<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueNegateUlong3(ValueNegateBase):
    """ValueNegate<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueNegateSbyte3(ValueNegateBase):
    """ValueNegate<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueNegateShort3(ValueNegateBase):
    """ValueNegate<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueNegateInt3(ValueNegateBase):
    """ValueNegate<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueNegateLong3(ValueNegateBase):
    """ValueNegate<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueNegateFloat3(ValueNegateBase):
    """ValueNegate<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueNegateDouble3(ValueNegateBase):
    """ValueNegate<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueNegateBool4(ValueNegateBase):
    """ValueNegate<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueNegateByte4(ValueNegateBase):
    """ValueNegate<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueNegateUshort4(ValueNegateBase):
    """ValueNegate<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueNegateUint4(ValueNegateBase):
    """ValueNegate<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueNegateUlong4(ValueNegateBase):
    """ValueNegate<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueNegateSbyte4(ValueNegateBase):
    """ValueNegate<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueNegateShort4(ValueNegateBase):
    """ValueNegate<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueNegateInt4(ValueNegateBase):
    """ValueNegate<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueNegateLong4(ValueNegateBase):
    """ValueNegate<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueNegateFloat4(ValueNegateBase):
    """ValueNegate<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueNegateDouble4(ValueNegateBase):
    """ValueNegate<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueNegateFloat_2x2(ValueNegateBase):
    """ValueNegate<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueNegateDouble_2x2(ValueNegateBase):
    """ValueNegate<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueNegateFloat_3x3(ValueNegateBase):
    """ValueNegate<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueNegateDouble_3x3(ValueNegateBase):
    """ValueNegate<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueNegateFloat_4x4(ValueNegateBase):
    """ValueNegate<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueNegateDouble_4x4(ValueNegateBase):
    """ValueNegate<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueNegateFloatQ(ValueNegateBase):
    """ValueNegate<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueNegateDoubleQ(ValueNegateBase):
    """ValueNegate<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueNegateDateTime(ValueNegateBase):
    """ValueNegate<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueNegateTimeSpan(ValueNegateBase):
    """ValueNegate<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueNegateColor(ValueNegateBase):
    """ValueNegate<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueNegateColorX(ValueNegateBase):
    """ValueNegate<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueNegateShadowCastMode(ValueNegateBase):
    """ValueNegate<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueNegateLightType(ValueNegateBase):
    """ValueNegate<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueNegateSessionAccessLevel(ValueNegateBase):
    """ValueNegate<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueNegateKey(ValueNegateBase):
    """ValueNegate<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueNegateHttpStatusCode(ValueNegateBase):
    """ValueNegate<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueNegateHeadOutputDevice(ValueNegateBase):
    """ValueNegate<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueNegateReflectionProbeClear(ValueNegateBase):
    """ValueNegate<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueNegateReflectionProbeType(ValueNegateBase):
    """ValueNegate<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueNegateReflectionProbeTimeSlicingMode(ValueNegateBase):
    """ValueNegate<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueNegateCameraClearMode(ValueNegateBase):
    """ValueNegate<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueNegateCameraPositioningMode(ValueNegateBase):
    """ValueNegate<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueNegateCameraProjection(ValueNegateBase):
    """ValueNegate<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueNegateZWrite(ValueNegateBase):
    """ValueNegate<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueNegateZTest(ValueNegateBase):
    """ValueNegate<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueNegateBlend(ValueNegateBase):
    """ValueNegate<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueNegateBlendMode(ValueNegateBase):
    """ValueNegate<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueNegateCulling(ValueNegateBase):
    """ValueNegate<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueNegateBodyNode(ValueNegateBase):
    """ValueNegate<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueNegateChirality(ValueNegateBase):
    """ValueNegate<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueNegateDummyEnum(ValueNegateBase):
    """ValueNegate<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueNegate<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueNegate variant
ValueNegate = (
    ValueNegateBool |
    ValueNegateByte |
    ValueNegateUshort |
    ValueNegateUint |
    ValueNegateUlong |
    ValueNegateSbyte |
    ValueNegateShort |
    ValueNegateInt |
    ValueNegateLong |
    ValueNegateFloat |
    ValueNegateDouble |
    ValueNegateDecimal |
    ValueNegateChar |
    ValueNegateString |
    ValueNegateUri |
    ValueNegateBool2 |
    ValueNegateByte2 |
    ValueNegateUshort2 |
    ValueNegateUint2 |
    ValueNegateUlong2 |
    ValueNegateSbyte2 |
    ValueNegateShort2 |
    ValueNegateInt2 |
    ValueNegateLong2 |
    ValueNegateFloat2 |
    ValueNegateDouble2 |
    ValueNegateBool3 |
    ValueNegateByte3 |
    ValueNegateUshort3 |
    ValueNegateUint3 |
    ValueNegateUlong3 |
    ValueNegateSbyte3 |
    ValueNegateShort3 |
    ValueNegateInt3 |
    ValueNegateLong3 |
    ValueNegateFloat3 |
    ValueNegateDouble3 |
    ValueNegateBool4 |
    ValueNegateByte4 |
    ValueNegateUshort4 |
    ValueNegateUint4 |
    ValueNegateUlong4 |
    ValueNegateSbyte4 |
    ValueNegateShort4 |
    ValueNegateInt4 |
    ValueNegateLong4 |
    ValueNegateFloat4 |
    ValueNegateDouble4 |
    ValueNegateFloat_2x2 |
    ValueNegateDouble_2x2 |
    ValueNegateFloat_3x3 |
    ValueNegateDouble_3x3 |
    ValueNegateFloat_4x4 |
    ValueNegateDouble_4x4 |
    ValueNegateFloatQ |
    ValueNegateDoubleQ |
    ValueNegateDateTime |
    ValueNegateTimeSpan |
    ValueNegateColor |
    ValueNegateColorX |
    ValueNegateShadowCastMode |
    ValueNegateLightType |
    ValueNegateSessionAccessLevel |
    ValueNegateKey |
    ValueNegateHttpStatusCode |
    ValueNegateHeadOutputDevice |
    ValueNegateReflectionProbeClear |
    ValueNegateReflectionProbeType |
    ValueNegateReflectionProbeTimeSlicingMode |
    ValueNegateCameraClearMode |
    ValueNegateCameraPositioningMode |
    ValueNegateCameraProjection |
    ValueNegateZWrite |
    ValueNegateZTest |
    ValueNegateBlend |
    ValueNegateBlendMode |
    ValueNegateCulling |
    ValueNegateBodyNode |
    ValueNegateChirality |
    ValueNegateDummyEnum
)