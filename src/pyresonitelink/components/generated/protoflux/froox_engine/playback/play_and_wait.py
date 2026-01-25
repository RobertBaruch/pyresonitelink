"""Generated component: PlayAndWait.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PlayAndWait(GeneratedComponent):
    """PlayAndWait component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.PlayAndWait
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.PlayAndWait"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_playback_finished": "OnPlaybackFinished",
        "on_started": "OnStarted",
        "persistent": "persistent",
        "target": "Target",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_playback_finished: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IPlayable>
    update_order: FieldInt | None = None