"""Generated component: ReleaseUser.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ReleaseUser(GeneratedComponent):
    """ReleaseUser component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.ReleaseUser
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.ReleaseUser"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "anchor": "Anchor",
        "enabled": "Enabled",
        "on_failure": "OnFailure",
        "on_released": "OnReleased",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    anchor: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAvatarAnchor>
    enabled: FieldBool | None = None
    on_failure: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_released: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None