"""Generated component: StringRemove.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class StringRemove(GeneratedComponent):
    """StringRemove component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.StringRemove
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.StringRemove"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "length": "Length",
        "persistent": "persistent",
        "start_index": "StartIndex",
        "str": "Str",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    start_index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None