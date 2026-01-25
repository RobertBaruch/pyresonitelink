"""Generated component: DynamicImpulseReceiver.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DynamicImpulseReceiver(GeneratedComponent):
    """DynamicImpulseReceiver component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiver
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiver"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_triggered": "OnTriggered",
        "persistent": "persistent",
        "tag": "Tag",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>
    update_order: FieldInt | None = None