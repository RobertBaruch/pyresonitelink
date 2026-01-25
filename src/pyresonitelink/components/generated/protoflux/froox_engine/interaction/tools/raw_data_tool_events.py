"""Generated component: RawDataToolEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RawDataToolEvents(GeneratedComponent):
    """RawDataToolEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.RawDataToolEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.RawDataToolEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "dequipped": "Dequipped",
        "enabled": "Enabled",
        "equipped": "Equipped",
        "persistent": "persistent",
        "primary_held": "PrimaryHeld",
        "primary_pressed": "PrimaryPressed",
        "primary_released": "PrimaryReleased",
        "secondary_held": "SecondaryHeld",
        "secondary_pressed": "SecondaryPressed",
        "secondary_released": "SecondaryReleased",
        "tool": "Tool",
        "tool_update": "ToolUpdate",
        "update_order": "UpdateOrder",
    }

    dequipped: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    enabled: FieldBool | None = None
    equipped: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    primary_held: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    primary_pressed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    primary_released: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    secondary_held: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    secondary_pressed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    secondary_released: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tool: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.RawDataTool>
    tool_update: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None