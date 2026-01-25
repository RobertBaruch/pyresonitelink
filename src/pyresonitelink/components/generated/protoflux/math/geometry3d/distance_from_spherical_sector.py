"""Generated component: DistanceFromSphericalSector.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DistanceFromSphericalSector(GeneratedComponent):
    """DistanceFromSphericalSector component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.DistanceFromSphericalSector
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.DistanceFromSphericalSector"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "angle": "Angle",
        "center": "Center",
        "direction": "Direction",
        "enabled": "Enabled",
        "persistent": "persistent",
        "point": "Point",
        "radius": "Radius",
        "update_order": "UpdateOrder",
    }

    angle: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    center: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None