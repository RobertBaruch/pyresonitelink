"""Generated component: RayPlaneIntersection.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RayPlaneIntersection(GeneratedComponent):
    """RayPlaneIntersection component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RayPlaneIntersection
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RayPlaneIntersection"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "plane_normal": "PlaneNormal",
        "plane_point": "PlanePoint",
        "ray_direction": "RayDirection",
        "ray_origin": "RayOrigin",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    plane_normal: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    plane_point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    ray_direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    ray_origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None