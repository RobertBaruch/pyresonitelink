"""Generated component: Raycaster.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Raycaster(GeneratedComponent):
    """Raycaster component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.Raycaster
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.Raycaster"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "direction": "Direction",
        "enabled": "Enabled",
        "hit_triggers": "HitTriggers",
        "max_distance": "MaxDistance",
        "origin": "Origin",
        "persistent": "persistent",
        "root": "Root",
        "update_order": "UpdateOrder",
        "users_only": "UsersOnly",
    }

    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    enabled: FieldBool | None = None
    hit_triggers: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    max_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    persistent: FieldBool | None = None
    root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None
    users_only: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>