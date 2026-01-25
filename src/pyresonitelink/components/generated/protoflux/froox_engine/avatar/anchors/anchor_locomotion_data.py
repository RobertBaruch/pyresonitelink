"""Generated component: AnchorLocomotionData.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AnchorLocomotionData(GeneratedComponent):
    """AnchorLocomotionData component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorLocomotionData
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorLocomotionData"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "anchor": "Anchor",
        "enabled": "Enabled",
        "on_locomotion_update": "OnLocomotionUpdate",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    anchor: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.CommonAvatar.AvatarAnchor>
    enabled: FieldBool | None = None
    on_locomotion_update: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None