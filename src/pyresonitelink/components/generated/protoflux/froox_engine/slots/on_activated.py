"""Generated component: OnActivated.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OnActivated(GeneratedComponent):
    """OnActivated component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.OnActivated
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.OnActivated"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "only_host": "OnlyHost",
        "persistent": "persistent",
        "trigger": "Trigger",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    only_host: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    trigger: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None