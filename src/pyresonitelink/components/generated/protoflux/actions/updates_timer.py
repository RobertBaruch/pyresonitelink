"""Generated component: UpdatesTimer.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UpdatesTimer(GeneratedComponent):
    """UpdatesTimer component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.UpdatesTimer
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.UpdatesTimer"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "interval": "Interval",
        "on_update": "OnUpdate",
        "persistent": "persistent",
        "skip_if_null": "SkipIfNull",
        "update_order": "UpdateOrder",
        "updating_user": "UpdatingUser",
    }

    enabled: FieldBool | None = None
    interval: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    on_update: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    skip_if_null: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<bool>
    update_order: FieldInt | None = None
    updating_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.User>