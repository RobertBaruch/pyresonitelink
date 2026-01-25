"""Generated component: CountOccurrences.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class CountOccurrences(GeneratedComponent):
    """CountOccurrences component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.CountOccurrences
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.CountOccurrences"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "comparison_mode": "ComparisonMode",
        "enabled": "Enabled",
        "persistent": "persistent",
        "search": "Search",
        "str": "Str",
        "update_order": "UpdateOrder",
    }

    comparison_mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.StringComparison>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    search: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None