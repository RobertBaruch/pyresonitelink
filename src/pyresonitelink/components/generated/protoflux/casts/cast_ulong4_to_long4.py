"""Generated component: Cast_ulong4_To_long4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Cast_ulong4_To_long4(GeneratedComponent):
    """Cast_ulong4_To_long4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.Cast_ulong4_To_long4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.Cast_ulong4_To_long4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "input": "Input",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None