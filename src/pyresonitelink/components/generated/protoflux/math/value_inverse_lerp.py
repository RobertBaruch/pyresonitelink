"""Generated component: ValueInverseLerp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueInverseLerpBase(GeneratedComponent):
    """Base class for ValueInverseLerp<T> variants."""

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
class ValueInverseLerpBool(ValueInverseLerpBase):
    """ValueInverseLerp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueInverseLerpByte(ValueInverseLerpBase):
    """ValueInverseLerp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueInverseLerpUshort(ValueInverseLerpBase):
    """ValueInverseLerp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueInverseLerpUint(ValueInverseLerpBase):
    """ValueInverseLerp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueInverseLerpUlong(ValueInverseLerpBase):
    """ValueInverseLerp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueInverseLerpSbyte(ValueInverseLerpBase):
    """ValueInverseLerp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueInverseLerpShort(ValueInverseLerpBase):
    """ValueInverseLerp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueInverseLerpInt(ValueInverseLerpBase):
    """ValueInverseLerp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueInverseLerpLong(ValueInverseLerpBase):
    """ValueInverseLerp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueInverseLerpFloat(ValueInverseLerpBase):
    """ValueInverseLerp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueInverseLerpDouble(ValueInverseLerpBase):
    """ValueInverseLerp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueInverseLerpDecimal(ValueInverseLerpBase):
    """ValueInverseLerp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueInverseLerpChar(ValueInverseLerpBase):
    """ValueInverseLerp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueInverseLerpString(ValueInverseLerpBase):
    """ValueInverseLerp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueInverseLerpUri(ValueInverseLerpBase):
    """ValueInverseLerp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueInverseLerpBool2(ValueInverseLerpBase):
    """ValueInverseLerp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueInverseLerpByte2(ValueInverseLerpBase):
    """ValueInverseLerp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueInverseLerpUshort2(ValueInverseLerpBase):
    """ValueInverseLerp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueInverseLerpUint2(ValueInverseLerpBase):
    """ValueInverseLerp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueInverseLerpUlong2(ValueInverseLerpBase):
    """ValueInverseLerp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueInverseLerpSbyte2(ValueInverseLerpBase):
    """ValueInverseLerp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueInverseLerpShort2(ValueInverseLerpBase):
    """ValueInverseLerp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueInverseLerpInt2(ValueInverseLerpBase):
    """ValueInverseLerp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueInverseLerpLong2(ValueInverseLerpBase):
    """ValueInverseLerp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueInverseLerpFloat2(ValueInverseLerpBase):
    """ValueInverseLerp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueInverseLerpDouble2(ValueInverseLerpBase):
    """ValueInverseLerp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueInverseLerpBool3(ValueInverseLerpBase):
    """ValueInverseLerp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueInverseLerpByte3(ValueInverseLerpBase):
    """ValueInverseLerp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueInverseLerpUshort3(ValueInverseLerpBase):
    """ValueInverseLerp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueInverseLerpUint3(ValueInverseLerpBase):
    """ValueInverseLerp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueInverseLerpUlong3(ValueInverseLerpBase):
    """ValueInverseLerp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueInverseLerpSbyte3(ValueInverseLerpBase):
    """ValueInverseLerp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueInverseLerpShort3(ValueInverseLerpBase):
    """ValueInverseLerp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueInverseLerpInt3(ValueInverseLerpBase):
    """ValueInverseLerp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueInverseLerpLong3(ValueInverseLerpBase):
    """ValueInverseLerp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueInverseLerpFloat3(ValueInverseLerpBase):
    """ValueInverseLerp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueInverseLerpDouble3(ValueInverseLerpBase):
    """ValueInverseLerp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueInverseLerpBool4(ValueInverseLerpBase):
    """ValueInverseLerp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueInverseLerpByte4(ValueInverseLerpBase):
    """ValueInverseLerp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueInverseLerpUshort4(ValueInverseLerpBase):
    """ValueInverseLerp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueInverseLerpUint4(ValueInverseLerpBase):
    """ValueInverseLerp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueInverseLerpUlong4(ValueInverseLerpBase):
    """ValueInverseLerp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueInverseLerpSbyte4(ValueInverseLerpBase):
    """ValueInverseLerp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueInverseLerpShort4(ValueInverseLerpBase):
    """ValueInverseLerp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueInverseLerpInt4(ValueInverseLerpBase):
    """ValueInverseLerp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueInverseLerpLong4(ValueInverseLerpBase):
    """ValueInverseLerp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueInverseLerpFloat4(ValueInverseLerpBase):
    """ValueInverseLerp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueInverseLerpDouble4(ValueInverseLerpBase):
    """ValueInverseLerp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueInverseLerpFloat_2x2(ValueInverseLerpBase):
    """ValueInverseLerp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueInverseLerpDouble_2x2(ValueInverseLerpBase):
    """ValueInverseLerp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueInverseLerpFloat_3x3(ValueInverseLerpBase):
    """ValueInverseLerp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueInverseLerpDouble_3x3(ValueInverseLerpBase):
    """ValueInverseLerp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueInverseLerpFloat_4x4(ValueInverseLerpBase):
    """ValueInverseLerp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueInverseLerpDouble_4x4(ValueInverseLerpBase):
    """ValueInverseLerp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueInverseLerpFloatQ(ValueInverseLerpBase):
    """ValueInverseLerp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueInverseLerpDoubleQ(ValueInverseLerpBase):
    """ValueInverseLerp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueInverseLerpDateTime(ValueInverseLerpBase):
    """ValueInverseLerp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueInverseLerpTimeSpan(ValueInverseLerpBase):
    """ValueInverseLerp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueInverseLerpColor(ValueInverseLerpBase):
    """ValueInverseLerp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueInverseLerpColorX(ValueInverseLerpBase):
    """ValueInverseLerp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueInverseLerpShadowCastMode(ValueInverseLerpBase):
    """ValueInverseLerp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueInverseLerpLightType(ValueInverseLerpBase):
    """ValueInverseLerp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueInverseLerpSessionAccessLevel(ValueInverseLerpBase):
    """ValueInverseLerp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueInverseLerpKey(ValueInverseLerpBase):
    """ValueInverseLerp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueInverseLerpHttpStatusCode(ValueInverseLerpBase):
    """ValueInverseLerp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueInverseLerpHeadOutputDevice(ValueInverseLerpBase):
    """ValueInverseLerp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueInverseLerpReflectionProbeClear(ValueInverseLerpBase):
    """ValueInverseLerp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueInverseLerpReflectionProbeType(ValueInverseLerpBase):
    """ValueInverseLerp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueInverseLerpReflectionProbeTimeSlicingMode(ValueInverseLerpBase):
    """ValueInverseLerp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueInverseLerpCameraClearMode(ValueInverseLerpBase):
    """ValueInverseLerp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueInverseLerpCameraPositioningMode(ValueInverseLerpBase):
    """ValueInverseLerp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueInverseLerpCameraProjection(ValueInverseLerpBase):
    """ValueInverseLerp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueInverseLerpZWrite(ValueInverseLerpBase):
    """ValueInverseLerp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueInverseLerpZTest(ValueInverseLerpBase):
    """ValueInverseLerp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueInverseLerpBlend(ValueInverseLerpBase):
    """ValueInverseLerp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueInverseLerpBlendMode(ValueInverseLerpBase):
    """ValueInverseLerp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueInverseLerpCulling(ValueInverseLerpBase):
    """ValueInverseLerp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueInverseLerpBodyNode(ValueInverseLerpBase):
    """ValueInverseLerp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueInverseLerpChirality(ValueInverseLerpBase):
    """ValueInverseLerp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueInverseLerpDummyEnum(ValueInverseLerpBase):
    """ValueInverseLerp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueInverseLerp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "from_": "From",
        "to": "To",
        "value": "Value",
    }

    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueInverseLerp variant
ValueInverseLerp = (
    ValueInverseLerpBool |
    ValueInverseLerpByte |
    ValueInverseLerpUshort |
    ValueInverseLerpUint |
    ValueInverseLerpUlong |
    ValueInverseLerpSbyte |
    ValueInverseLerpShort |
    ValueInverseLerpInt |
    ValueInverseLerpLong |
    ValueInverseLerpFloat |
    ValueInverseLerpDouble |
    ValueInverseLerpDecimal |
    ValueInverseLerpChar |
    ValueInverseLerpString |
    ValueInverseLerpUri |
    ValueInverseLerpBool2 |
    ValueInverseLerpByte2 |
    ValueInverseLerpUshort2 |
    ValueInverseLerpUint2 |
    ValueInverseLerpUlong2 |
    ValueInverseLerpSbyte2 |
    ValueInverseLerpShort2 |
    ValueInverseLerpInt2 |
    ValueInverseLerpLong2 |
    ValueInverseLerpFloat2 |
    ValueInverseLerpDouble2 |
    ValueInverseLerpBool3 |
    ValueInverseLerpByte3 |
    ValueInverseLerpUshort3 |
    ValueInverseLerpUint3 |
    ValueInverseLerpUlong3 |
    ValueInverseLerpSbyte3 |
    ValueInverseLerpShort3 |
    ValueInverseLerpInt3 |
    ValueInverseLerpLong3 |
    ValueInverseLerpFloat3 |
    ValueInverseLerpDouble3 |
    ValueInverseLerpBool4 |
    ValueInverseLerpByte4 |
    ValueInverseLerpUshort4 |
    ValueInverseLerpUint4 |
    ValueInverseLerpUlong4 |
    ValueInverseLerpSbyte4 |
    ValueInverseLerpShort4 |
    ValueInverseLerpInt4 |
    ValueInverseLerpLong4 |
    ValueInverseLerpFloat4 |
    ValueInverseLerpDouble4 |
    ValueInverseLerpFloat_2x2 |
    ValueInverseLerpDouble_2x2 |
    ValueInverseLerpFloat_3x3 |
    ValueInverseLerpDouble_3x3 |
    ValueInverseLerpFloat_4x4 |
    ValueInverseLerpDouble_4x4 |
    ValueInverseLerpFloatQ |
    ValueInverseLerpDoubleQ |
    ValueInverseLerpDateTime |
    ValueInverseLerpTimeSpan |
    ValueInverseLerpColor |
    ValueInverseLerpColorX |
    ValueInverseLerpShadowCastMode |
    ValueInverseLerpLightType |
    ValueInverseLerpSessionAccessLevel |
    ValueInverseLerpKey |
    ValueInverseLerpHttpStatusCode |
    ValueInverseLerpHeadOutputDevice |
    ValueInverseLerpReflectionProbeClear |
    ValueInverseLerpReflectionProbeType |
    ValueInverseLerpReflectionProbeTimeSlicingMode |
    ValueInverseLerpCameraClearMode |
    ValueInverseLerpCameraPositioningMode |
    ValueInverseLerpCameraProjection |
    ValueInverseLerpZWrite |
    ValueInverseLerpZTest |
    ValueInverseLerpBlend |
    ValueInverseLerpBlendMode |
    ValueInverseLerpCulling |
    ValueInverseLerpBodyNode |
    ValueInverseLerpChirality |
    ValueInverseLerpDummyEnum
)