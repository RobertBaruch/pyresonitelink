"""Generated component: AnchorEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AnchorEvents(GeneratedComponent):
    """AnchorEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "anchor": "Anchor",
        "enabled": "Enabled",
        "on_anchored": "OnAnchored",
        "on_released": "OnReleased",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    anchor: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.CommonAvatar.AvatarAnchor>
    enabled: FieldBool | None = None
    on_anchored: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_released: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None