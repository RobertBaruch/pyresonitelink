"""Generated component: BlackBodyColorX.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BlackBodyColorX(GeneratedComponent):
    """BlackBodyColorX component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.BlackBodyColorX
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.BlackBodyColorX"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "temperature": "Temperature",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    temperature: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None