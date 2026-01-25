"""Generated component: DebugBox.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DebugBox(GeneratedComponent):
    """DebugBox component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugBox
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugBox"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "duration": "Duration",
        "enabled": "Enabled",
        "next": "Next",
        "orientation": "Orientation",
        "persistent": "persistent",
        "point": "Point",
        "size": "Size",
        "update_order": "UpdateOrder",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    size: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None