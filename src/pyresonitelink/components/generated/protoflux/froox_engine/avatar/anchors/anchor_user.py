"""Generated component: AnchorUser.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AnchorUser(GeneratedComponent):
    """AnchorUser component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorUser
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorUser"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "anchor": "Anchor",
        "enabled": "Enabled",
        "on_anchored": "OnAnchored",
        "on_failure": "OnFailure",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "user": "User",
    }

    anchor: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAvatarAnchor>
    enabled: FieldBool | None = None
    on_anchored: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failure: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>