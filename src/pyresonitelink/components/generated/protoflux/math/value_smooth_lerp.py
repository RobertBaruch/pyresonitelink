"""Generated component: ValueSmoothLerp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueSmoothLerpBase(GeneratedComponent):
    """Base class for ValueSmoothLerp<T> variants."""

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
class ValueSmoothLerpBool(ValueSmoothLerpBase):
    """ValueSmoothLerp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpByte(ValueSmoothLerpBase):
    """ValueSmoothLerp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUshort(ValueSmoothLerpBase):
    """ValueSmoothLerp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUint(ValueSmoothLerpBase):
    """ValueSmoothLerp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUlong(ValueSmoothLerpBase):
    """ValueSmoothLerp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpSbyte(ValueSmoothLerpBase):
    """ValueSmoothLerp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpShort(ValueSmoothLerpBase):
    """ValueSmoothLerp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpInt(ValueSmoothLerpBase):
    """ValueSmoothLerp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpLong(ValueSmoothLerpBase):
    """ValueSmoothLerp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat(ValueSmoothLerpBase):
    """ValueSmoothLerp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble(ValueSmoothLerpBase):
    """ValueSmoothLerp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDecimal(ValueSmoothLerpBase):
    """ValueSmoothLerp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpChar(ValueSmoothLerpBase):
    """ValueSmoothLerp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpString(ValueSmoothLerpBase):
    """ValueSmoothLerp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUri(ValueSmoothLerpBase):
    """ValueSmoothLerp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBool2(ValueSmoothLerpBase):
    """ValueSmoothLerp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpByte2(ValueSmoothLerpBase):
    """ValueSmoothLerp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUshort2(ValueSmoothLerpBase):
    """ValueSmoothLerp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUint2(ValueSmoothLerpBase):
    """ValueSmoothLerp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUlong2(ValueSmoothLerpBase):
    """ValueSmoothLerp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpSbyte2(ValueSmoothLerpBase):
    """ValueSmoothLerp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpShort2(ValueSmoothLerpBase):
    """ValueSmoothLerp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpInt2(ValueSmoothLerpBase):
    """ValueSmoothLerp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpLong2(ValueSmoothLerpBase):
    """ValueSmoothLerp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat2(ValueSmoothLerpBase):
    """ValueSmoothLerp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble2(ValueSmoothLerpBase):
    """ValueSmoothLerp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBool3(ValueSmoothLerpBase):
    """ValueSmoothLerp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpByte3(ValueSmoothLerpBase):
    """ValueSmoothLerp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUshort3(ValueSmoothLerpBase):
    """ValueSmoothLerp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUint3(ValueSmoothLerpBase):
    """ValueSmoothLerp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUlong3(ValueSmoothLerpBase):
    """ValueSmoothLerp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpSbyte3(ValueSmoothLerpBase):
    """ValueSmoothLerp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpShort3(ValueSmoothLerpBase):
    """ValueSmoothLerp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpInt3(ValueSmoothLerpBase):
    """ValueSmoothLerp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpLong3(ValueSmoothLerpBase):
    """ValueSmoothLerp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat3(ValueSmoothLerpBase):
    """ValueSmoothLerp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble3(ValueSmoothLerpBase):
    """ValueSmoothLerp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBool4(ValueSmoothLerpBase):
    """ValueSmoothLerp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpByte4(ValueSmoothLerpBase):
    """ValueSmoothLerp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUshort4(ValueSmoothLerpBase):
    """ValueSmoothLerp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUint4(ValueSmoothLerpBase):
    """ValueSmoothLerp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpUlong4(ValueSmoothLerpBase):
    """ValueSmoothLerp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpSbyte4(ValueSmoothLerpBase):
    """ValueSmoothLerp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpShort4(ValueSmoothLerpBase):
    """ValueSmoothLerp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpInt4(ValueSmoothLerpBase):
    """ValueSmoothLerp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpLong4(ValueSmoothLerpBase):
    """ValueSmoothLerp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat4(ValueSmoothLerpBase):
    """ValueSmoothLerp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble4(ValueSmoothLerpBase):
    """ValueSmoothLerp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat_2x2(ValueSmoothLerpBase):
    """ValueSmoothLerp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble_2x2(ValueSmoothLerpBase):
    """ValueSmoothLerp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat_3x3(ValueSmoothLerpBase):
    """ValueSmoothLerp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble_3x3(ValueSmoothLerpBase):
    """ValueSmoothLerp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloat_4x4(ValueSmoothLerpBase):
    """ValueSmoothLerp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDouble_4x4(ValueSmoothLerpBase):
    """ValueSmoothLerp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpFloatQ(ValueSmoothLerpBase):
    """ValueSmoothLerp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDoubleQ(ValueSmoothLerpBase):
    """ValueSmoothLerp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDateTime(ValueSmoothLerpBase):
    """ValueSmoothLerp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpTimeSpan(ValueSmoothLerpBase):
    """ValueSmoothLerp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpColor(ValueSmoothLerpBase):
    """ValueSmoothLerp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpColorX(ValueSmoothLerpBase):
    """ValueSmoothLerp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpShadowCastMode(ValueSmoothLerpBase):
    """ValueSmoothLerp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpLightType(ValueSmoothLerpBase):
    """ValueSmoothLerp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpSessionAccessLevel(ValueSmoothLerpBase):
    """ValueSmoothLerp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpKey(ValueSmoothLerpBase):
    """ValueSmoothLerp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpHttpStatusCode(ValueSmoothLerpBase):
    """ValueSmoothLerp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpHeadOutputDevice(ValueSmoothLerpBase):
    """ValueSmoothLerp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpReflectionProbeClear(ValueSmoothLerpBase):
    """ValueSmoothLerp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpReflectionProbeType(ValueSmoothLerpBase):
    """ValueSmoothLerp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpReflectionProbeTimeSlicingMode(ValueSmoothLerpBase):
    """ValueSmoothLerp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpCameraClearMode(ValueSmoothLerpBase):
    """ValueSmoothLerp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpCameraPositioningMode(ValueSmoothLerpBase):
    """ValueSmoothLerp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpCameraProjection(ValueSmoothLerpBase):
    """ValueSmoothLerp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpZWrite(ValueSmoothLerpBase):
    """ValueSmoothLerp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpZTest(ValueSmoothLerpBase):
    """ValueSmoothLerp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBlend(ValueSmoothLerpBase):
    """ValueSmoothLerp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBlendMode(ValueSmoothLerpBase):
    """ValueSmoothLerp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpCulling(ValueSmoothLerpBase):
    """ValueSmoothLerp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpBodyNode(ValueSmoothLerpBase):
    """ValueSmoothLerp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpChirality(ValueSmoothLerpBase):
    """ValueSmoothLerp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueSmoothLerpDummyEnum(ValueSmoothLerpBase):
    """ValueSmoothLerp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueSmoothLerp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
        "speed": "Speed",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


# Type alias for any ValueSmoothLerp variant
ValueSmoothLerp = (
    ValueSmoothLerpBool |
    ValueSmoothLerpByte |
    ValueSmoothLerpUshort |
    ValueSmoothLerpUint |
    ValueSmoothLerpUlong |
    ValueSmoothLerpSbyte |
    ValueSmoothLerpShort |
    ValueSmoothLerpInt |
    ValueSmoothLerpLong |
    ValueSmoothLerpFloat |
    ValueSmoothLerpDouble |
    ValueSmoothLerpDecimal |
    ValueSmoothLerpChar |
    ValueSmoothLerpString |
    ValueSmoothLerpUri |
    ValueSmoothLerpBool2 |
    ValueSmoothLerpByte2 |
    ValueSmoothLerpUshort2 |
    ValueSmoothLerpUint2 |
    ValueSmoothLerpUlong2 |
    ValueSmoothLerpSbyte2 |
    ValueSmoothLerpShort2 |
    ValueSmoothLerpInt2 |
    ValueSmoothLerpLong2 |
    ValueSmoothLerpFloat2 |
    ValueSmoothLerpDouble2 |
    ValueSmoothLerpBool3 |
    ValueSmoothLerpByte3 |
    ValueSmoothLerpUshort3 |
    ValueSmoothLerpUint3 |
    ValueSmoothLerpUlong3 |
    ValueSmoothLerpSbyte3 |
    ValueSmoothLerpShort3 |
    ValueSmoothLerpInt3 |
    ValueSmoothLerpLong3 |
    ValueSmoothLerpFloat3 |
    ValueSmoothLerpDouble3 |
    ValueSmoothLerpBool4 |
    ValueSmoothLerpByte4 |
    ValueSmoothLerpUshort4 |
    ValueSmoothLerpUint4 |
    ValueSmoothLerpUlong4 |
    ValueSmoothLerpSbyte4 |
    ValueSmoothLerpShort4 |
    ValueSmoothLerpInt4 |
    ValueSmoothLerpLong4 |
    ValueSmoothLerpFloat4 |
    ValueSmoothLerpDouble4 |
    ValueSmoothLerpFloat_2x2 |
    ValueSmoothLerpDouble_2x2 |
    ValueSmoothLerpFloat_3x3 |
    ValueSmoothLerpDouble_3x3 |
    ValueSmoothLerpFloat_4x4 |
    ValueSmoothLerpDouble_4x4 |
    ValueSmoothLerpFloatQ |
    ValueSmoothLerpDoubleQ |
    ValueSmoothLerpDateTime |
    ValueSmoothLerpTimeSpan |
    ValueSmoothLerpColor |
    ValueSmoothLerpColorX |
    ValueSmoothLerpShadowCastMode |
    ValueSmoothLerpLightType |
    ValueSmoothLerpSessionAccessLevel |
    ValueSmoothLerpKey |
    ValueSmoothLerpHttpStatusCode |
    ValueSmoothLerpHeadOutputDevice |
    ValueSmoothLerpReflectionProbeClear |
    ValueSmoothLerpReflectionProbeType |
    ValueSmoothLerpReflectionProbeTimeSlicingMode |
    ValueSmoothLerpCameraClearMode |
    ValueSmoothLerpCameraPositioningMode |
    ValueSmoothLerpCameraProjection |
    ValueSmoothLerpZWrite |
    ValueSmoothLerpZTest |
    ValueSmoothLerpBlend |
    ValueSmoothLerpBlendMode |
    ValueSmoothLerpCulling |
    ValueSmoothLerpBodyNode |
    ValueSmoothLerpChirality |
    ValueSmoothLerpDummyEnum
)