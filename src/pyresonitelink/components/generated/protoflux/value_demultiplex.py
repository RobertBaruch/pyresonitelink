"""Generated component: ValueDemultiplex.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class ValueDemultiplexBase(GeneratedComponent):
    """Base class for ValueDemultiplex<T> variants."""

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
class ValueDemultiplexBool(ValueDemultiplexBase):
    """ValueDemultiplex<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexByte(ValueDemultiplexBase):
    """ValueDemultiplex<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUshort(ValueDemultiplexBase):
    """ValueDemultiplex<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUint(ValueDemultiplexBase):
    """ValueDemultiplex<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUlong(ValueDemultiplexBase):
    """ValueDemultiplex<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexSbyte(ValueDemultiplexBase):
    """ValueDemultiplex<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexShort(ValueDemultiplexBase):
    """ValueDemultiplex<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexInt(ValueDemultiplexBase):
    """ValueDemultiplex<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexLong(ValueDemultiplexBase):
    """ValueDemultiplex<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat(ValueDemultiplexBase):
    """ValueDemultiplex<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble(ValueDemultiplexBase):
    """ValueDemultiplex<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDecimal(ValueDemultiplexBase):
    """ValueDemultiplex<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexChar(ValueDemultiplexBase):
    """ValueDemultiplex<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexString(ValueDemultiplexBase):
    """ValueDemultiplex<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUri(ValueDemultiplexBase):
    """ValueDemultiplex<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBool2(ValueDemultiplexBase):
    """ValueDemultiplex<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexByte2(ValueDemultiplexBase):
    """ValueDemultiplex<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUshort2(ValueDemultiplexBase):
    """ValueDemultiplex<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUint2(ValueDemultiplexBase):
    """ValueDemultiplex<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUlong2(ValueDemultiplexBase):
    """ValueDemultiplex<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexSbyte2(ValueDemultiplexBase):
    """ValueDemultiplex<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexShort2(ValueDemultiplexBase):
    """ValueDemultiplex<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexInt2(ValueDemultiplexBase):
    """ValueDemultiplex<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexLong2(ValueDemultiplexBase):
    """ValueDemultiplex<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat2(ValueDemultiplexBase):
    """ValueDemultiplex<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble2(ValueDemultiplexBase):
    """ValueDemultiplex<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBool3(ValueDemultiplexBase):
    """ValueDemultiplex<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexByte3(ValueDemultiplexBase):
    """ValueDemultiplex<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUshort3(ValueDemultiplexBase):
    """ValueDemultiplex<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUint3(ValueDemultiplexBase):
    """ValueDemultiplex<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUlong3(ValueDemultiplexBase):
    """ValueDemultiplex<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexSbyte3(ValueDemultiplexBase):
    """ValueDemultiplex<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexShort3(ValueDemultiplexBase):
    """ValueDemultiplex<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexInt3(ValueDemultiplexBase):
    """ValueDemultiplex<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexLong3(ValueDemultiplexBase):
    """ValueDemultiplex<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat3(ValueDemultiplexBase):
    """ValueDemultiplex<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble3(ValueDemultiplexBase):
    """ValueDemultiplex<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBool4(ValueDemultiplexBase):
    """ValueDemultiplex<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexByte4(ValueDemultiplexBase):
    """ValueDemultiplex<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUshort4(ValueDemultiplexBase):
    """ValueDemultiplex<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUint4(ValueDemultiplexBase):
    """ValueDemultiplex<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexUlong4(ValueDemultiplexBase):
    """ValueDemultiplex<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexSbyte4(ValueDemultiplexBase):
    """ValueDemultiplex<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexShort4(ValueDemultiplexBase):
    """ValueDemultiplex<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexInt4(ValueDemultiplexBase):
    """ValueDemultiplex<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexLong4(ValueDemultiplexBase):
    """ValueDemultiplex<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat4(ValueDemultiplexBase):
    """ValueDemultiplex<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble4(ValueDemultiplexBase):
    """ValueDemultiplex<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat_2x2(ValueDemultiplexBase):
    """ValueDemultiplex<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble_2x2(ValueDemultiplexBase):
    """ValueDemultiplex<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat_3x3(ValueDemultiplexBase):
    """ValueDemultiplex<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble_3x3(ValueDemultiplexBase):
    """ValueDemultiplex<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloat_4x4(ValueDemultiplexBase):
    """ValueDemultiplex<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDouble_4x4(ValueDemultiplexBase):
    """ValueDemultiplex<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexFloatQ(ValueDemultiplexBase):
    """ValueDemultiplex<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDoubleQ(ValueDemultiplexBase):
    """ValueDemultiplex<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDateTime(ValueDemultiplexBase):
    """ValueDemultiplex<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexTimeSpan(ValueDemultiplexBase):
    """ValueDemultiplex<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexColor(ValueDemultiplexBase):
    """ValueDemultiplex<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexColorX(ValueDemultiplexBase):
    """ValueDemultiplex<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexShadowCastMode(ValueDemultiplexBase):
    """ValueDemultiplex<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexLightType(ValueDemultiplexBase):
    """ValueDemultiplex<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexSessionAccessLevel(ValueDemultiplexBase):
    """ValueDemultiplex<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexKey(ValueDemultiplexBase):
    """ValueDemultiplex<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexHttpStatusCode(ValueDemultiplexBase):
    """ValueDemultiplex<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexHeadOutputDevice(ValueDemultiplexBase):
    """ValueDemultiplex<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexReflectionProbeClear(ValueDemultiplexBase):
    """ValueDemultiplex<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexReflectionProbeType(ValueDemultiplexBase):
    """ValueDemultiplex<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexReflectionProbeTimeSlicingMode(ValueDemultiplexBase):
    """ValueDemultiplex<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexCameraClearMode(ValueDemultiplexBase):
    """ValueDemultiplex<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexCameraPositioningMode(ValueDemultiplexBase):
    """ValueDemultiplex<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexCameraProjection(ValueDemultiplexBase):
    """ValueDemultiplex<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexZWrite(ValueDemultiplexBase):
    """ValueDemultiplex<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexZTest(ValueDemultiplexBase):
    """ValueDemultiplex<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBlend(ValueDemultiplexBase):
    """ValueDemultiplex<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBlendMode(ValueDemultiplexBase):
    """ValueDemultiplex<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexCulling(ValueDemultiplexBase):
    """ValueDemultiplex<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexBodyNode(ValueDemultiplexBase):
    """ValueDemultiplex<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexChirality(ValueDemultiplexBase):
    """ValueDemultiplex<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    value_outputs: SyncList | None = None


