"""Generated component: FromUnixSeconds.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FromUnixSeconds(GeneratedComponent):
    """FromUnixSeconds component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.FromUnixSeconds
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.FromUnixSeconds"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "is_local": "IsLocal",
        "persistent": "persistent",
        "unix_seconds": "UnixSeconds",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    is_local: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    unix_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    update_order: FieldInt | None = None