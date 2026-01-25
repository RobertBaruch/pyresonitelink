"""Generated component: HitUVCoordinate.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class HitUVCoordinate(GeneratedComponent):
    """HitUVCoordinate component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.HitUVCoordinate
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.HitUVCoordinate"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "hit_collider": "HitCollider",
        "hit_point": "HitPoint",
        "hit_triangle_index": "HitTriangleIndex",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    hit_collider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.ICollider>
    hit_point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    hit_triangle_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None