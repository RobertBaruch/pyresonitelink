"""Generated component: EquipAvatar.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EquipAvatar(GeneratedComponent):
    """EquipAvatar component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.EquipAvatar
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.EquipAvatar"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "avatar_root": "AvatarRoot",
        "destroy_old": "DestroyOld",
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "user": "User",
    }

    avatar_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    destroy_old: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>