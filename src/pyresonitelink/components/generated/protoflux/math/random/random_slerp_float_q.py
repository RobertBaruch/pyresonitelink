"""Generated component: RandomSlerpFloatQ.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RandomSlerpFloatQ(GeneratedComponent):
    """RandomSlerpFloatQ component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomSlerpFloatQ
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomSlerpFloatQ"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "max": "Max",
        "min": "Min",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None