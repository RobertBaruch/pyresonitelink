"""Generated component: SetSpeed.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetSpeed(GeneratedComponent):
    """SetSpeed component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.SetSpeed
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Playback.SetSpeed"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "speed": "Speed",
        "target": "Target",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IPlayable>
    update_order: FieldInt | None = None