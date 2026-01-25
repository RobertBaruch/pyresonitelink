"""Generated component: TranslateRect.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TranslateRect(GeneratedComponent):
    """TranslateRect component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.TranslateRect
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.TranslateRect"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "offset": "Offset",
        "persistent": "persistent",
        "rect": "Rect",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    persistent: FieldBool | None = None
    rect: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Rect>
    update_order: FieldInt | None = None