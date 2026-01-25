"""Generated component: ShiftLeft_Bool4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ShiftLeft_Bool4(GeneratedComponent):
    """ShiftLeft_Bool4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ShiftLeft_Bool4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ShiftLeft_Bool4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "enabled": "Enabled",
        "persistent": "persistent",
        "shift": "Shift",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    shift: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None