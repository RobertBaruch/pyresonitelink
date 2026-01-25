"""Generated component: HSV_ToColor.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class HSV_ToColor(GeneratedComponent):
    """HSV_ToColor component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSV_ToColor
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSV_ToColor"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "h": "H",
        "persistent": "persistent",
        "s": "S",
        "update_order": "UpdateOrder",
        "v": "V",
    }

    enabled: FieldBool | None = None
    h: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    s: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None
    v: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>