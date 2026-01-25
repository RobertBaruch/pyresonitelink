"""Generated component: RectFromXYWH.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RectFromXYWH(GeneratedComponent):
    """RectFromXYWH component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectFromXYWH
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectFromXYWH"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "height": "Height",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "width": "Width",
        "x": "X",
        "y": "Y",
    }

    enabled: FieldBool | None = None
    height: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    width: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    y: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>