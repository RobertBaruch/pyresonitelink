"""Generated component: ClosestPointOnConeSurface.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ClosestPointOnConeSurface(GeneratedComponent):
    """ClosestPointOnConeSurface component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointOnConeSurface
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointOnConeSurface"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "cone_base_radius": "ConeBaseRadius",
        "cone_center": "ConeCenter",
        "cone_height": "ConeHeight",
        "cone_orientation": "ConeOrientation",
        "enabled": "Enabled",
        "persistent": "persistent",
        "point": "Point",
        "update_order": "UpdateOrder",
    }

    cone_base_radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    cone_center: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    cone_height: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    cone_orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None