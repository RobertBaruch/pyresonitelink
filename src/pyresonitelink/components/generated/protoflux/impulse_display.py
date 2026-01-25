"""Generated component: ImpulseDisplay.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ImpulseDisplay(GeneratedComponent):
    """ImpulseDisplay component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseDisplay
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseDisplay"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "_debug_text": "_debugText",
        "_timeline_root": "_timelineRoot",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    _debug_text: Reference | None = None  # -> FrooxEngine.UIX.Text
    _timeline_root: Reference | None = None  # -> FrooxEngine.Slot
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None