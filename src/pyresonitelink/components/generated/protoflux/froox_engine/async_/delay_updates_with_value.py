"""Generated component: DelayUpdatesWithValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelayUpdatesWithValueBase(GeneratedComponent):
    """Base class for DelayUpdatesWithValue<T> variants."""

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
class DelayUpdatesWithValueBool(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DelayUpdatesWithValueByte(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DelayUpdatesWithValueUshort(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DelayUpdatesWithValueUint(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DelayUpdatesWithValueUlong(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DelayUpdatesWithValueSbyte(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DelayUpdatesWithValueShort(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DelayUpdatesWithValueInt(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DelayUpdatesWithValueLong(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DelayUpdatesWithValueFloat(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DelayUpdatesWithValueDouble(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DelayUpdatesWithValueDecimal(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DelayUpdatesWithValueChar(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DelayUpdatesWithValueString(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DelayUpdatesWithValueUri(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DelayUpdatesWithValueBool2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DelayUpdatesWithValueByte2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DelayUpdatesWithValueUshort2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DelayUpdatesWithValueUint2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DelayUpdatesWithValueUlong2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DelayUpdatesWithValueSbyte2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DelayUpdatesWithValueShort2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DelayUpdatesWithValueInt2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DelayUpdatesWithValueLong2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DelayUpdatesWithValueFloat2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DelayUpdatesWithValueDouble2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DelayUpdatesWithValueBool3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DelayUpdatesWithValueByte3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DelayUpdatesWithValueUshort3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DelayUpdatesWithValueUint3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DelayUpdatesWithValueUlong3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DelayUpdatesWithValueSbyte3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DelayUpdatesWithValueShort3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DelayUpdatesWithValueInt3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DelayUpdatesWithValueLong3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DelayUpdatesWithValueFloat3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DelayUpdatesWithValueDouble3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DelayUpdatesWithValueBool4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DelayUpdatesWithValueByte4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DelayUpdatesWithValueUshort4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DelayUpdatesWithValueUint4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DelayUpdatesWithValueUlong4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DelayUpdatesWithValueSbyte4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DelayUpdatesWithValueShort4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DelayUpdatesWithValueInt4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DelayUpdatesWithValueLong4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DelayUpdatesWithValueFloat4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DelayUpdatesWithValueDouble4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DelayUpdatesWithValueFloat_2x2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DelayUpdatesWithValueDouble_2x2(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DelayUpdatesWithValueFloat_3x3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DelayUpdatesWithValueDouble_3x3(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DelayUpdatesWithValueFloat_4x4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DelayUpdatesWithValueDouble_4x4(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DelayUpdatesWithValueFloatQ(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DelayUpdatesWithValueDoubleQ(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DelayUpdatesWithValueDateTime(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DelayUpdatesWithValueTimeSpan(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DelayUpdatesWithValueColor(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DelayUpdatesWithValueColorX(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DelayUpdatesWithValueShadowCastMode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DelayUpdatesWithValueLightType(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DelayUpdatesWithValueSessionAccessLevel(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DelayUpdatesWithValueKey(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DelayUpdatesWithValueHttpStatusCode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DelayUpdatesWithValueHeadOutputDevice(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DelayUpdatesWithValueReflectionProbeClear(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DelayUpdatesWithValueReflectionProbeType(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DelayUpdatesWithValueReflectionProbeTimeSlicingMode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DelayUpdatesWithValueCameraClearMode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DelayUpdatesWithValueCameraPositioningMode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DelayUpdatesWithValueCameraProjection(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DelayUpdatesWithValueZWrite(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DelayUpdatesWithValueZTest(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DelayUpdatesWithValueBlend(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DelayUpdatesWithValueBlendMode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DelayUpdatesWithValueCulling(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DelayUpdatesWithValueBodyNode(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DelayUpdatesWithValueChirality(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DelayUpdatesWithValueDummyEnum(DelayUpdatesWithValueBase):
    """DelayUpdatesWithValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesWithValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DelayUpdatesWithValue variant
