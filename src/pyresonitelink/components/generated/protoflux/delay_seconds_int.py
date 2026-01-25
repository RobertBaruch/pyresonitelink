"""Generated component: DelaySecondsInt.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelaySecondsInt(GeneratedComponent):
    """DelaySecondsInt component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.DelaySecondsInt
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.DelaySecondsInt"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "duration": "Duration",
        "enabled": "Enabled",
        "next": "Next",
        "on_triggered": "OnTriggered",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None