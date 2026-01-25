"""Generated component: SetHipsPosition.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetHipsPosition(GeneratedComponent):
    """SetHipsPosition component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.SetHipsPosition
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.SetHipsPosition"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "position": "Position",
        "update_order": "UpdateOrder",
        "user_root": "UserRoot",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None
    user_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UserRoot>