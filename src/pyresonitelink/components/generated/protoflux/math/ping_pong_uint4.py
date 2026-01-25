"""Generated component: PingPong_Uint4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PingPong_Uint4(GeneratedComponent):
    """PingPong_Uint4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PingPong_Uint4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "length": "Length",
        "n": "N",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None