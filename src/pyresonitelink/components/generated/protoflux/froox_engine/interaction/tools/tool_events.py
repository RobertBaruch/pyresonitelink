"""Generated component: ToolEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ToolEvents(GeneratedComponent):
    """ToolEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.ToolEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.ToolEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "dequipped": "Dequipped",
        "enabled": "Enabled",
        "equipped": "Equipped",
        "persistent": "persistent",
        "tool": "Tool",
        "update_order": "UpdateOrder",
    }

    dequipped: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    enabled: FieldBool | None = None
    equipped: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    tool: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.ITool>
    update_order: FieldInt | None = None