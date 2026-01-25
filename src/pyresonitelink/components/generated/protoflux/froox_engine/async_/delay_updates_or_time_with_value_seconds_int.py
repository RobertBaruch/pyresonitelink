"""Generated component: DelayUpdatesOrTimeWithValueSecondsInt.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBase(GeneratedComponent):
    """Base class for DelayUpdatesOrTimeWithValueSecondsInt<T> variants."""

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
class DelayUpdatesOrTimeWithValueSecondsIntBool(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntByte(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUshort(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUint(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUlong(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntSbyte(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntShort(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntInt(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntLong(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDecimal(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntChar(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntString(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUri(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBool2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntByte2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUshort2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUint2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUlong2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntSbyte2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntShort2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntInt2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntLong2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBool3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntByte3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUshort3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUint3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUlong3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntSbyte3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntShort3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntInt3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntLong3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBool4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntByte4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUshort4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUint4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntUlong4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntSbyte4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntShort4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntInt4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntLong4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat_2x2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble_2x2(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat_3x3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble_3x3(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloat_4x4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDouble_4x4(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntFloatQ(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDoubleQ(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDateTime(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntTimeSpan(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntColor(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntColorX(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntShadowCastMode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntLightType(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntSessionAccessLevel(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntKey(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntHttpStatusCode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntHeadOutputDevice(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeClear(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeType(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeTimeSlicingMode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntCameraClearMode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntCameraPositioningMode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntCameraProjection(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntZWrite(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntZTest(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBlend(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBlendMode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntCulling(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntBodyNode(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntChirality(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsIntDummyEnum(DelayUpdatesOrTimeWithValueSecondsIntBase):
    """DelayUpdatesOrTimeWithValueSecondsInt<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsInt<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DelayUpdatesOrTimeWithValueSecondsInt variant
DelayUpdatesOrTimeWithValueSecondsInt = (
    DelayUpdatesOrTimeWithValueSecondsIntBool |
    DelayUpdatesOrTimeWithValueSecondsIntByte |
    DelayUpdatesOrTimeWithValueSecondsIntUshort |
    DelayUpdatesOrTimeWithValueSecondsIntUint |
    DelayUpdatesOrTimeWithValueSecondsIntUlong |
    DelayUpdatesOrTimeWithValueSecondsIntSbyte |
    DelayUpdatesOrTimeWithValueSecondsIntShort |
    DelayUpdatesOrTimeWithValueSecondsIntInt |
    DelayUpdatesOrTimeWithValueSecondsIntLong |
    DelayUpdatesOrTimeWithValueSecondsIntFloat |
    DelayUpdatesOrTimeWithValueSecondsIntDouble |
    DelayUpdatesOrTimeWithValueSecondsIntDecimal |
    DelayUpdatesOrTimeWithValueSecondsIntChar |
    DelayUpdatesOrTimeWithValueSecondsIntString |
    DelayUpdatesOrTimeWithValueSecondsIntUri |
    DelayUpdatesOrTimeWithValueSecondsIntBool2 |
    DelayUpdatesOrTimeWithValueSecondsIntByte2 |
    DelayUpdatesOrTimeWithValueSecondsIntUshort2 |
    DelayUpdatesOrTimeWithValueSecondsIntUint2 |
    DelayUpdatesOrTimeWithValueSecondsIntUlong2 |
    DelayUpdatesOrTimeWithValueSecondsIntSbyte2 |
    DelayUpdatesOrTimeWithValueSecondsIntShort2 |
    DelayUpdatesOrTimeWithValueSecondsIntInt2 |
    DelayUpdatesOrTimeWithValueSecondsIntLong2 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat2 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble2 |
    DelayUpdatesOrTimeWithValueSecondsIntBool3 |
    DelayUpdatesOrTimeWithValueSecondsIntByte3 |
    DelayUpdatesOrTimeWithValueSecondsIntUshort3 |
    DelayUpdatesOrTimeWithValueSecondsIntUint3 |
    DelayUpdatesOrTimeWithValueSecondsIntUlong3 |
    DelayUpdatesOrTimeWithValueSecondsIntSbyte3 |
    DelayUpdatesOrTimeWithValueSecondsIntShort3 |
    DelayUpdatesOrTimeWithValueSecondsIntInt3 |
    DelayUpdatesOrTimeWithValueSecondsIntLong3 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat3 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble3 |
    DelayUpdatesOrTimeWithValueSecondsIntBool4 |
    DelayUpdatesOrTimeWithValueSecondsIntByte4 |
    DelayUpdatesOrTimeWithValueSecondsIntUshort4 |
    DelayUpdatesOrTimeWithValueSecondsIntUint4 |
    DelayUpdatesOrTimeWithValueSecondsIntUlong4 |
    DelayUpdatesOrTimeWithValueSecondsIntSbyte4 |
    DelayUpdatesOrTimeWithValueSecondsIntShort4 |
    DelayUpdatesOrTimeWithValueSecondsIntInt4 |
    DelayUpdatesOrTimeWithValueSecondsIntLong4 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat4 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble4 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat_2x2 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble_2x2 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat_3x3 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble_3x3 |
    DelayUpdatesOrTimeWithValueSecondsIntFloat_4x4 |
    DelayUpdatesOrTimeWithValueSecondsIntDouble_4x4 |
    DelayUpdatesOrTimeWithValueSecondsIntFloatQ |
    DelayUpdatesOrTimeWithValueSecondsIntDoubleQ |
    DelayUpdatesOrTimeWithValueSecondsIntDateTime |
    DelayUpdatesOrTimeWithValueSecondsIntTimeSpan |
    DelayUpdatesOrTimeWithValueSecondsIntColor |
    DelayUpdatesOrTimeWithValueSecondsIntColorX |
    DelayUpdatesOrTimeWithValueSecondsIntShadowCastMode |
    DelayUpdatesOrTimeWithValueSecondsIntLightType |
    DelayUpdatesOrTimeWithValueSecondsIntSessionAccessLevel |
    DelayUpdatesOrTimeWithValueSecondsIntKey |
    DelayUpdatesOrTimeWithValueSecondsIntHttpStatusCode |
    DelayUpdatesOrTimeWithValueSecondsIntHeadOutputDevice |
    DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeClear |
    DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeType |
    DelayUpdatesOrTimeWithValueSecondsIntReflectionProbeTimeSlicingMode |
    DelayUpdatesOrTimeWithValueSecondsIntCameraClearMode |
    DelayUpdatesOrTimeWithValueSecondsIntCameraPositioningMode |
    DelayUpdatesOrTimeWithValueSecondsIntCameraProjection |
    DelayUpdatesOrTimeWithValueSecondsIntZWrite |
    DelayUpdatesOrTimeWithValueSecondsIntZTest |
    DelayUpdatesOrTimeWithValueSecondsIntBlend |
    DelayUpdatesOrTimeWithValueSecondsIntBlendMode |
    DelayUpdatesOrTimeWithValueSecondsIntCulling |
    DelayUpdatesOrTimeWithValueSecondsIntBodyNode |
    DelayUpdatesOrTimeWithValueSecondsIntChirality |
    DelayUpdatesOrTimeWithValueSecondsIntDummyEnum
)