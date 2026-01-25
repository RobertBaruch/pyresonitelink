"""Generated component: RayToLineIntersectionDistance.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RayToLineIntersectionDistance(GeneratedComponent):
    """RayToLineIntersectionDistance component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayToLineIntersectionDistance
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayToLineIntersectionDistance"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "direction": "Direction",
        "enabled": "Enabled",
        "line_point0": "LinePoint0",
        "line_point1": "LinePoint1",
        "origin": "Origin",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    enabled: FieldBool | None = None
    line_point0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    line_point1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    origin: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None