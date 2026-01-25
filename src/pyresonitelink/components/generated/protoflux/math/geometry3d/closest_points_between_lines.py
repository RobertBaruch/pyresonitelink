"""Generated component: ClosestPointsBetweenLines.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ClosestPointsBetweenLines(GeneratedComponent):
    """ClosestPointsBetweenLines component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointsBetweenLines
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointsBetweenLines"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "line_dir0": "LineDir0",
        "line_dir1": "LineDir1",
        "line_point0": "LinePoint0",
        "line_point1": "LinePoint1",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    line_dir0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    line_dir1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    line_point0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    line_point1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None