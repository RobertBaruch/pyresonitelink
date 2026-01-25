"""Generated component: Div_Ulong_Ulong2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Div_Ulong_Ulong2(GeneratedComponent):
    """Div_Ulong_Ulong2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Div_Ulong_Ulong2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Div_Ulong_Ulong2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "b": "B",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    b: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None