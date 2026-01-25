"""Generated component: FindParentByName.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FindParentByName(GeneratedComponent):
    """FindParentByName component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.FindParentByName
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.FindParentByName"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "ignore_case": "IgnoreCase",
        "instance": "Instance",
        "match_substring": "MatchSubstring",
        "name": "Name",
        "persistent": "persistent",
        "search_depth": "SearchDepth",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    ignore_case: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    instance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    match_substring: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    search_depth: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None