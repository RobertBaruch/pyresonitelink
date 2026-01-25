"""Generated component: PointOnCircle.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PointOnCircle(GeneratedComponent):
    """PointOnCircle component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.PointOnCircle
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.PointOnCircle"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "normalized_position": "NormalizedPosition",
        "persistent": "persistent",
        "radius": "Radius",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    normalized_position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None