"""Generated component: SetUserScale.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetUserScale(GeneratedComponent):
    """SetUserScale component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.SetUserScale
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.SetUserScale"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation_time": "AnimationTime",
        "enabled": "Enabled",
        "on_animation_finished": "OnAnimationFinished",
        "on_scale_change_start": "OnScaleChangeStart",
        "persistent": "persistent",
        "scale": "Scale",
        "update_order": "UpdateOrder",
        "user_root": "UserRoot",
    }

    animation_time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    on_animation_finished: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_scale_change_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    scale: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None
    user_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UserRoot>