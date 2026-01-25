"""Generated component: FormatDateTimeAsDate.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FormatDateTimeAsDate(GeneratedComponent):
    """FormatDateTimeAsDate component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatDateTimeAsDate
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatDateTimeAsDate"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "date": "Date",
        "enabled": "Enabled",
        "format_provider": "FormatProvider",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    date: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    enabled: FieldBool | None = None
    format_provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.IFormatProvider>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None