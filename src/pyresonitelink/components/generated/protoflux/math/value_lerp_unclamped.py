"""Generated component: ValueLerpUnclamped.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueLerpUnclampedBase(GeneratedComponent):
    """Base class for ValueLerpUnclamped<T> variants."""

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
class ValueLerpUnclampedBool(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueLerpUnclampedByte(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueLerpUnclampedUshort(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueLerpUnclampedUint(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueLerpUnclampedUlong(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueLerpUnclampedSbyte(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueLerpUnclampedShort(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueLerpUnclampedInt(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueLerpUnclampedLong(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueLerpUnclampedFloat(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueLerpUnclampedDouble(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueLerpUnclampedDecimal(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueLerpUnclampedChar(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueLerpUnclampedString(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueLerpUnclampedUri(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueLerpUnclampedBool2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueLerpUnclampedByte2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueLerpUnclampedUshort2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueLerpUnclampedUint2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueLerpUnclampedUlong2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueLerpUnclampedSbyte2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueLerpUnclampedShort2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueLerpUnclampedInt2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueLerpUnclampedLong2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueLerpUnclampedFloat2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueLerpUnclampedDouble2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueLerpUnclampedBool3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueLerpUnclampedByte3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueLerpUnclampedUshort3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueLerpUnclampedUint3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueLerpUnclampedUlong3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueLerpUnclampedSbyte3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueLerpUnclampedShort3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueLerpUnclampedInt3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueLerpUnclampedLong3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueLerpUnclampedFloat3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueLerpUnclampedDouble3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueLerpUnclampedBool4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueLerpUnclampedByte4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueLerpUnclampedUshort4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueLerpUnclampedUint4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueLerpUnclampedUlong4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueLerpUnclampedSbyte4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueLerpUnclampedShort4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueLerpUnclampedInt4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueLerpUnclampedLong4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueLerpUnclampedFloat4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueLerpUnclampedDouble4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueLerpUnclampedFloat_2x2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueLerpUnclampedDouble_2x2(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueLerpUnclampedFloat_3x3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueLerpUnclampedDouble_3x3(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueLerpUnclampedFloat_4x4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueLerpUnclampedDouble_4x4(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueLerpUnclampedFloatQ(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueLerpUnclampedDoubleQ(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueLerpUnclampedDateTime(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueLerpUnclampedTimeSpan(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueLerpUnclampedColor(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueLerpUnclampedColorX(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueLerpUnclampedShadowCastMode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueLerpUnclampedLightType(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueLerpUnclampedSessionAccessLevel(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueLerpUnclampedKey(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueLerpUnclampedHttpStatusCode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueLerpUnclampedHeadOutputDevice(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueLerpUnclampedReflectionProbeClear(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueLerpUnclampedReflectionProbeType(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueLerpUnclampedReflectionProbeTimeSlicingMode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueLerpUnclampedCameraClearMode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueLerpUnclampedCameraPositioningMode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueLerpUnclampedCameraProjection(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueLerpUnclampedZWrite(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueLerpUnclampedZTest(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueLerpUnclampedBlend(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueLerpUnclampedBlendMode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueLerpUnclampedCulling(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueLerpUnclampedBodyNode(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueLerpUnclampedChirality(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueLerpUnclampedDummyEnum(ValueLerpUnclampedBase):
    """ValueLerpUnclamped<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerpUnclamped<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "lerp": "Lerp",
        "to": "To",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueLerpUnclamped variant
ValueLerpUnclamped = (
    ValueLerpUnclampedBool |
    ValueLerpUnclampedByte |
    ValueLerpUnclampedUshort |
    ValueLerpUnclampedUint |
    ValueLerpUnclampedUlong |
    ValueLerpUnclampedSbyte |
    ValueLerpUnclampedShort |
    ValueLerpUnclampedInt |
    ValueLerpUnclampedLong |
    ValueLerpUnclampedFloat |
    ValueLerpUnclampedDouble |
    ValueLerpUnclampedDecimal |
    ValueLerpUnclampedChar |
    ValueLerpUnclampedString |
    ValueLerpUnclampedUri |
    ValueLerpUnclampedBool2 |
    ValueLerpUnclampedByte2 |
    ValueLerpUnclampedUshort2 |
    ValueLerpUnclampedUint2 |
    ValueLerpUnclampedUlong2 |
    ValueLerpUnclampedSbyte2 |
    ValueLerpUnclampedShort2 |
    ValueLerpUnclampedInt2 |
    ValueLerpUnclampedLong2 |
    ValueLerpUnclampedFloat2 |
    ValueLerpUnclampedDouble2 |
    ValueLerpUnclampedBool3 |
    ValueLerpUnclampedByte3 |
    ValueLerpUnclampedUshort3 |
    ValueLerpUnclampedUint3 |
    ValueLerpUnclampedUlong3 |
    ValueLerpUnclampedSbyte3 |
    ValueLerpUnclampedShort3 |
    ValueLerpUnclampedInt3 |
    ValueLerpUnclampedLong3 |
    ValueLerpUnclampedFloat3 |
    ValueLerpUnclampedDouble3 |
    ValueLerpUnclampedBool4 |
    ValueLerpUnclampedByte4 |
    ValueLerpUnclampedUshort4 |
    ValueLerpUnclampedUint4 |
    ValueLerpUnclampedUlong4 |
    ValueLerpUnclampedSbyte4 |
    ValueLerpUnclampedShort4 |
    ValueLerpUnclampedInt4 |
    ValueLerpUnclampedLong4 |
    ValueLerpUnclampedFloat4 |
    ValueLerpUnclampedDouble4 |
    ValueLerpUnclampedFloat_2x2 |
    ValueLerpUnclampedDouble_2x2 |
    ValueLerpUnclampedFloat_3x3 |
    ValueLerpUnclampedDouble_3x3 |
    ValueLerpUnclampedFloat_4x4 |
    ValueLerpUnclampedDouble_4x4 |
    ValueLerpUnclampedFloatQ |
    ValueLerpUnclampedDoubleQ |
    ValueLerpUnclampedDateTime |
    ValueLerpUnclampedTimeSpan |
    ValueLerpUnclampedColor |
    ValueLerpUnclampedColorX |
    ValueLerpUnclampedShadowCastMode |
    ValueLerpUnclampedLightType |
    ValueLerpUnclampedSessionAccessLevel |
    ValueLerpUnclampedKey |
    ValueLerpUnclampedHttpStatusCode |
    ValueLerpUnclampedHeadOutputDevice |
    ValueLerpUnclampedReflectionProbeClear |
    ValueLerpUnclampedReflectionProbeType |
    ValueLerpUnclampedReflectionProbeTimeSlicingMode |
    ValueLerpUnclampedCameraClearMode |
    ValueLerpUnclampedCameraPositioningMode |
    ValueLerpUnclampedCameraProjection |
    ValueLerpUnclampedZWrite |
    ValueLerpUnclampedZTest |
    ValueLerpUnclampedBlend |
    ValueLerpUnclampedBlendMode |
    ValueLerpUnclampedCulling |
    ValueLerpUnclampedBodyNode |
    ValueLerpUnclampedChirality |
    ValueLerpUnclampedDummyEnum
)