"""Generated component: ApplyCharacterImpulse.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ApplyCharacterImpulse(GeneratedComponent):
    """ApplyCharacterImpulse component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.ApplyCharacterImpulse
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.ApplyCharacterImpulse"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "character": "Character",
        "enabled": "Enabled",
        "ignore_mass": "IgnoreMass",
        "impulse": "Impulse",
        "next": "Next",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    character: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.CharacterController>
    enabled: FieldBool | None = None
    ignore_mass: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    impulse: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None