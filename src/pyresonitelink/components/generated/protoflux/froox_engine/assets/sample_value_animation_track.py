"""Generated component: SampleValueAnimationTrack.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleValueAnimationTrackBase(GeneratedComponent):
    """Base class for SampleValueAnimationTrack<T> variants."""

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
class SampleValueAnimationTrackBool(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackByte(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUshort(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUint(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUlong(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackSbyte(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackShort(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackInt(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackLong(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDecimal(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackChar(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackString(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUri(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBool2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackByte2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUshort2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUint2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUlong2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackSbyte2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackShort2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackInt2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackLong2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBool3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackByte3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUshort3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUint3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUlong3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackSbyte3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackShort3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackInt3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackLong3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBool4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackByte4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUshort4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUint4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackUlong4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackSbyte4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackShort4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackInt4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackLong4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat_2x2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble_2x2(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat_3x3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble_3x3(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloat_4x4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDouble_4x4(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackFloatQ(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDoubleQ(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDateTime(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackTimeSpan(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackColor(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackColorX(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackShadowCastMode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackLightType(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackSessionAccessLevel(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackKey(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackHttpStatusCode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackHeadOutputDevice(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackReflectionProbeClear(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackReflectionProbeType(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackReflectionProbeTimeSlicingMode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackCameraClearMode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackCameraPositioningMode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackCameraProjection(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackZWrite(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackZTest(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBlend(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBlendMode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackCulling(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackBodyNode(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackChirality(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class SampleValueAnimationTrackDummyEnum(SampleValueAnimationTrackBase):
    """SampleValueAnimationTrack<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleValueAnimationTrack<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "time": "Time",
        "track_index": "TrackIndex",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    track_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


# Type alias for any SampleValueAnimationTrack variant
SampleValueAnimationTrack = (
    SampleValueAnimationTrackBool |
    SampleValueAnimationTrackByte |
    SampleValueAnimationTrackUshort |
    SampleValueAnimationTrackUint |
    SampleValueAnimationTrackUlong |
    SampleValueAnimationTrackSbyte |
    SampleValueAnimationTrackShort |
    SampleValueAnimationTrackInt |
    SampleValueAnimationTrackLong |
    SampleValueAnimationTrackFloat |
    SampleValueAnimationTrackDouble |
    SampleValueAnimationTrackDecimal |
    SampleValueAnimationTrackChar |
    SampleValueAnimationTrackString |
    SampleValueAnimationTrackUri |
    SampleValueAnimationTrackBool2 |
    SampleValueAnimationTrackByte2 |
    SampleValueAnimationTrackUshort2 |
    SampleValueAnimationTrackUint2 |
    SampleValueAnimationTrackUlong2 |
    SampleValueAnimationTrackSbyte2 |
    SampleValueAnimationTrackShort2 |
    SampleValueAnimationTrackInt2 |
    SampleValueAnimationTrackLong2 |
    SampleValueAnimationTrackFloat2 |
    SampleValueAnimationTrackDouble2 |
    SampleValueAnimationTrackBool3 |
    SampleValueAnimationTrackByte3 |
    SampleValueAnimationTrackUshort3 |
    SampleValueAnimationTrackUint3 |
    SampleValueAnimationTrackUlong3 |
    SampleValueAnimationTrackSbyte3 |
    SampleValueAnimationTrackShort3 |
    SampleValueAnimationTrackInt3 |
    SampleValueAnimationTrackLong3 |
    SampleValueAnimationTrackFloat3 |
    SampleValueAnimationTrackDouble3 |
    SampleValueAnimationTrackBool4 |
    SampleValueAnimationTrackByte4 |
    SampleValueAnimationTrackUshort4 |
    SampleValueAnimationTrackUint4 |
    SampleValueAnimationTrackUlong4 |
    SampleValueAnimationTrackSbyte4 |
    SampleValueAnimationTrackShort4 |
    SampleValueAnimationTrackInt4 |
    SampleValueAnimationTrackLong4 |
    SampleValueAnimationTrackFloat4 |
    SampleValueAnimationTrackDouble4 |
    SampleValueAnimationTrackFloat_2x2 |
    SampleValueAnimationTrackDouble_2x2 |
    SampleValueAnimationTrackFloat_3x3 |
    SampleValueAnimationTrackDouble_3x3 |
    SampleValueAnimationTrackFloat_4x4 |
    SampleValueAnimationTrackDouble_4x4 |
    SampleValueAnimationTrackFloatQ |
    SampleValueAnimationTrackDoubleQ |
    SampleValueAnimationTrackDateTime |
    SampleValueAnimationTrackTimeSpan |
    SampleValueAnimationTrackColor |
    SampleValueAnimationTrackColorX |
    SampleValueAnimationTrackShadowCastMode |
    SampleValueAnimationTrackLightType |
    SampleValueAnimationTrackSessionAccessLevel |
    SampleValueAnimationTrackKey |
    SampleValueAnimationTrackHttpStatusCode |
    SampleValueAnimationTrackHeadOutputDevice |
    SampleValueAnimationTrackReflectionProbeClear |
    SampleValueAnimationTrackReflectionProbeType |
    SampleValueAnimationTrackReflectionProbeTimeSlicingMode |
    SampleValueAnimationTrackCameraClearMode |
    SampleValueAnimationTrackCameraPositioningMode |
    SampleValueAnimationTrackCameraProjection |
    SampleValueAnimationTrackZWrite |
    SampleValueAnimationTrackZTest |
    SampleValueAnimationTrackBlend |
    SampleValueAnimationTrackBlendMode |
    SampleValueAnimationTrackCulling |
    SampleValueAnimationTrackBodyNode |
    SampleValueAnimationTrackChirality |
    SampleValueAnimationTrackDummyEnum
)