"""Generated component: DuplicateSlot.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DuplicateSlot(GeneratedComponent):
    """DuplicateSlot component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.DuplicateSlot
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.DuplicateSlot"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "override_parent": "OverrideParent",
        "persistent": "persistent",
        "template": "Template",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    override_parent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    persistent: FieldBool | None = None
    template: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None