"""Generated component: ButtonEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ButtonEvents(GeneratedComponent):
    """ButtonEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.ButtonEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.ButtonEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "button": "Button",
        "enabled": "Enabled",
        "hover_enter": "HoverEnter",
        "hover_leave": "HoverLeave",
        "hover_stay": "HoverStay",
        "persistent": "persistent",
        "pressed": "Pressed",
        "pressing": "Pressing",
        "released": "Released",
        "update_order": "UpdateOrder",
    }

    button: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.IButton>
    enabled: FieldBool | None = None
    hover_enter: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    hover_leave: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    hover_stay: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    pressed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    pressing: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    released: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None