"""Generated component: ConstructDateTime.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ConstructDateTime(GeneratedComponent):
    """ConstructDateTime component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.ConstructDateTime
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.TimeAndDate.ConstructDateTime"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "day": "Day",
        "enabled": "Enabled",
        "hour": "Hour",
        "kind": "Kind",
        "millisecond": "Millisecond",
        "minute": "Minute",
        "month": "Month",
        "persistent": "persistent",
        "second": "Second",
        "update_order": "UpdateOrder",
        "year": "Year",
    }

    day: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    enabled: FieldBool | None = None
    hour: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    kind: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTimeKind>
    millisecond: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    minute: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    month: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    second: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None
    year: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>