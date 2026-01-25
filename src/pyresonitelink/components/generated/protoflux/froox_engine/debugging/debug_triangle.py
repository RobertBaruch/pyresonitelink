"""Generated component: DebugTriangle.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DebugTriangle(GeneratedComponent):
    """DebugTriangle component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugTriangle
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugTriangle"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "duration": "Duration",
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "point0": "Point0",
        "point1": "Point1",
        "point2": "Point2",
        "update_order": "UpdateOrder",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    point0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    point1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    point2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None