"""Generated component: SphereForTangentLine.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SphereForTangentLine(GeneratedComponent):
    """SphereForTangentLine component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.SphereForTangentLine
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.SphereForTangentLine"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "line_direction": "LineDirection",
        "line_point": "LinePoint",
        "persistent": "persistent",
        "sphere_center": "SphereCenter",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    line_direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    line_point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    persistent: FieldBool | None = None
    sphere_center: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None