DelayUpdatesWithValue = (
    DelayUpdatesWithValueBool |
    DelayUpdatesWithValueByte |
    DelayUpdatesWithValueUshort |
    DelayUpdatesWithValueUint |
    DelayUpdatesWithValueUlong |
    DelayUpdatesWithValueSbyte |
    DelayUpdatesWithValueShort |
    DelayUpdatesWithValueInt |
    DelayUpdatesWithValueLong |
    DelayUpdatesWithValueFloat |
    DelayUpdatesWithValueDouble |
    DelayUpdatesWithValueDecimal |
    DelayUpdatesWithValueChar |
    DelayUpdatesWithValueString |
    DelayUpdatesWithValueUri |
    DelayUpdatesWithValueBool2 |
    DelayUpdatesWithValueByte2 |
    DelayUpdatesWithValueUshort2 |
    DelayUpdatesWithValueUint2 |
    DelayUpdatesWithValueUlong2 |
    DelayUpdatesWithValueSbyte2 |
    DelayUpdatesWithValueShort2 |
    DelayUpdatesWithValueInt2 |
    DelayUpdatesWithValueLong2 |
    DelayUpdatesWithValueFloat2 |
    DelayUpdatesWithValueDouble2 |
    DelayUpdatesWithValueBool3 |
    DelayUpdatesWithValueByte3 |
    DelayUpdatesWithValueUshort3 |
    DelayUpdatesWithValueUint3 |
    DelayUpdatesWithValueUlong3 |
    DelayUpdatesWithValueSbyte3 |
    DelayUpdatesWithValueShort3 |
    DelayUpdatesWithValueInt3 |
    DelayUpdatesWithValueLong3 |
    DelayUpdatesWithValueFloat3 |
    DelayUpdatesWithValueDouble3 |
    DelayUpdatesWithValueBool4 |
    DelayUpdatesWithValueByte4 |
    DelayUpdatesWithValueUshort4 |
    DelayUpdatesWithValueUint4 |
    DelayUpdatesWithValueUlong4 |
    DelayUpdatesWithValueSbyte4 |
    DelayUpdatesWithValueShort4 |
    DelayUpdatesWithValueInt4 |
    DelayUpdatesWithValueLong4 |
    DelayUpdatesWithValueFloat4 |
    DelayUpdatesWithValueDouble4 |
    DelayUpdatesWithValueFloat_2x2 |
    DelayUpdatesWithValueDouble_2x2 |
    DelayUpdatesWithValueFloat_3x3 |
    DelayUpdatesWithValueDouble_3x3 |
    DelayUpdatesWithValueFloat_4x4 |
    DelayUpdatesWithValueDouble_4x4 |
    DelayUpdatesWithValueFloatQ |
    DelayUpdatesWithValueDoubleQ |
    DelayUpdatesWithValueDateTime |
    DelayUpdatesWithValueTimeSpan |
    DelayUpdatesWithValueColor |
    DelayUpdatesWithValueColorX |
    DelayUpdatesWithValueShadowCastMode |
    DelayUpdatesWithValueLightType |
    DelayUpdatesWithValueSessionAccessLevel |
    DelayUpdatesWithValueKey |
    DelayUpdatesWithValueHttpStatusCode |
    DelayUpdatesWithValueHeadOutputDevice |
    DelayUpdatesWithValueReflectionProbeClear |
    DelayUpdatesWithValueReflectionProbeType |
    DelayUpdatesWithValueReflectionProbeTimeSlicingMode |
    DelayUpdatesWithValueCameraClearMode |
    DelayUpdatesWithValueCameraPositioningMode |
    DelayUpdatesWithValueCameraProjection |
    DelayUpdatesWithValueZWrite |
    DelayUpdatesWithValueZTest |
    DelayUpdatesWithValueBlend |
    DelayUpdatesWithValueBlendMode |
    DelayUpdatesWithValueCulling |
    DelayUpdatesWithValueBodyNode |
    DelayUpdatesWithValueChirality |
    DelayUpdatesWithValueDummyEnum
)