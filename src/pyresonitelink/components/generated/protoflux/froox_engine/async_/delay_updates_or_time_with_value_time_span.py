"""Generated component: DelayUpdatesOrTimeWithValueTimeSpan.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBase(GeneratedComponent):
    """Base class for DelayUpdatesOrTimeWithValueTimeSpan<T> variants."""

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
class DelayUpdatesOrTimeWithValueTimeSpanBool(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanByte(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUshort(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUint(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUlong(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanSbyte(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanShort(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanInt(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanLong(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDecimal(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanChar(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanString(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUri(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBool2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanByte2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUshort2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUint2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUlong2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanSbyte2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanShort2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanInt2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanLong2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBool3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanByte3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUshort3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUint3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUlong3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanSbyte3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanShort3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanInt3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanLong3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBool4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanByte4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUshort4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUint4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanUlong4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanSbyte4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanShort4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanInt4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanLong4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat_2x2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble_2x2(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat_3x3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble_3x3(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloat_4x4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDouble_4x4(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanFloatQ(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDoubleQ(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDateTime(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanTimeSpan(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanColor(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanColorX(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanShadowCastMode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanLightType(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanSessionAccessLevel(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanKey(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanHttpStatusCode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanHeadOutputDevice(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeClear(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeType(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeTimeSlicingMode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanCameraClearMode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanCameraPositioningMode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanCameraProjection(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanZWrite(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanZTest(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBlend(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBlendMode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanCulling(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanBodyNode(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanChirality(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DelayUpdatesOrTimeWithValueTimeSpanDummyEnum(DelayUpdatesOrTimeWithValueTimeSpanBase):
    """DelayUpdatesOrTimeWithValueTimeSpan<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueTimeSpan<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DelayUpdatesOrTimeWithValueTimeSpan variant
DelayUpdatesOrTimeWithValueTimeSpan = (
    DelayUpdatesOrTimeWithValueTimeSpanBool |
    DelayUpdatesOrTimeWithValueTimeSpanByte |
    DelayUpdatesOrTimeWithValueTimeSpanUshort |
    DelayUpdatesOrTimeWithValueTimeSpanUint |
    DelayUpdatesOrTimeWithValueTimeSpanUlong |
    DelayUpdatesOrTimeWithValueTimeSpanSbyte |
    DelayUpdatesOrTimeWithValueTimeSpanShort |
    DelayUpdatesOrTimeWithValueTimeSpanInt |
    DelayUpdatesOrTimeWithValueTimeSpanLong |
    DelayUpdatesOrTimeWithValueTimeSpanFloat |
    DelayUpdatesOrTimeWithValueTimeSpanDouble |
    DelayUpdatesOrTimeWithValueTimeSpanDecimal |
    DelayUpdatesOrTimeWithValueTimeSpanChar |
    DelayUpdatesOrTimeWithValueTimeSpanString |
    DelayUpdatesOrTimeWithValueTimeSpanUri |
    DelayUpdatesOrTimeWithValueTimeSpanBool2 |
    DelayUpdatesOrTimeWithValueTimeSpanByte2 |
    DelayUpdatesOrTimeWithValueTimeSpanUshort2 |
    DelayUpdatesOrTimeWithValueTimeSpanUint2 |
    DelayUpdatesOrTimeWithValueTimeSpanUlong2 |
    DelayUpdatesOrTimeWithValueTimeSpanSbyte2 |
    DelayUpdatesOrTimeWithValueTimeSpanShort2 |
    DelayUpdatesOrTimeWithValueTimeSpanInt2 |
    DelayUpdatesOrTimeWithValueTimeSpanLong2 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat2 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble2 |
    DelayUpdatesOrTimeWithValueTimeSpanBool3 |
    DelayUpdatesOrTimeWithValueTimeSpanByte3 |
    DelayUpdatesOrTimeWithValueTimeSpanUshort3 |
    DelayUpdatesOrTimeWithValueTimeSpanUint3 |
    DelayUpdatesOrTimeWithValueTimeSpanUlong3 |
    DelayUpdatesOrTimeWithValueTimeSpanSbyte3 |
    DelayUpdatesOrTimeWithValueTimeSpanShort3 |
    DelayUpdatesOrTimeWithValueTimeSpanInt3 |
    DelayUpdatesOrTimeWithValueTimeSpanLong3 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat3 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble3 |
    DelayUpdatesOrTimeWithValueTimeSpanBool4 |
    DelayUpdatesOrTimeWithValueTimeSpanByte4 |
    DelayUpdatesOrTimeWithValueTimeSpanUshort4 |
    DelayUpdatesOrTimeWithValueTimeSpanUint4 |
    DelayUpdatesOrTimeWithValueTimeSpanUlong4 |
    DelayUpdatesOrTimeWithValueTimeSpanSbyte4 |
    DelayUpdatesOrTimeWithValueTimeSpanShort4 |
    DelayUpdatesOrTimeWithValueTimeSpanInt4 |
    DelayUpdatesOrTimeWithValueTimeSpanLong4 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat4 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble4 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat_2x2 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble_2x2 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat_3x3 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble_3x3 |
    DelayUpdatesOrTimeWithValueTimeSpanFloat_4x4 |
    DelayUpdatesOrTimeWithValueTimeSpanDouble_4x4 |
    DelayUpdatesOrTimeWithValueTimeSpanFloatQ |
    DelayUpdatesOrTimeWithValueTimeSpanDoubleQ |
    DelayUpdatesOrTimeWithValueTimeSpanDateTime |
    DelayUpdatesOrTimeWithValueTimeSpanTimeSpan |
    DelayUpdatesOrTimeWithValueTimeSpanColor |
    DelayUpdatesOrTimeWithValueTimeSpanColorX |
    DelayUpdatesOrTimeWithValueTimeSpanShadowCastMode |
    DelayUpdatesOrTimeWithValueTimeSpanLightType |
    DelayUpdatesOrTimeWithValueTimeSpanSessionAccessLevel |
    DelayUpdatesOrTimeWithValueTimeSpanKey |
    DelayUpdatesOrTimeWithValueTimeSpanHttpStatusCode |
    DelayUpdatesOrTimeWithValueTimeSpanHeadOutputDevice |
    DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeClear |
    DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeType |
    DelayUpdatesOrTimeWithValueTimeSpanReflectionProbeTimeSlicingMode |
    DelayUpdatesOrTimeWithValueTimeSpanCameraClearMode |
    DelayUpdatesOrTimeWithValueTimeSpanCameraPositioningMode |
    DelayUpdatesOrTimeWithValueTimeSpanCameraProjection |
    DelayUpdatesOrTimeWithValueTimeSpanZWrite |
    DelayUpdatesOrTimeWithValueTimeSpanZTest |
    DelayUpdatesOrTimeWithValueTimeSpanBlend |
    DelayUpdatesOrTimeWithValueTimeSpanBlendMode |
    DelayUpdatesOrTimeWithValueTimeSpanCulling |
    DelayUpdatesOrTimeWithValueTimeSpanBodyNode |
    DelayUpdatesOrTimeWithValueTimeSpanChirality |
    DelayUpdatesOrTimeWithValueTimeSpanDummyEnum
)