"""Generated component: HeadFacingDirection.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class HeadFacingDirection(GeneratedComponent):
    """HeadFacingDirection component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.HeadFacingDirection
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.HeadFacingDirection"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "user_root": "UserRoot",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    user_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UserRoot>