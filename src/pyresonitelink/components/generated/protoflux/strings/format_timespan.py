"""Generated component: FormatTimespan.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FormatTimespan(GeneratedComponent):
    """FormatTimespan component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatTimespan
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.FormatTimespan"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "format_provider": "FormatProvider",
        "persistent": "persistent",
        "show_milliseconds": "ShowMilliseconds",
        "show_seconds": "ShowSeconds",
        "time_span": "TimeSpan",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    format_provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.IFormatProvider>
    persistent: FieldBool | None = None
    show_milliseconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    show_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    time_span: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    update_order: FieldInt | None = None