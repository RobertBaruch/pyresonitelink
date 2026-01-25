"""Generated component: ValueDisplay.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueDisplayBase(GeneratedComponent):
    """Base class for ValueDisplay<T> variants."""

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
class ValueDisplayBool(ValueDisplayBase):
    """ValueDisplay<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueDisplayByte(ValueDisplayBase):
    """ValueDisplay<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueDisplayUshort(ValueDisplayBase):
    """ValueDisplay<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueDisplayUint(ValueDisplayBase):
    """ValueDisplay<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueDisplayUlong(ValueDisplayBase):
    """ValueDisplay<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueDisplaySbyte(ValueDisplayBase):
    """ValueDisplay<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueDisplayShort(ValueDisplayBase):
    """ValueDisplay<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueDisplayInt(ValueDisplayBase):
    """ValueDisplay<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueDisplayLong(ValueDisplayBase):
    """ValueDisplay<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueDisplayFloat(ValueDisplayBase):
    """ValueDisplay<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueDisplayDouble(ValueDisplayBase):
    """ValueDisplay<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueDisplayDecimal(ValueDisplayBase):
    """ValueDisplay<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueDisplayChar(ValueDisplayBase):
    """ValueDisplay<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueDisplayString(ValueDisplayBase):
    """ValueDisplay<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueDisplayUri(ValueDisplayBase):
    """ValueDisplay<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueDisplayBool2(ValueDisplayBase):
    """ValueDisplay<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueDisplayByte2(ValueDisplayBase):
    """ValueDisplay<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueDisplayUshort2(ValueDisplayBase):
    """ValueDisplay<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueDisplayUint2(ValueDisplayBase):
    """ValueDisplay<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueDisplayUlong2(ValueDisplayBase):
    """ValueDisplay<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueDisplaySbyte2(ValueDisplayBase):
    """ValueDisplay<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueDisplayShort2(ValueDisplayBase):
    """ValueDisplay<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueDisplayInt2(ValueDisplayBase):
    """ValueDisplay<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueDisplayLong2(ValueDisplayBase):
    """ValueDisplay<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueDisplayFloat2(ValueDisplayBase):
    """ValueDisplay<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueDisplayDouble2(ValueDisplayBase):
    """ValueDisplay<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueDisplayBool3(ValueDisplayBase):
    """ValueDisplay<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueDisplayByte3(ValueDisplayBase):
    """ValueDisplay<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueDisplayUshort3(ValueDisplayBase):
    """ValueDisplay<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueDisplayUint3(ValueDisplayBase):
    """ValueDisplay<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueDisplayUlong3(ValueDisplayBase):
    """ValueDisplay<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueDisplaySbyte3(ValueDisplayBase):
    """ValueDisplay<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueDisplayShort3(ValueDisplayBase):
    """ValueDisplay<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueDisplayInt3(ValueDisplayBase):
    """ValueDisplay<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueDisplayLong3(ValueDisplayBase):
    """ValueDisplay<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueDisplayFloat3(ValueDisplayBase):
    """ValueDisplay<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueDisplayDouble3(ValueDisplayBase):
    """ValueDisplay<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueDisplayBool4(ValueDisplayBase):
    """ValueDisplay<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueDisplayByte4(ValueDisplayBase):
    """ValueDisplay<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueDisplayUshort4(ValueDisplayBase):
    """ValueDisplay<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueDisplayUint4(ValueDisplayBase):
    """ValueDisplay<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueDisplayUlong4(ValueDisplayBase):
    """ValueDisplay<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueDisplaySbyte4(ValueDisplayBase):
    """ValueDisplay<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueDisplayShort4(ValueDisplayBase):
    """ValueDisplay<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueDisplayInt4(ValueDisplayBase):
    """ValueDisplay<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueDisplayLong4(ValueDisplayBase):
    """ValueDisplay<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueDisplayFloat4(ValueDisplayBase):
    """ValueDisplay<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueDisplayDouble4(ValueDisplayBase):
    """ValueDisplay<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueDisplayFloat_2x2(ValueDisplayBase):
    """ValueDisplay<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueDisplayDouble_2x2(ValueDisplayBase):
    """ValueDisplay<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueDisplayFloat_3x3(ValueDisplayBase):
    """ValueDisplay<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueDisplayDouble_3x3(ValueDisplayBase):
    """ValueDisplay<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueDisplayFloat_4x4(ValueDisplayBase):
    """ValueDisplay<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueDisplayDouble_4x4(ValueDisplayBase):
    """ValueDisplay<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueDisplayFloatQ(ValueDisplayBase):
    """ValueDisplay<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueDisplayDoubleQ(ValueDisplayBase):
    """ValueDisplay<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueDisplayDateTime(ValueDisplayBase):
    """ValueDisplay<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueDisplayTimeSpan(ValueDisplayBase):
    """ValueDisplay<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueDisplayColor(ValueDisplayBase):
    """ValueDisplay<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueDisplayColorX(ValueDisplayBase):
    """ValueDisplay<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueDisplayShadowCastMode(ValueDisplayBase):
    """ValueDisplay<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueDisplayLightType(ValueDisplayBase):
    """ValueDisplay<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueDisplaySessionAccessLevel(ValueDisplayBase):
    """ValueDisplay<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueDisplayKey(ValueDisplayBase):
    """ValueDisplay<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueDisplayHttpStatusCode(ValueDisplayBase):
    """ValueDisplay<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueDisplayHeadOutputDevice(ValueDisplayBase):
    """ValueDisplay<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueDisplayReflectionProbeClear(ValueDisplayBase):
    """ValueDisplay<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueDisplayReflectionProbeType(ValueDisplayBase):
    """ValueDisplay<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueDisplayReflectionProbeTimeSlicingMode(ValueDisplayBase):
    """ValueDisplay<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueDisplayCameraClearMode(ValueDisplayBase):
    """ValueDisplay<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueDisplayCameraPositioningMode(ValueDisplayBase):
    """ValueDisplay<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueDisplayCameraProjection(ValueDisplayBase):
    """ValueDisplay<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueDisplayZWrite(ValueDisplayBase):
    """ValueDisplay<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueDisplayZTest(ValueDisplayBase):
    """ValueDisplay<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueDisplayBlend(ValueDisplayBase):
    """ValueDisplay<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueDisplayBlendMode(ValueDisplayBase):
    """ValueDisplay<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueDisplayCulling(ValueDisplayBase):
    """ValueDisplay<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueDisplayBodyNode(ValueDisplayBase):
    """ValueDisplay<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueDisplayChirality(ValueDisplayBase):
    """ValueDisplay<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueDisplayDummyEnum(ValueDisplayBase):
    """ValueDisplay<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDisplay<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueDisplay variant
ValueDisplay = (
    ValueDisplayBool |
    ValueDisplayByte |
    ValueDisplayUshort |
    ValueDisplayUint |
    ValueDisplayUlong |
    ValueDisplaySbyte |
    ValueDisplayShort |
    ValueDisplayInt |
    ValueDisplayLong |
    ValueDisplayFloat |
    ValueDisplayDouble |
    ValueDisplayDecimal |
    ValueDisplayChar |
    ValueDisplayString |
    ValueDisplayUri |
    ValueDisplayBool2 |
    ValueDisplayByte2 |
    ValueDisplayUshort2 |
    ValueDisplayUint2 |
    ValueDisplayUlong2 |
    ValueDisplaySbyte2 |
    ValueDisplayShort2 |
    ValueDisplayInt2 |
    ValueDisplayLong2 |
    ValueDisplayFloat2 |
    ValueDisplayDouble2 |
    ValueDisplayBool3 |
    ValueDisplayByte3 |
    ValueDisplayUshort3 |
    ValueDisplayUint3 |
    ValueDisplayUlong3 |
    ValueDisplaySbyte3 |
    ValueDisplayShort3 |
    ValueDisplayInt3 |
    ValueDisplayLong3 |
    ValueDisplayFloat3 |
    ValueDisplayDouble3 |
    ValueDisplayBool4 |
    ValueDisplayByte4 |
    ValueDisplayUshort4 |
    ValueDisplayUint4 |
    ValueDisplayUlong4 |
    ValueDisplaySbyte4 |
    ValueDisplayShort4 |
    ValueDisplayInt4 |
    ValueDisplayLong4 |
    ValueDisplayFloat4 |
    ValueDisplayDouble4 |
    ValueDisplayFloat_2x2 |
    ValueDisplayDouble_2x2 |
    ValueDisplayFloat_3x3 |
    ValueDisplayDouble_3x3 |
    ValueDisplayFloat_4x4 |
    ValueDisplayDouble_4x4 |
    ValueDisplayFloatQ |
    ValueDisplayDoubleQ |
    ValueDisplayDateTime |
    ValueDisplayTimeSpan |
    ValueDisplayColor |
    ValueDisplayColorX |
    ValueDisplayShadowCastMode |
    ValueDisplayLightType |
    ValueDisplaySessionAccessLevel |
    ValueDisplayKey |
    ValueDisplayHttpStatusCode |
    ValueDisplayHeadOutputDevice |
    ValueDisplayReflectionProbeClear |
    ValueDisplayReflectionProbeType |
    ValueDisplayReflectionProbeTimeSlicingMode |
    ValueDisplayCameraClearMode |
    ValueDisplayCameraPositioningMode |
    ValueDisplayCameraProjection |
    ValueDisplayZWrite |
    ValueDisplayZTest |
    ValueDisplayBlend |
    ValueDisplayBlendMode |
    ValueDisplayCulling |
    ValueDisplayBodyNode |
    ValueDisplayChirality |
    ValueDisplayDummyEnum
)