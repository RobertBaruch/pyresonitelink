"""Generated component: DebugVector.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DebugVector(GeneratedComponent):
    """DebugVector component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugVector
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugVector"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "duration": "Duration",
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "position": "Position",
        "radius_ratio": "RadiusRatio",
        "update_order": "UpdateOrder",
        "vector": "Vector",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    radius_ratio: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None
    vector: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>