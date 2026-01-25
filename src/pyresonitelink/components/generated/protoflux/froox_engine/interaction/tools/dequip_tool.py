"""Generated component: DequipTool.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DequipTool(GeneratedComponent):
    """DequipTool component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.DequipTool
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.DequipTool"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_dequip_fail": "OnDequipFail",
        "on_dequipped": "OnDequipped",
        "persistent": "persistent",
        "pop_off": "PopOff",
        "side": "Side",
        "update_order": "UpdateOrder",
        "user": "User",
    }

    enabled: FieldBool | None = None
    on_dequip_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_dequipped: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    pop_off: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    side: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    update_order: FieldInt | None = None
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>