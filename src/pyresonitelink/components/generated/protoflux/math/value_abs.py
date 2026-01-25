"""Generated component: ValueAbs.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueAbsBase(GeneratedComponent):
    """Base class for ValueAbs<T> variants."""

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
class ValueAbsBool(ValueAbsBase):
    """ValueAbs<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueAbsByte(ValueAbsBase):
    """ValueAbs<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueAbsUshort(ValueAbsBase):
    """ValueAbs<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueAbsUint(ValueAbsBase):
    """ValueAbs<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueAbsUlong(ValueAbsBase):
    """ValueAbs<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueAbsSbyte(ValueAbsBase):
    """ValueAbs<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueAbsShort(ValueAbsBase):
    """ValueAbs<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueAbsInt(ValueAbsBase):
    """ValueAbs<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueAbsLong(ValueAbsBase):
    """ValueAbs<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueAbsFloat(ValueAbsBase):
    """ValueAbs<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueAbsDouble(ValueAbsBase):
    """ValueAbs<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueAbsDecimal(ValueAbsBase):
    """ValueAbs<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueAbsChar(ValueAbsBase):
    """ValueAbs<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueAbsString(ValueAbsBase):
    """ValueAbs<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueAbsUri(ValueAbsBase):
    """ValueAbs<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueAbsBool2(ValueAbsBase):
    """ValueAbs<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueAbsByte2(ValueAbsBase):
    """ValueAbs<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueAbsUshort2(ValueAbsBase):
    """ValueAbs<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueAbsUint2(ValueAbsBase):
    """ValueAbs<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueAbsUlong2(ValueAbsBase):
    """ValueAbs<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueAbsSbyte2(ValueAbsBase):
    """ValueAbs<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueAbsShort2(ValueAbsBase):
    """ValueAbs<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueAbsInt2(ValueAbsBase):
    """ValueAbs<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueAbsLong2(ValueAbsBase):
    """ValueAbs<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueAbsFloat2(ValueAbsBase):
    """ValueAbs<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueAbsDouble2(ValueAbsBase):
    """ValueAbs<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueAbsBool3(ValueAbsBase):
    """ValueAbs<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueAbsByte3(ValueAbsBase):
    """ValueAbs<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueAbsUshort3(ValueAbsBase):
    """ValueAbs<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueAbsUint3(ValueAbsBase):
    """ValueAbs<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueAbsUlong3(ValueAbsBase):
    """ValueAbs<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueAbsSbyte3(ValueAbsBase):
    """ValueAbs<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueAbsShort3(ValueAbsBase):
    """ValueAbs<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueAbsInt3(ValueAbsBase):
    """ValueAbs<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueAbsLong3(ValueAbsBase):
    """ValueAbs<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueAbsFloat3(ValueAbsBase):
    """ValueAbs<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueAbsDouble3(ValueAbsBase):
    """ValueAbs<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueAbsBool4(ValueAbsBase):
    """ValueAbs<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueAbsByte4(ValueAbsBase):
    """ValueAbs<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueAbsUshort4(ValueAbsBase):
    """ValueAbs<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueAbsUint4(ValueAbsBase):
    """ValueAbs<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueAbsUlong4(ValueAbsBase):
    """ValueAbs<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueAbsSbyte4(ValueAbsBase):
    """ValueAbs<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueAbsShort4(ValueAbsBase):
    """ValueAbs<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueAbsInt4(ValueAbsBase):
    """ValueAbs<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueAbsLong4(ValueAbsBase):
    """ValueAbs<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueAbsFloat4(ValueAbsBase):
    """ValueAbs<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueAbsDouble4(ValueAbsBase):
    """ValueAbs<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueAbsFloat_2x2(ValueAbsBase):
    """ValueAbs<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueAbsDouble_2x2(ValueAbsBase):
    """ValueAbs<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueAbsFloat_3x3(ValueAbsBase):
    """ValueAbs<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueAbsDouble_3x3(ValueAbsBase):
    """ValueAbs<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueAbsFloat_4x4(ValueAbsBase):
    """ValueAbs<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueAbsDouble_4x4(ValueAbsBase):
    """ValueAbs<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueAbsFloatQ(ValueAbsBase):
    """ValueAbs<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueAbsDoubleQ(ValueAbsBase):
    """ValueAbs<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueAbsDateTime(ValueAbsBase):
    """ValueAbs<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueAbsTimeSpan(ValueAbsBase):
    """ValueAbs<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueAbsColor(ValueAbsBase):
    """ValueAbs<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueAbsColorX(ValueAbsBase):
    """ValueAbs<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueAbsShadowCastMode(ValueAbsBase):
    """ValueAbs<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueAbsLightType(ValueAbsBase):
    """ValueAbs<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueAbsSessionAccessLevel(ValueAbsBase):
    """ValueAbs<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueAbsKey(ValueAbsBase):
    """ValueAbs<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueAbsHttpStatusCode(ValueAbsBase):
    """ValueAbs<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueAbsHeadOutputDevice(ValueAbsBase):
    """ValueAbs<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueAbsReflectionProbeClear(ValueAbsBase):
    """ValueAbs<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueAbsReflectionProbeType(ValueAbsBase):
    """ValueAbs<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueAbsReflectionProbeTimeSlicingMode(ValueAbsBase):
    """ValueAbs<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueAbsCameraClearMode(ValueAbsBase):
    """ValueAbs<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueAbsCameraPositioningMode(ValueAbsBase):
    """ValueAbs<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueAbsCameraProjection(ValueAbsBase):
    """ValueAbs<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueAbsZWrite(ValueAbsBase):
    """ValueAbs<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueAbsZTest(ValueAbsBase):
    """ValueAbs<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueAbsBlend(ValueAbsBase):
    """ValueAbs<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueAbsBlendMode(ValueAbsBase):
    """ValueAbs<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueAbsCulling(ValueAbsBase):
    """ValueAbs<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueAbsBodyNode(ValueAbsBase):
    """ValueAbs<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueAbsChirality(ValueAbsBase):
    """ValueAbs<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueAbsDummyEnum(ValueAbsBase):
    """ValueAbs<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueAbs<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "n": "N",
    }

    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueAbs variant
ValueAbs = (
    ValueAbsBool |
    ValueAbsByte |
    ValueAbsUshort |
    ValueAbsUint |
    ValueAbsUlong |
    ValueAbsSbyte |
    ValueAbsShort |
    ValueAbsInt |
    ValueAbsLong |
    ValueAbsFloat |
    ValueAbsDouble |
    ValueAbsDecimal |
    ValueAbsChar |
    ValueAbsString |
    ValueAbsUri |
    ValueAbsBool2 |
    ValueAbsByte2 |
    ValueAbsUshort2 |
    ValueAbsUint2 |
    ValueAbsUlong2 |
    ValueAbsSbyte2 |
    ValueAbsShort2 |
    ValueAbsInt2 |
    ValueAbsLong2 |
    ValueAbsFloat2 |
    ValueAbsDouble2 |
    ValueAbsBool3 |
    ValueAbsByte3 |
    ValueAbsUshort3 |
    ValueAbsUint3 |
    ValueAbsUlong3 |
    ValueAbsSbyte3 |
    ValueAbsShort3 |
    ValueAbsInt3 |
    ValueAbsLong3 |
    ValueAbsFloat3 |
    ValueAbsDouble3 |
    ValueAbsBool4 |
    ValueAbsByte4 |
    ValueAbsUshort4 |
    ValueAbsUint4 |
    ValueAbsUlong4 |
    ValueAbsSbyte4 |
    ValueAbsShort4 |
    ValueAbsInt4 |
    ValueAbsLong4 |
    ValueAbsFloat4 |
    ValueAbsDouble4 |
    ValueAbsFloat_2x2 |
    ValueAbsDouble_2x2 |
    ValueAbsFloat_3x3 |
    ValueAbsDouble_3x3 |
    ValueAbsFloat_4x4 |
    ValueAbsDouble_4x4 |
    ValueAbsFloatQ |
    ValueAbsDoubleQ |
    ValueAbsDateTime |
    ValueAbsTimeSpan |
    ValueAbsColor |
    ValueAbsColorX |
    ValueAbsShadowCastMode |
    ValueAbsLightType |
    ValueAbsSessionAccessLevel |
    ValueAbsKey |
    ValueAbsHttpStatusCode |
    ValueAbsHeadOutputDevice |
    ValueAbsReflectionProbeClear |
    ValueAbsReflectionProbeType |
    ValueAbsReflectionProbeTimeSlicingMode |
    ValueAbsCameraClearMode |
    ValueAbsCameraPositioningMode |
    ValueAbsCameraProjection |
    ValueAbsZWrite |
    ValueAbsZTest |
    ValueAbsBlend |
    ValueAbsBlendMode |
    ValueAbsCulling |
    ValueAbsBodyNode |
    ValueAbsChirality |
    ValueAbsDummyEnum
)