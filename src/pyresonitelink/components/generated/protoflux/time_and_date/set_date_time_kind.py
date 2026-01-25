"""Generated component: SetDateTimeKind.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetDateTimeKind(GeneratedComponent):
    """SetDateTimeKind component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.SetDateTimeKind
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.SetDateTimeKind"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "date_time": "DateTime",
        "enabled": "Enabled",
        "kind": "Kind",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    date_time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    enabled: FieldBool | None = None
    kind: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTimeKind>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None