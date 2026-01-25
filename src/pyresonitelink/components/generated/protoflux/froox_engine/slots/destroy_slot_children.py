"""Generated component: DestroySlotChildren.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DestroySlotChildren(GeneratedComponent):
    """DestroySlotChildren component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.DestroySlotChildren
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.DestroySlotChildren"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "instance": "Instance",
        "next": "Next",
        "persistent": "persistent",
        "preserve_assets": "PreserveAssets",
        "send_destroying_event": "SendDestroyingEvent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    instance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    preserve_assets: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    send_destroying_event: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    update_order: FieldInt | None = None