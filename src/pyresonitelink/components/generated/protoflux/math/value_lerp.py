"""Generated component: ValueLerp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueLerpBase(GeneratedComponent):
    """Base class for ValueLerp<T> variants."""

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
class ValueLerpBool(ValueLerpBase):
    """ValueLerp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueLerpByte(ValueLerpBase):
    """ValueLerp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueLerpUshort(ValueLerpBase):
    """ValueLerp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueLerpUint(ValueLerpBase):
    """ValueLerp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueLerpUlong(ValueLerpBase):
    """ValueLerp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueLerpSbyte(ValueLerpBase):
    """ValueLerp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueLerpShort(ValueLerpBase):
    """ValueLerp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueLerpInt(ValueLerpBase):
    """ValueLerp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueLerpLong(ValueLerpBase):
    """ValueLerp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueLerpFloat(ValueLerpBase):
    """ValueLerp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueLerpDouble(ValueLerpBase):
    """ValueLerp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueLerpDecimal(ValueLerpBase):
    """ValueLerp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueLerpChar(ValueLerpBase):
    """ValueLerp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueLerpString(ValueLerpBase):
    """ValueLerp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueLerpUri(ValueLerpBase):
    """ValueLerp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueLerpBool2(ValueLerpBase):
    """ValueLerp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueLerpByte2(ValueLerpBase):
    """ValueLerp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueLerpUshort2(ValueLerpBase):
    """ValueLerp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueLerpUint2(ValueLerpBase):
    """ValueLerp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueLerpUlong2(ValueLerpBase):
    """ValueLerp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueLerpSbyte2(ValueLerpBase):
    """ValueLerp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueLerpShort2(ValueLerpBase):
    """ValueLerp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueLerpInt2(ValueLerpBase):
    """ValueLerp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueLerpLong2(ValueLerpBase):
    """ValueLerp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueLerpFloat2(ValueLerpBase):
    """ValueLerp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueLerpDouble2(ValueLerpBase):
    """ValueLerp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueLerpBool3(ValueLerpBase):
    """ValueLerp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueLerpByte3(ValueLerpBase):
    """ValueLerp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueLerpUshort3(ValueLerpBase):
    """ValueLerp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueLerpUint3(ValueLerpBase):
    """ValueLerp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueLerpUlong3(ValueLerpBase):
    """ValueLerp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueLerpSbyte3(ValueLerpBase):
    """ValueLerp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueLerpShort3(ValueLerpBase):
    """ValueLerp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueLerpInt3(ValueLerpBase):
    """ValueLerp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueLerpLong3(ValueLerpBase):
    """ValueLerp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueLerpFloat3(ValueLerpBase):
    """ValueLerp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueLerpDouble3(ValueLerpBase):
    """ValueLerp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueLerpBool4(ValueLerpBase):
    """ValueLerp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueLerpByte4(ValueLerpBase):
    """ValueLerp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueLerpUshort4(ValueLerpBase):
    """ValueLerp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueLerpUint4(ValueLerpBase):
    """ValueLerp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueLerpUlong4(ValueLerpBase):
    """ValueLerp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueLerpSbyte4(ValueLerpBase):
    """ValueLerp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueLerpShort4(ValueLerpBase):
    """ValueLerp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueLerpInt4(ValueLerpBase):
    """ValueLerp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueLerpLong4(ValueLerpBase):
    """ValueLerp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueLerpFloat4(ValueLerpBase):
    """ValueLerp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueLerpDouble4(ValueLerpBase):
    """ValueLerp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueLerpFloat_2x2(ValueLerpBase):
    """ValueLerp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueLerpDouble_2x2(ValueLerpBase):
    """ValueLerp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueLerpFloat_3x3(ValueLerpBase):
    """ValueLerp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueLerpDouble_3x3(ValueLerpBase):
    """ValueLerp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueLerpFloat_4x4(ValueLerpBase):
    """ValueLerp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueLerpDouble_4x4(ValueLerpBase):
    """ValueLerp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueLerpFloatQ(ValueLerpBase):
    """ValueLerp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueLerpDoubleQ(ValueLerpBase):
    """ValueLerp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueLerpDateTime(ValueLerpBase):
    """ValueLerp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueLerpTimeSpan(ValueLerpBase):
    """ValueLerp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueLerpColor(ValueLerpBase):
    """ValueLerp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueLerpColorX(ValueLerpBase):
    """ValueLerp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueLerpShadowCastMode(ValueLerpBase):
    """ValueLerp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueLerpLightType(ValueLerpBase):
    """ValueLerp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueLerpSessionAccessLevel(ValueLerpBase):
    """ValueLerp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueLerpKey(ValueLerpBase):
    """ValueLerp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueLerpHttpStatusCode(ValueLerpBase):
    """ValueLerp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueLerpHeadOutputDevice(ValueLerpBase):
    """ValueLerp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueLerpReflectionProbeClear(ValueLerpBase):
    """ValueLerp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueLerpReflectionProbeType(ValueLerpBase):
    """ValueLerp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueLerpReflectionProbeTimeSlicingMode(ValueLerpBase):
    """ValueLerp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueLerpCameraClearMode(ValueLerpBase):
    """ValueLerp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueLerpCameraPositioningMode(ValueLerpBase):
    """ValueLerp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueLerpCameraProjection(ValueLerpBase):
    """ValueLerp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueLerpZWrite(ValueLerpBase):
    """ValueLerp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueLerpZTest(ValueLerpBase):
    """ValueLerp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueLerpBlend(ValueLerpBase):
    """ValueLerp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueLerpBlendMode(ValueLerpBase):
    """ValueLerp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueLerpCulling(ValueLerpBase):
    """ValueLerp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueLerpBodyNode(ValueLerpBase):
    """ValueLerp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueLerpChirality(ValueLerpBase):
    """ValueLerp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueLerpDummyEnum(ValueLerpBase):
    """ValueLerp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueLerp variant
ValueLerp = (
    ValueLerpBool |
    ValueLerpByte |
    ValueLerpUshort |
    ValueLerpUint |
    ValueLerpUlong |
    ValueLerpSbyte |
    ValueLerpShort |
    ValueLerpInt |
    ValueLerpLong |
    ValueLerpFloat |
    ValueLerpDouble |
    ValueLerpDecimal |
    ValueLerpChar |
    ValueLerpString |
    ValueLerpUri |
    ValueLerpBool2 |
    ValueLerpByte2 |
    ValueLerpUshort2 |
    ValueLerpUint2 |
    ValueLerpUlong2 |
    ValueLerpSbyte2 |
    ValueLerpShort2 |
    ValueLerpInt2 |
    ValueLerpLong2 |
    ValueLerpFloat2 |
    ValueLerpDouble2 |
    ValueLerpBool3 |
    ValueLerpByte3 |
    ValueLerpUshort3 |
    ValueLerpUint3 |
    ValueLerpUlong3 |
    ValueLerpSbyte3 |
    ValueLerpShort3 |
    ValueLerpInt3 |
    ValueLerpLong3 |
    ValueLerpFloat3 |
    ValueLerpDouble3 |
    ValueLerpBool4 |
    ValueLerpByte4 |
    ValueLerpUshort4 |
    ValueLerpUint4 |
    ValueLerpUlong4 |
    ValueLerpSbyte4 |
    ValueLerpShort4 |
    ValueLerpInt4 |
    ValueLerpLong4 |
    ValueLerpFloat4 |
    ValueLerpDouble4 |
    ValueLerpFloat_2x2 |
    ValueLerpDouble_2x2 |
    ValueLerpFloat_3x3 |
    ValueLerpDouble_3x3 |
    ValueLerpFloat_4x4 |
    ValueLerpDouble_4x4 |
    ValueLerpFloatQ |
    ValueLerpDoubleQ |
    ValueLerpDateTime |
    ValueLerpTimeSpan |
    ValueLerpColor |
    ValueLerpColorX |
    ValueLerpShadowCastMode |
    ValueLerpLightType |
    ValueLerpSessionAccessLevel |
    ValueLerpKey |
    ValueLerpHttpStatusCode |
    ValueLerpHeadOutputDevice |
    ValueLerpReflectionProbeClear |
    ValueLerpReflectionProbeType |
    ValueLerpReflectionProbeTimeSlicingMode |
    ValueLerpCameraClearMode |
    ValueLerpCameraPositioningMode |
    ValueLerpCameraProjection |
    ValueLerpZWrite |
    ValueLerpZTest |
    ValueLerpBlend |
    ValueLerpBlendMode |
    ValueLerpCulling |
    ValueLerpBodyNode |
    ValueLerpChirality |
    ValueLerpDummyEnum
)