"""Generated component: IndexOfString.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class IndexOfString(GeneratedComponent):
    """IndexOfString component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.IndexOfString
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.IndexOfString"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "comparison_mode": "ComparisonMode",
        "enabled": "Enabled",
        "part": "Part",
        "persistent": "persistent",
        "search_from_end": "SearchFromEnd",
        "start_index": "StartIndex",
        "str": "Str",
        "update_order": "UpdateOrder",
    }

    comparison_mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.StringComparison>
    enabled: FieldBool | None = None
    part: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    search_from_end: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    start_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None