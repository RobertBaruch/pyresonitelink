"""Generated component: RotateLeft_Bool2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RotateLeft_Bool2(GeneratedComponent):
    """RotateLeft_Bool2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Bool2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.RotateLeft_Bool2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "enabled": "Enabled",
        "persistent": "persistent",
        "rotate": "Rotate",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    rotate: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None