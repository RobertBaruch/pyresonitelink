"""Generated component: UserLeft.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UserLeft(GeneratedComponent):
    """UserLeft component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.UserLeft
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.UserLeft"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_left": "OnLeft",
        "only_host": "OnlyHost",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_left: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_host: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None