"""Generated component: OnDestroying.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OnDestroying(GeneratedComponent):
    """OnDestroying component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.OnDestroying
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.OnDestroying"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "trigger": "Trigger",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    trigger: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None