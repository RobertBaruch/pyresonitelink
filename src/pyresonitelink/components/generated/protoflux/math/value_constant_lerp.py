"""Generated component: ValueConstantLerp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueConstantLerpBase(GeneratedComponent):
    """Base class for ValueConstantLerp<T> variants."""

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
class ValueConstantLerpBool(ValueConstantLerpBase):
    """ValueConstantLerp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpByte(ValueConstantLerpBase):
    """ValueConstantLerp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUshort(ValueConstantLerpBase):
    """ValueConstantLerp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUint(ValueConstantLerpBase):
    """ValueConstantLerp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUlong(ValueConstantLerpBase):
    """ValueConstantLerp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpSbyte(ValueConstantLerpBase):
    """ValueConstantLerp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpShort(ValueConstantLerpBase):
    """ValueConstantLerp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpInt(ValueConstantLerpBase):
    """ValueConstantLerp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpLong(ValueConstantLerpBase):
    """ValueConstantLerp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat(ValueConstantLerpBase):
    """ValueConstantLerp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble(ValueConstantLerpBase):
    """ValueConstantLerp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDecimal(ValueConstantLerpBase):
    """ValueConstantLerp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpChar(ValueConstantLerpBase):
    """ValueConstantLerp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpString(ValueConstantLerpBase):
    """ValueConstantLerp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUri(ValueConstantLerpBase):
    """ValueConstantLerp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBool2(ValueConstantLerpBase):
    """ValueConstantLerp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpByte2(ValueConstantLerpBase):
    """ValueConstantLerp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUshort2(ValueConstantLerpBase):
    """ValueConstantLerp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUint2(ValueConstantLerpBase):
    """ValueConstantLerp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUlong2(ValueConstantLerpBase):
    """ValueConstantLerp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpSbyte2(ValueConstantLerpBase):
    """ValueConstantLerp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpShort2(ValueConstantLerpBase):
    """ValueConstantLerp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpInt2(ValueConstantLerpBase):
    """ValueConstantLerp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpLong2(ValueConstantLerpBase):
    """ValueConstantLerp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat2(ValueConstantLerpBase):
    """ValueConstantLerp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble2(ValueConstantLerpBase):
    """ValueConstantLerp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBool3(ValueConstantLerpBase):
    """ValueConstantLerp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpByte3(ValueConstantLerpBase):
    """ValueConstantLerp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUshort3(ValueConstantLerpBase):
    """ValueConstantLerp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUint3(ValueConstantLerpBase):
    """ValueConstantLerp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUlong3(ValueConstantLerpBase):
    """ValueConstantLerp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpSbyte3(ValueConstantLerpBase):
    """ValueConstantLerp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpShort3(ValueConstantLerpBase):
    """ValueConstantLerp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpInt3(ValueConstantLerpBase):
    """ValueConstantLerp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpLong3(ValueConstantLerpBase):
    """ValueConstantLerp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat3(ValueConstantLerpBase):
    """ValueConstantLerp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble3(ValueConstantLerpBase):
    """ValueConstantLerp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBool4(ValueConstantLerpBase):
    """ValueConstantLerp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpByte4(ValueConstantLerpBase):
    """ValueConstantLerp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUshort4(ValueConstantLerpBase):
    """ValueConstantLerp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUint4(ValueConstantLerpBase):
    """ValueConstantLerp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpUlong4(ValueConstantLerpBase):
    """ValueConstantLerp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpSbyte4(ValueConstantLerpBase):
    """ValueConstantLerp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpShort4(ValueConstantLerpBase):
    """ValueConstantLerp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpInt4(ValueConstantLerpBase):
    """ValueConstantLerp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpLong4(ValueConstantLerpBase):
    """ValueConstantLerp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat4(ValueConstantLerpBase):
    """ValueConstantLerp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble4(ValueConstantLerpBase):
    """ValueConstantLerp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat_2x2(ValueConstantLerpBase):
    """ValueConstantLerp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble_2x2(ValueConstantLerpBase):
    """ValueConstantLerp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat_3x3(ValueConstantLerpBase):
    """ValueConstantLerp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble_3x3(ValueConstantLerpBase):
    """ValueConstantLerp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloat_4x4(ValueConstantLerpBase):
    """ValueConstantLerp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDouble_4x4(ValueConstantLerpBase):
    """ValueConstantLerp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpFloatQ(ValueConstantLerpBase):
    """ValueConstantLerp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDoubleQ(ValueConstantLerpBase):
    """ValueConstantLerp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDateTime(ValueConstantLerpBase):
    """ValueConstantLerp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpTimeSpan(ValueConstantLerpBase):
    """ValueConstantLerp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpColor(ValueConstantLerpBase):
    """ValueConstantLerp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpColorX(ValueConstantLerpBase):
    """ValueConstantLerp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpShadowCastMode(ValueConstantLerpBase):
    """ValueConstantLerp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpLightType(ValueConstantLerpBase):
    """ValueConstantLerp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpSessionAccessLevel(ValueConstantLerpBase):
    """ValueConstantLerp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpKey(ValueConstantLerpBase):
    """ValueConstantLerp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpHttpStatusCode(ValueConstantLerpBase):
    """ValueConstantLerp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpHeadOutputDevice(ValueConstantLerpBase):
    """ValueConstantLerp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpReflectionProbeClear(ValueConstantLerpBase):
    """ValueConstantLerp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpReflectionProbeType(ValueConstantLerpBase):
    """ValueConstantLerp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpReflectionProbeTimeSlicingMode(ValueConstantLerpBase):
    """ValueConstantLerp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpCameraClearMode(ValueConstantLerpBase):
    """ValueConstantLerp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpCameraPositioningMode(ValueConstantLerpBase):
    """ValueConstantLerp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpCameraProjection(ValueConstantLerpBase):
    """ValueConstantLerp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpZWrite(ValueConstantLerpBase):
    """ValueConstantLerp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpZTest(ValueConstantLerpBase):
    """ValueConstantLerp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBlend(ValueConstantLerpBase):
    """ValueConstantLerp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBlendMode(ValueConstantLerpBase):
    """ValueConstantLerp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpCulling(ValueConstantLerpBase):
    """ValueConstantLerp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpBodyNode(ValueConstantLerpBase):
    """ValueConstantLerp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpChirality(ValueConstantLerpBase):
    """ValueConstantLerp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueConstantLerpDummyEnum(ValueConstantLerpBase):
    """ValueConstantLerp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueConstantLerp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


# Type alias for any ValueConstantLerp variant
ValueConstantLerp = (
    ValueConstantLerpBool |
    ValueConstantLerpByte |
    ValueConstantLerpUshort |
    ValueConstantLerpUint |
    ValueConstantLerpUlong |
    ValueConstantLerpSbyte |
    ValueConstantLerpShort |
    ValueConstantLerpInt |
    ValueConstantLerpLong |
    ValueConstantLerpFloat |
    ValueConstantLerpDouble |
    ValueConstantLerpDecimal |
    ValueConstantLerpChar |
    ValueConstantLerpString |
    ValueConstantLerpUri |
    ValueConstantLerpBool2 |
    ValueConstantLerpByte2 |
    ValueConstantLerpUshort2 |
    ValueConstantLerpUint2 |
    ValueConstantLerpUlong2 |
    ValueConstantLerpSbyte2 |
    ValueConstantLerpShort2 |
    ValueConstantLerpInt2 |
    ValueConstantLerpLong2 |
    ValueConstantLerpFloat2 |
    ValueConstantLerpDouble2 |
    ValueConstantLerpBool3 |
    ValueConstantLerpByte3 |
    ValueConstantLerpUshort3 |
    ValueConstantLerpUint3 |
    ValueConstantLerpUlong3 |
    ValueConstantLerpSbyte3 |
    ValueConstantLerpShort3 |
    ValueConstantLerpInt3 |
    ValueConstantLerpLong3 |
    ValueConstantLerpFloat3 |
    ValueConstantLerpDouble3 |
    ValueConstantLerpBool4 |
    ValueConstantLerpByte4 |
    ValueConstantLerpUshort4 |
    ValueConstantLerpUint4 |
    ValueConstantLerpUlong4 |
    ValueConstantLerpSbyte4 |
    ValueConstantLerpShort4 |
    ValueConstantLerpInt4 |
    ValueConstantLerpLong4 |
    ValueConstantLerpFloat4 |
    ValueConstantLerpDouble4 |
    ValueConstantLerpFloat_2x2 |
    ValueConstantLerpDouble_2x2 |
    ValueConstantLerpFloat_3x3 |
    ValueConstantLerpDouble_3x3 |
    ValueConstantLerpFloat_4x4 |
    ValueConstantLerpDouble_4x4 |
    ValueConstantLerpFloatQ |
    ValueConstantLerpDoubleQ |
    ValueConstantLerpDateTime |
    ValueConstantLerpTimeSpan |
    ValueConstantLerpColor |
    ValueConstantLerpColorX |
    ValueConstantLerpShadowCastMode |
    ValueConstantLerpLightType |
    ValueConstantLerpSessionAccessLevel |
    ValueConstantLerpKey |
    ValueConstantLerpHttpStatusCode |
    ValueConstantLerpHeadOutputDevice |
    ValueConstantLerpReflectionProbeClear |
    ValueConstantLerpReflectionProbeType |
    ValueConstantLerpReflectionProbeTimeSlicingMode |
    ValueConstantLerpCameraClearMode |
    ValueConstantLerpCameraPositioningMode |
    ValueConstantLerpCameraProjection |
    ValueConstantLerpZWrite |
    ValueConstantLerpZTest |
    ValueConstantLerpBlend |
    ValueConstantLerpBlendMode |
    ValueConstantLerpCulling |
    ValueConstantLerpBodyNode |
    ValueConstantLerpChirality |
    ValueConstantLerpDummyEnum
)