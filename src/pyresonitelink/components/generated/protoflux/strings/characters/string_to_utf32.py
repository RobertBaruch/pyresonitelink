"""Generated component: StringToUTF32.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class StringToUTF32(GeneratedComponent):
    """StringToUTF32 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.StringToUTF32
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.StringToUTF32"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "index": "Index",
        "persistent": "persistent",
        "string": "String",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    string: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None