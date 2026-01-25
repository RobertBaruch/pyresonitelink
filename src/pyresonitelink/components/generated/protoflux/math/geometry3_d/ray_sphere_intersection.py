"""Generated component: RaySphereIntersection.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RaySphereIntersection(GeneratedComponent):
    """RaySphereIntersection component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RaySphereIntersection
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RaySphereIntersection"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "center": "Center",
        "enabled": "Enabled",
        "persistent": "persistent",
        "radius": "Radius",
        "ray_direction": "RayDirection",
        "ray_origin": "RayOrigin",
        "update_order": "UpdateOrder",
    }

    center: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    ray_direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    ray_origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None