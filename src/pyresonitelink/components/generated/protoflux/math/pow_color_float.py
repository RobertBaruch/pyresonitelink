"""Generated component: Pow_Color_Float.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Pow_Color_Float(GeneratedComponent):
    """Pow_Color_Float component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Pow_Color_Float
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Pow_Color_Float"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "n": "N",
        "persistent": "persistent",
        "power": "Power",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    persistent: FieldBool | None = None
    power: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None