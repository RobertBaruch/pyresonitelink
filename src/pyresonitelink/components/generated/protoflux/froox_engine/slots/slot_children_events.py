"""Generated component: SlotChildrenEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SlotChildrenEvents(GeneratedComponent):
    """SlotChildrenEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.SlotChildrenEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.SlotChildrenEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "instance": "Instance",
        "on_child_added": "OnChildAdded",
        "on_child_removed": "OnChildRemoved",
        "on_user": "OnUser",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    instance: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.Slot>
    on_child_added: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_child_removed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None