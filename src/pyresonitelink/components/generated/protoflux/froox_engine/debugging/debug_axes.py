"""Generated component: DebugAxes.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DebugAxes(GeneratedComponent):
    """DebugAxes component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugAxes
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugAxes"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "enabled": "Enabled",
        "forward_color": "ForwardColor",
        "length": "Length",
        "next": "Next",
        "persistent": "persistent",
        "position": "Position",
        "right_color": "RightColor",
        "rotation": "Rotation",
        "up_color": "UpColor",
        "update_order": "UpdateOrder",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    forward_color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    right_color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    rotation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    up_color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    update_order: FieldInt | None = None