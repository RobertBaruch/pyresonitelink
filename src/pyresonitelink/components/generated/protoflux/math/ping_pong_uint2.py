"""Generated component: PingPong_Uint2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PingPong_Uint2(GeneratedComponent):
    """PingPong_Uint2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "length": "Length",
        "n": "N",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None