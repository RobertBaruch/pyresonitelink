"""Generated component: TweenValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TweenValueBase(GeneratedComponent):
    """Base class for TweenValue<T> variants."""

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
class TweenValueBool(TweenValueBase):
    """TweenValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<bool>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class TweenValueByte(TweenValueBase):
    """TweenValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<byte>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class TweenValueUshort(TweenValueBase):
    """TweenValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ushort>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class TweenValueUint(TweenValueBase):
    """TweenValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<uint>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TweenValueUlong(TweenValueBase):
    """TweenValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ulong>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class TweenValueSbyte(TweenValueBase):
    """TweenValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<sbyte>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class TweenValueShort(TweenValueBase):
    """TweenValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<short>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class TweenValueInt(TweenValueBase):
    """TweenValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<int>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TweenValueLong(TweenValueBase):
    """TweenValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<long>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TweenValueFloat(TweenValueBase):
    """TweenValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class TweenValueDouble(TweenValueBase):
    """TweenValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class TweenValueDecimal(TweenValueBase):
    """TweenValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<decimal>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class TweenValueChar(TweenValueBase):
    """TweenValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<char>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class TweenValueString(TweenValueBase):
    """TweenValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<string>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class TweenValueUri(TweenValueBase):
    """TweenValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<Uri>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class TweenValueBool2(TweenValueBase):
    """TweenValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<bool2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class TweenValueByte2(TweenValueBase):
    """TweenValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<byte2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class TweenValueUshort2(TweenValueBase):
    """TweenValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ushort2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class TweenValueUint2(TweenValueBase):
    """TweenValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<uint2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class TweenValueUlong2(TweenValueBase):
    """TweenValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ulong2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class TweenValueSbyte2(TweenValueBase):
    """TweenValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<sbyte2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class TweenValueShort2(TweenValueBase):
    """TweenValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<short2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class TweenValueInt2(TweenValueBase):
    """TweenValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<int2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class TweenValueLong2(TweenValueBase):
    """TweenValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<long2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class TweenValueFloat2(TweenValueBase):
    """TweenValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class TweenValueDouble2(TweenValueBase):
    """TweenValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class TweenValueBool3(TweenValueBase):
    """TweenValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<bool3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class TweenValueByte3(TweenValueBase):
    """TweenValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<byte3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class TweenValueUshort3(TweenValueBase):
    """TweenValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ushort3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class TweenValueUint3(TweenValueBase):
    """TweenValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<uint3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class TweenValueUlong3(TweenValueBase):
    """TweenValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ulong3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class TweenValueSbyte3(TweenValueBase):
    """TweenValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<sbyte3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class TweenValueShort3(TweenValueBase):
    """TweenValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<short3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class TweenValueInt3(TweenValueBase):
    """TweenValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<int3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class TweenValueLong3(TweenValueBase):
    """TweenValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<long3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class TweenValueFloat3(TweenValueBase):
    """TweenValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class TweenValueDouble3(TweenValueBase):
    """TweenValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class TweenValueBool4(TweenValueBase):
    """TweenValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<bool4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class TweenValueByte4(TweenValueBase):
    """TweenValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<byte4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class TweenValueUshort4(TweenValueBase):
    """TweenValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ushort4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class TweenValueUint4(TweenValueBase):
    """TweenValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<uint4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class TweenValueUlong4(TweenValueBase):
    """TweenValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<ulong4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class TweenValueSbyte4(TweenValueBase):
    """TweenValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<sbyte4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class TweenValueShort4(TweenValueBase):
    """TweenValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<short4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class TweenValueInt4(TweenValueBase):
    """TweenValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<int4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class TweenValueLong4(TweenValueBase):
    """TweenValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<long4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class TweenValueFloat4(TweenValueBase):
    """TweenValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class TweenValueDouble4(TweenValueBase):
    """TweenValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class TweenValueFloat_2x2(TweenValueBase):
    """TweenValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float2x2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class TweenValueDouble_2x2(TweenValueBase):
    """TweenValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double2x2>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class TweenValueFloat_3x3(TweenValueBase):
    """TweenValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float3x3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class TweenValueDouble_3x3(TweenValueBase):
    """TweenValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double3x3>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class TweenValueFloat_4x4(TweenValueBase):
    """TweenValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<float4x4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class TweenValueDouble_4x4(TweenValueBase):
    """TweenValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<double4x4>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class TweenValueFloatQ(TweenValueBase):
    """TweenValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<floatQ>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class TweenValueDoubleQ(TweenValueBase):
    """TweenValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<doubleQ>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class TweenValueDateTime(TweenValueBase):
    """TweenValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[System.Private.CoreLib]System.DateTime>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class TweenValueTimeSpan(TweenValueBase):
    """TweenValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[System.Private.CoreLib]System.TimeSpan>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class TweenValueColor(TweenValueBase):
    """TweenValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<color>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class TweenValueColorX(TweenValueBase):
    """TweenValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<colorX>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class TweenValueShadowCastMode(TweenValueBase):
    """TweenValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.ShadowCastMode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class TweenValueLightType(TweenValueBase):
    """TweenValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.LightType>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class TweenValueSessionAccessLevel(TweenValueBase):
    """TweenValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class TweenValueKey(TweenValueBase):
    """TweenValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.Key>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class TweenValueHttpStatusCode(TweenValueBase):
    """TweenValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[System.Net.Primitives]System.Net.HttpStatusCode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class TweenValueHeadOutputDevice(TweenValueBase):
    """TweenValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class TweenValueReflectionProbeClear(TweenValueBase):
    """TweenValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class TweenValueReflectionProbeType(TweenValueBase):
    """TweenValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class TweenValueReflectionProbeTimeSlicingMode(TweenValueBase):
    """TweenValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class TweenValueCameraClearMode(TweenValueBase):
    """TweenValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.CameraClearMode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class TweenValueCameraPositioningMode(TweenValueBase):
    """TweenValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.CameraPositioningMode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class TweenValueCameraProjection(TweenValueBase):
    """TweenValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.CameraProjection>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class TweenValueZWrite(TweenValueBase):
    """TweenValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.ZWrite>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class TweenValueZTest(TweenValueBase):
    """TweenValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.ZTest>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class TweenValueBlend(TweenValueBase):
    """TweenValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.Blend>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class TweenValueBlendMode(TweenValueBase):
    """TweenValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.BlendMode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class TweenValueCulling(TweenValueBase):
    """TweenValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<FrooxEngine.Culling>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class TweenValueBodyNode(TweenValueBase):
    """TweenValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.BodyNode>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class TweenValueChirality(TweenValueBase):
    """TweenValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.Chirality>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class TweenValueDummyEnum(TweenValueBase):
    """TweenValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Animation.TweenValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "curve": "Curve",
        "duration": "Duration",
        "from_": "From",
        "on_done": "OnDone",
        "on_started": "OnStarted",
        "proportional_duration": "ProportionalDuration",
        "target": "Target",
        "to": "To",
    }

    curve: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CurvePreset>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    proportional_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IField<DummyEnum>>
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any TweenValue variant
TweenValue = (
    TweenValueBool |
    TweenValueByte |
    TweenValueUshort |
    TweenValueUint |
    TweenValueUlong |
    TweenValueSbyte |
    TweenValueShort |
    TweenValueInt |
    TweenValueLong |
    TweenValueFloat |
    TweenValueDouble |
    TweenValueDecimal |
    TweenValueChar |
    TweenValueString |
    TweenValueUri |
    TweenValueBool2 |
    TweenValueByte2 |
    TweenValueUshort2 |
    TweenValueUint2 |
    TweenValueUlong2 |
    TweenValueSbyte2 |
    TweenValueShort2 |
    TweenValueInt2 |
    TweenValueLong2 |
    TweenValueFloat2 |
    TweenValueDouble2 |
    TweenValueBool3 |
    TweenValueByte3 |
    TweenValueUshort3 |
    TweenValueUint3 |
    TweenValueUlong3 |
    TweenValueSbyte3 |
    TweenValueShort3 |
    TweenValueInt3 |
    TweenValueLong3 |
    TweenValueFloat3 |
    TweenValueDouble3 |
    TweenValueBool4 |
    TweenValueByte4 |
    TweenValueUshort4 |
    TweenValueUint4 |
    TweenValueUlong4 |
    TweenValueSbyte4 |
    TweenValueShort4 |
    TweenValueInt4 |
    TweenValueLong4 |
    TweenValueFloat4 |
    TweenValueDouble4 |
    TweenValueFloat_2x2 |
    TweenValueDouble_2x2 |
    TweenValueFloat_3x3 |
    TweenValueDouble_3x3 |
    TweenValueFloat_4x4 |
    TweenValueDouble_4x4 |
    TweenValueFloatQ |
    TweenValueDoubleQ |
    TweenValueDateTime |
    TweenValueTimeSpan |
    TweenValueColor |
    TweenValueColorX |
    TweenValueShadowCastMode |
    TweenValueLightType |
    TweenValueSessionAccessLevel |
    TweenValueKey |
    TweenValueHttpStatusCode |
    TweenValueHeadOutputDevice |
    TweenValueReflectionProbeClear |
    TweenValueReflectionProbeType |
    TweenValueReflectionProbeTimeSlicingMode |
    TweenValueCameraClearMode |
    TweenValueCameraPositioningMode |
    TweenValueCameraProjection |
    TweenValueZWrite |
    TweenValueZTest |
    TweenValueBlend |
    TweenValueBlendMode |
    TweenValueCulling |
    TweenValueBodyNode |
    TweenValueChirality |
    TweenValueDummyEnum
)