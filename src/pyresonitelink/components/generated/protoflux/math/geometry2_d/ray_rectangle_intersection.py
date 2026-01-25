"""Generated component: RayRectangleIntersection.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RayRectangleIntersection(GeneratedComponent):
    """RayRectangleIntersection component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayRectangleIntersection
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayRectangleIntersection"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "direction": "Direction",
        "enabled": "Enabled",
        "origin": "Origin",
        "persistent": "persistent",
        "rectangle": "Rectangle",
        "update_order": "UpdateOrder",
    }

    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    enabled: FieldBool | None = None
    origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    persistent: FieldBool | None = None
    rectangle: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Rect>
    update_order: FieldInt | None = None