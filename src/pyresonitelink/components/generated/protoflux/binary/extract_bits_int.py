"""Generated component: ExtractBits_int.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ExtractBits_int(GeneratedComponent):
    """ExtractBits_int component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_int
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_int"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "integer": "Integer",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    integer: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None