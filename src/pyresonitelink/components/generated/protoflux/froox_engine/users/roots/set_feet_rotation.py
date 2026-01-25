"""Generated component: SetFeetRotation.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetFeetRotation(GeneratedComponent):
    """SetFeetRotation component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.SetFeetRotation
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.SetFeetRotation"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "rotation": "Rotation",
        "update_order": "UpdateOrder",
        "user_root": "UserRoot",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    rotation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    update_order: FieldInt | None = None
    user_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UserRoot>