"""Generated component: LocalScreenPointToWorld.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class LocalScreenPointToWorld(GeneratedComponent):
    """LocalScreenPointToWorld component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalScreen.LocalScreenPointToWorld
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.LocalScreen.LocalScreenPointToWorld"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "distance": "Distance",
        "enabled": "Enabled",
        "normalized_screen_point": "NormalizedScreenPoint",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    normalized_screen_point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None