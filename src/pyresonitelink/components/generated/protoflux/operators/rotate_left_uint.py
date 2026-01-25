"""Generated component: RotateLeft_Uint.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RotateLeft_Uint(GeneratedComponent):
    """RotateLeft_Uint component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Uint
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Uint"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "enabled": "Enabled",
        "persistent": "persistent",
        "rotate": "Rotate",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    rotate: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None