@dataclass
class ValueDemultiplexDummyEnum(ValueDemultiplexBase):
    """ValueDemultiplex<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueDemultiplex<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "index": "Index",
        "value": "Value",
        "value_outputs": "ValueOutputs",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    value_outputs: SyncList | None = None


# Type alias for any ValueDemultiplex variant
ValueDemultiplex = (
    ValueDemultiplexBool |
    ValueDemultiplexByte |
    ValueDemultiplexUshort |
    ValueDemultiplexUint |
    ValueDemultiplexUlong |
    ValueDemultiplexSbyte |
    ValueDemultiplexShort |
    ValueDemultiplexInt |
    ValueDemultiplexLong |
    ValueDemultiplexFloat |
    ValueDemultiplexDouble |
    ValueDemultiplexDecimal |
    ValueDemultiplexChar |
    ValueDemultiplexString |
    ValueDemultiplexUri |
    ValueDemultiplexBool2 |
    ValueDemultiplexByte2 |
    ValueDemultiplexUshort2 |
    ValueDemultiplexUint2 |
    ValueDemultiplexUlong2 |
    ValueDemultiplexSbyte2 |
    ValueDemultiplexShort2 |
    ValueDemultiplexInt2 |
    ValueDemultiplexLong2 |
    ValueDemultiplexFloat2 |
    ValueDemultiplexDouble2 |
    ValueDemultiplexBool3 |
    ValueDemultiplexByte3 |
    ValueDemultiplexUshort3 |
    ValueDemultiplexUint3 |
    ValueDemultiplexUlong3 |
    ValueDemultiplexSbyte3 |
    ValueDemultiplexShort3 |
    ValueDemultiplexInt3 |
    ValueDemultiplexLong3 |
    ValueDemultiplexFloat3 |
    ValueDemultiplexDouble3 |
    ValueDemultiplexBool4 |
    ValueDemultiplexByte4 |
    ValueDemultiplexUshort4 |
    ValueDemultiplexUint4 |
    ValueDemultiplexUlong4 |
    ValueDemultiplexSbyte4 |
    ValueDemultiplexShort4 |
    ValueDemultiplexInt4 |
    ValueDemultiplexLong4 |
    ValueDemultiplexFloat4 |
    ValueDemultiplexDouble4 |
    ValueDemultiplexFloat_2x2 |
    ValueDemultiplexDouble_2x2 |
    ValueDemultiplexFloat_3x3 |
    ValueDemultiplexDouble_3x3 |
    ValueDemultiplexFloat_4x4 |
    ValueDemultiplexDouble_4x4 |
    ValueDemultiplexFloatQ |
    ValueDemultiplexDoubleQ |
    ValueDemultiplexDateTime |
    ValueDemultiplexTimeSpan |
    ValueDemultiplexColor |
    ValueDemultiplexColorX |
    ValueDemultiplexShadowCastMode |
    ValueDemultiplexLightType |
    ValueDemultiplexSessionAccessLevel |
    ValueDemultiplexKey |
    ValueDemultiplexHttpStatusCode |
    ValueDemultiplexHeadOutputDevice |
    ValueDemultiplexReflectionProbeClear |
    ValueDemultiplexReflectionProbeType |
    ValueDemultiplexReflectionProbeTimeSlicingMode |
    ValueDemultiplexCameraClearMode |
    ValueDemultiplexCameraPositioningMode |
    ValueDemultiplexCameraProjection |
    ValueDemultiplexZWrite |
    ValueDemultiplexZTest |
    ValueDemultiplexBlend |
    ValueDemultiplexBlendMode |
    ValueDemultiplexCulling |
    ValueDemultiplexBodyNode |
    ValueDemultiplexChirality |
    ValueDemultiplexDummyEnum
)