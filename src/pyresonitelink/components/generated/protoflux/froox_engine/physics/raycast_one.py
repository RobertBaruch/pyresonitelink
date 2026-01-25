"""Generated component: RaycastOne.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RaycastOne(GeneratedComponent):
    """RaycastOne component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.RaycastOne
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.RaycastOne"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "debug_duration": "DebugDuration",
        "direction": "Direction",
        "enabled": "Enabled",
        "hit_triggers": "HitTriggers",
        "max_distance": "MaxDistance",
        "on_hit": "OnHit",
        "on_miss": "OnMiss",
        "origin": "Origin",
        "persistent": "persistent",
        "root": "Root",
        "update_order": "UpdateOrder",
        "users_only": "UsersOnly",
    }

    debug_duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    enabled: FieldBool | None = None
    hit_triggers: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    max_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    on_hit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_miss: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    persistent: FieldBool | None = None
    root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None
    users_only: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>