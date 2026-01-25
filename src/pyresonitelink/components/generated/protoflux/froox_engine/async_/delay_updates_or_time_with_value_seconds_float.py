"""Generated component: DelayUpdatesOrTimeWithValueSecondsFloat.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBase(GeneratedComponent):
    """Base class for DelayUpdatesOrTimeWithValueSecondsFloat<T> variants."""

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
class DelayUpdatesOrTimeWithValueSecondsFloatBool(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatByte(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUshort(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUint(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUlong(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatSbyte(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatShort(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatInt(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatLong(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDecimal(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatChar(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatString(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUri(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBool2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatByte2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUshort2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUint2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUlong2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatSbyte2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatShort2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatInt2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatLong2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBool3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatByte3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUshort3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUint3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUlong3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatSbyte3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatShort3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatInt3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatLong3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBool4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatByte4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUshort4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUint4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatUlong4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatSbyte4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatShort4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatInt4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatLong4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat_2x2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble_2x2(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat_3x3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble_3x3(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloat_4x4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDouble_4x4(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatFloatQ(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDoubleQ(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDateTime(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatTimeSpan(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatColor(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatColorX(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatShadowCastMode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatLightType(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatSessionAccessLevel(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatKey(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatHttpStatusCode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatHeadOutputDevice(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeClear(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeType(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeTimeSlicingMode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatCameraClearMode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatCameraPositioningMode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatCameraProjection(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatZWrite(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatZTest(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBlend(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBlendMode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatCulling(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatBodyNode(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatChirality(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DelayUpdatesOrTimeWithValueSecondsFloatDummyEnum(DelayUpdatesOrTimeWithValueSecondsFloatBase):
    """DelayUpdatesOrTimeWithValueSecondsFloat<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithValueSecondsFloat<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "updates": "Updates",
        "value": "Value",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    updates: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DelayUpdatesOrTimeWithValueSecondsFloat variant
DelayUpdatesOrTimeWithValueSecondsFloat = (
    DelayUpdatesOrTimeWithValueSecondsFloatBool |
    DelayUpdatesOrTimeWithValueSecondsFloatByte |
    DelayUpdatesOrTimeWithValueSecondsFloatUshort |
    DelayUpdatesOrTimeWithValueSecondsFloatUint |
    DelayUpdatesOrTimeWithValueSecondsFloatUlong |
    DelayUpdatesOrTimeWithValueSecondsFloatSbyte |
    DelayUpdatesOrTimeWithValueSecondsFloatShort |
    DelayUpdatesOrTimeWithValueSecondsFloatInt |
    DelayUpdatesOrTimeWithValueSecondsFloatLong |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble |
    DelayUpdatesOrTimeWithValueSecondsFloatDecimal |
    DelayUpdatesOrTimeWithValueSecondsFloatChar |
    DelayUpdatesOrTimeWithValueSecondsFloatString |
    DelayUpdatesOrTimeWithValueSecondsFloatUri |
    DelayUpdatesOrTimeWithValueSecondsFloatBool2 |
    DelayUpdatesOrTimeWithValueSecondsFloatByte2 |
    DelayUpdatesOrTimeWithValueSecondsFloatUshort2 |
    DelayUpdatesOrTimeWithValueSecondsFloatUint2 |
    DelayUpdatesOrTimeWithValueSecondsFloatUlong2 |
    DelayUpdatesOrTimeWithValueSecondsFloatSbyte2 |
    DelayUpdatesOrTimeWithValueSecondsFloatShort2 |
    DelayUpdatesOrTimeWithValueSecondsFloatInt2 |
    DelayUpdatesOrTimeWithValueSecondsFloatLong2 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat2 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble2 |
    DelayUpdatesOrTimeWithValueSecondsFloatBool3 |
    DelayUpdatesOrTimeWithValueSecondsFloatByte3 |
    DelayUpdatesOrTimeWithValueSecondsFloatUshort3 |
    DelayUpdatesOrTimeWithValueSecondsFloatUint3 |
    DelayUpdatesOrTimeWithValueSecondsFloatUlong3 |
    DelayUpdatesOrTimeWithValueSecondsFloatSbyte3 |
    DelayUpdatesOrTimeWithValueSecondsFloatShort3 |
    DelayUpdatesOrTimeWithValueSecondsFloatInt3 |
    DelayUpdatesOrTimeWithValueSecondsFloatLong3 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat3 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble3 |
    DelayUpdatesOrTimeWithValueSecondsFloatBool4 |
    DelayUpdatesOrTimeWithValueSecondsFloatByte4 |
    DelayUpdatesOrTimeWithValueSecondsFloatUshort4 |
    DelayUpdatesOrTimeWithValueSecondsFloatUint4 |
    DelayUpdatesOrTimeWithValueSecondsFloatUlong4 |
    DelayUpdatesOrTimeWithValueSecondsFloatSbyte4 |
    DelayUpdatesOrTimeWithValueSecondsFloatShort4 |
    DelayUpdatesOrTimeWithValueSecondsFloatInt4 |
    DelayUpdatesOrTimeWithValueSecondsFloatLong4 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat4 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble4 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat_2x2 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble_2x2 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat_3x3 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble_3x3 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloat_4x4 |
    DelayUpdatesOrTimeWithValueSecondsFloatDouble_4x4 |
    DelayUpdatesOrTimeWithValueSecondsFloatFloatQ |
    DelayUpdatesOrTimeWithValueSecondsFloatDoubleQ |
    DelayUpdatesOrTimeWithValueSecondsFloatDateTime |
    DelayUpdatesOrTimeWithValueSecondsFloatTimeSpan |
    DelayUpdatesOrTimeWithValueSecondsFloatColor |
    DelayUpdatesOrTimeWithValueSecondsFloatColorX |
    DelayUpdatesOrTimeWithValueSecondsFloatShadowCastMode |
    DelayUpdatesOrTimeWithValueSecondsFloatLightType |
    DelayUpdatesOrTimeWithValueSecondsFloatSessionAccessLevel |
    DelayUpdatesOrTimeWithValueSecondsFloatKey |
    DelayUpdatesOrTimeWithValueSecondsFloatHttpStatusCode |
    DelayUpdatesOrTimeWithValueSecondsFloatHeadOutputDevice |
    DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeClear |
    DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeType |
    DelayUpdatesOrTimeWithValueSecondsFloatReflectionProbeTimeSlicingMode |
    DelayUpdatesOrTimeWithValueSecondsFloatCameraClearMode |
    DelayUpdatesOrTimeWithValueSecondsFloatCameraPositioningMode |
    DelayUpdatesOrTimeWithValueSecondsFloatCameraProjection |
    DelayUpdatesOrTimeWithValueSecondsFloatZWrite |
    DelayUpdatesOrTimeWithValueSecondsFloatZTest |
    DelayUpdatesOrTimeWithValueSecondsFloatBlend |
    DelayUpdatesOrTimeWithValueSecondsFloatBlendMode |
    DelayUpdatesOrTimeWithValueSecondsFloatCulling |
    DelayUpdatesOrTimeWithValueSecondsFloatBodyNode |
    DelayUpdatesOrTimeWithValueSecondsFloatChirality |
    DelayUpdatesOrTimeWithValueSecondsFloatDummyEnum
)