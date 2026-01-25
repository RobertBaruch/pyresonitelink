"""Generated component: GenericValueDisplay.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class GenericValueDisplayBase(GeneratedComponent):
    """Base class for GenericValueDisplay<T> variants."""

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
class GenericValueDisplayBool(GenericValueDisplayBase):
    """GenericValueDisplay<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class GenericValueDisplayByte(GenericValueDisplayBase):
    """GenericValueDisplay<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class GenericValueDisplayUshort(GenericValueDisplayBase):
    """GenericValueDisplay<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class GenericValueDisplayUint(GenericValueDisplayBase):
    """GenericValueDisplay<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class GenericValueDisplayUlong(GenericValueDisplayBase):
    """GenericValueDisplay<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class GenericValueDisplaySbyte(GenericValueDisplayBase):
    """GenericValueDisplay<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class GenericValueDisplayShort(GenericValueDisplayBase):
    """GenericValueDisplay<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class GenericValueDisplayInt(GenericValueDisplayBase):
    """GenericValueDisplay<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class GenericValueDisplayLong(GenericValueDisplayBase):
    """GenericValueDisplay<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class GenericValueDisplayFloat(GenericValueDisplayBase):
    """GenericValueDisplay<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class GenericValueDisplayDouble(GenericValueDisplayBase):
    """GenericValueDisplay<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class GenericValueDisplayDecimal(GenericValueDisplayBase):
    """GenericValueDisplay<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class GenericValueDisplayChar(GenericValueDisplayBase):
    """GenericValueDisplay<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class GenericValueDisplayString(GenericValueDisplayBase):
    """GenericValueDisplay<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class GenericValueDisplayUri(GenericValueDisplayBase):
    """GenericValueDisplay<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class GenericValueDisplayBool2(GenericValueDisplayBase):
    """GenericValueDisplay<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class GenericValueDisplayByte2(GenericValueDisplayBase):
    """GenericValueDisplay<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class GenericValueDisplayUshort2(GenericValueDisplayBase):
    """GenericValueDisplay<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class GenericValueDisplayUint2(GenericValueDisplayBase):
    """GenericValueDisplay<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class GenericValueDisplayUlong2(GenericValueDisplayBase):
    """GenericValueDisplay<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class GenericValueDisplaySbyte2(GenericValueDisplayBase):
    """GenericValueDisplay<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class GenericValueDisplayShort2(GenericValueDisplayBase):
    """GenericValueDisplay<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class GenericValueDisplayInt2(GenericValueDisplayBase):
    """GenericValueDisplay<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class GenericValueDisplayLong2(GenericValueDisplayBase):
    """GenericValueDisplay<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class GenericValueDisplayFloat2(GenericValueDisplayBase):
    """GenericValueDisplay<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class GenericValueDisplayDouble2(GenericValueDisplayBase):
    """GenericValueDisplay<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class GenericValueDisplayBool3(GenericValueDisplayBase):
    """GenericValueDisplay<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class GenericValueDisplayByte3(GenericValueDisplayBase):
    """GenericValueDisplay<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class GenericValueDisplayUshort3(GenericValueDisplayBase):
    """GenericValueDisplay<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class GenericValueDisplayUint3(GenericValueDisplayBase):
    """GenericValueDisplay<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class GenericValueDisplayUlong3(GenericValueDisplayBase):
    """GenericValueDisplay<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class GenericValueDisplaySbyte3(GenericValueDisplayBase):
    """GenericValueDisplay<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class GenericValueDisplayShort3(GenericValueDisplayBase):
    """GenericValueDisplay<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class GenericValueDisplayInt3(GenericValueDisplayBase):
    """GenericValueDisplay<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class GenericValueDisplayLong3(GenericValueDisplayBase):
    """GenericValueDisplay<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class GenericValueDisplayFloat3(GenericValueDisplayBase):
    """GenericValueDisplay<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class GenericValueDisplayDouble3(GenericValueDisplayBase):
    """GenericValueDisplay<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class GenericValueDisplayBool4(GenericValueDisplayBase):
    """GenericValueDisplay<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class GenericValueDisplayByte4(GenericValueDisplayBase):
    """GenericValueDisplay<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class GenericValueDisplayUshort4(GenericValueDisplayBase):
    """GenericValueDisplay<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class GenericValueDisplayUint4(GenericValueDisplayBase):
    """GenericValueDisplay<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class GenericValueDisplayUlong4(GenericValueDisplayBase):
    """GenericValueDisplay<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class GenericValueDisplaySbyte4(GenericValueDisplayBase):
    """GenericValueDisplay<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class GenericValueDisplayShort4(GenericValueDisplayBase):
    """GenericValueDisplay<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class GenericValueDisplayInt4(GenericValueDisplayBase):
    """GenericValueDisplay<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class GenericValueDisplayLong4(GenericValueDisplayBase):
    """GenericValueDisplay<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class GenericValueDisplayFloat4(GenericValueDisplayBase):
    """GenericValueDisplay<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class GenericValueDisplayDouble4(GenericValueDisplayBase):
    """GenericValueDisplay<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class GenericValueDisplayFloat_2x2(GenericValueDisplayBase):
    """GenericValueDisplay<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class GenericValueDisplayDouble_2x2(GenericValueDisplayBase):
    """GenericValueDisplay<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class GenericValueDisplayFloat_3x3(GenericValueDisplayBase):
    """GenericValueDisplay<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class GenericValueDisplayDouble_3x3(GenericValueDisplayBase):
    """GenericValueDisplay<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class GenericValueDisplayFloat_4x4(GenericValueDisplayBase):
    """GenericValueDisplay<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class GenericValueDisplayDouble_4x4(GenericValueDisplayBase):
    """GenericValueDisplay<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class GenericValueDisplayFloatQ(GenericValueDisplayBase):
    """GenericValueDisplay<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class GenericValueDisplayDoubleQ(GenericValueDisplayBase):
    """GenericValueDisplay<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class GenericValueDisplayDateTime(GenericValueDisplayBase):
    """GenericValueDisplay<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class GenericValueDisplayTimeSpan(GenericValueDisplayBase):
    """GenericValueDisplay<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class GenericValueDisplayColor(GenericValueDisplayBase):
    """GenericValueDisplay<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class GenericValueDisplayColorX(GenericValueDisplayBase):
    """GenericValueDisplay<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class GenericValueDisplayShadowCastMode(GenericValueDisplayBase):
    """GenericValueDisplay<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class GenericValueDisplayLightType(GenericValueDisplayBase):
    """GenericValueDisplay<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class GenericValueDisplaySessionAccessLevel(GenericValueDisplayBase):
    """GenericValueDisplay<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class GenericValueDisplayKey(GenericValueDisplayBase):
    """GenericValueDisplay<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class GenericValueDisplayHttpStatusCode(GenericValueDisplayBase):
    """GenericValueDisplay<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class GenericValueDisplayHeadOutputDevice(GenericValueDisplayBase):
    """GenericValueDisplay<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class GenericValueDisplayReflectionProbeClear(GenericValueDisplayBase):
    """GenericValueDisplay<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class GenericValueDisplayReflectionProbeType(GenericValueDisplayBase):
    """GenericValueDisplay<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class GenericValueDisplayReflectionProbeTimeSlicingMode(GenericValueDisplayBase):
    """GenericValueDisplay<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class GenericValueDisplayCameraClearMode(GenericValueDisplayBase):
    """GenericValueDisplay<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class GenericValueDisplayCameraPositioningMode(GenericValueDisplayBase):
    """GenericValueDisplay<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class GenericValueDisplayCameraProjection(GenericValueDisplayBase):
    """GenericValueDisplay<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class GenericValueDisplayZWrite(GenericValueDisplayBase):
    """GenericValueDisplay<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class GenericValueDisplayZTest(GenericValueDisplayBase):
    """GenericValueDisplay<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class GenericValueDisplayBlend(GenericValueDisplayBase):
    """GenericValueDisplay<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class GenericValueDisplayBlendMode(GenericValueDisplayBase):
    """GenericValueDisplay<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class GenericValueDisplayCulling(GenericValueDisplayBase):
    """GenericValueDisplay<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class GenericValueDisplayBodyNode(GenericValueDisplayBase):
    """GenericValueDisplay<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class GenericValueDisplayChirality(GenericValueDisplayBase):
    """GenericValueDisplay<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class GenericValueDisplayDummyEnum(GenericValueDisplayBase):
    """GenericValueDisplay<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GenericValueDisplay<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any GenericValueDisplay variant
GenericValueDisplay = (
    GenericValueDisplayBool |
    GenericValueDisplayByte |
    GenericValueDisplayUshort |
    GenericValueDisplayUint |
    GenericValueDisplayUlong |
    GenericValueDisplaySbyte |
    GenericValueDisplayShort |
    GenericValueDisplayInt |
    GenericValueDisplayLong |
    GenericValueDisplayFloat |
    GenericValueDisplayDouble |
    GenericValueDisplayDecimal |
    GenericValueDisplayChar |
    GenericValueDisplayString |
    GenericValueDisplayUri |
    GenericValueDisplayBool2 |
    GenericValueDisplayByte2 |
    GenericValueDisplayUshort2 |
    GenericValueDisplayUint2 |
    GenericValueDisplayUlong2 |
    GenericValueDisplaySbyte2 |
    GenericValueDisplayShort2 |
    GenericValueDisplayInt2 |
    GenericValueDisplayLong2 |
    GenericValueDisplayFloat2 |
    GenericValueDisplayDouble2 |
    GenericValueDisplayBool3 |
    GenericValueDisplayByte3 |
    GenericValueDisplayUshort3 |
    GenericValueDisplayUint3 |
    GenericValueDisplayUlong3 |
    GenericValueDisplaySbyte3 |
    GenericValueDisplayShort3 |
    GenericValueDisplayInt3 |
    GenericValueDisplayLong3 |
    GenericValueDisplayFloat3 |
    GenericValueDisplayDouble3 |
    GenericValueDisplayBool4 |
    GenericValueDisplayByte4 |
    GenericValueDisplayUshort4 |
    GenericValueDisplayUint4 |
    GenericValueDisplayUlong4 |
    GenericValueDisplaySbyte4 |
    GenericValueDisplayShort4 |
    GenericValueDisplayInt4 |
    GenericValueDisplayLong4 |
    GenericValueDisplayFloat4 |
    GenericValueDisplayDouble4 |
    GenericValueDisplayFloat_2x2 |
    GenericValueDisplayDouble_2x2 |
    GenericValueDisplayFloat_3x3 |
    GenericValueDisplayDouble_3x3 |
    GenericValueDisplayFloat_4x4 |
    GenericValueDisplayDouble_4x4 |
    GenericValueDisplayFloatQ |
    GenericValueDisplayDoubleQ |
    GenericValueDisplayDateTime |
    GenericValueDisplayTimeSpan |
    GenericValueDisplayColor |
    GenericValueDisplayColorX |
    GenericValueDisplayShadowCastMode |
    GenericValueDisplayLightType |
    GenericValueDisplaySessionAccessLevel |
    GenericValueDisplayKey |
    GenericValueDisplayHttpStatusCode |
    GenericValueDisplayHeadOutputDevice |
    GenericValueDisplayReflectionProbeClear |
    GenericValueDisplayReflectionProbeType |
    GenericValueDisplayReflectionProbeTimeSlicingMode |
    GenericValueDisplayCameraClearMode |
    GenericValueDisplayCameraPositioningMode |
    GenericValueDisplayCameraProjection |
    GenericValueDisplayZWrite |
    GenericValueDisplayZTest |
    GenericValueDisplayBlend |
    GenericValueDisplayBlendMode |
    GenericValueDisplayCulling |
    GenericValueDisplayBodyNode |
    GenericValueDisplayChirality |
    GenericValueDisplayDummyEnum
)