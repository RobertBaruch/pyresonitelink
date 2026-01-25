"""Generated component: LineCircleIntersections.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class LineCircleIntersections(GeneratedComponent):
    """LineCircleIntersections component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.LineCircleIntersections
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.LineCircleIntersections"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "center": "Center",
        "enabled": "Enabled",
        "line_point0": "LinePoint0",
        "line_point1": "LinePoint1",
        "persistent": "persistent",
        "radius": "Radius",
        "update_order": "UpdateOrder",
    }

    center: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    enabled: FieldBool | None = None
    line_point0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    line_point1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    persistent: FieldBool | None = None
    radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None