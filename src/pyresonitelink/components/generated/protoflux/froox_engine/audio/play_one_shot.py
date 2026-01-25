"""Generated component: PlayOneShot.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PlayOneShot(GeneratedComponent):
    """PlayOneShot component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.PlayOneShot
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.PlayOneShot"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "clip": "Clip",
        "distance_space": "DistanceSpace",
        "doppler": "Doppler",
        "enabled": "Enabled",
        "global_": "Global",
        "group": "Group",
        "ignore_audio_effects": "IgnoreAudioEffects",
        "local_only": "LocalOnly",
        "max_distance": "MaxDistance",
        "max_scale": "MaxScale",
        "min_distance": "MinDistance",
        "min_scale": "MinScale",
        "on_started_playing": "OnStartedPlaying",
        "parent_under_root": "ParentUnderRoot",
        "persistent": "persistent",
        "point": "Point",
        "priority": "Priority",
        "rolloff": "Rolloff",
        "root": "Root",
        "spatial_blend": "SpatialBlend",
        "spatialize": "Spatialize",
        "speed": "Speed",
        "update_order": "UpdateOrder",
        "volume": "Volume",
    }

    clip: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.AudioClip>>
    distance_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.AudioDistanceSpace>
    doppler: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool>>
    group: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.AudioTypeGroup>
    ignore_audio_effects: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    local_only: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    max_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    max_scale: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    min_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    min_scale: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    on_started_playing: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    parent_under_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    priority: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    rolloff: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Awwdio]Awwdio.AudioRolloffCurve>
    root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    spatial_blend: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    spatialize: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None
    volume: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>