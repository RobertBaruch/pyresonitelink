"""Generated component: RandomPointInCone.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RandomPointInCone(GeneratedComponent):
    """RandomPointInCone component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomPointInCone
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomPointInCone"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_radius": "BaseRadius",
        "enabled": "Enabled",
        "height": "Height",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    base_radius: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    height: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None