"""Generated component: Compose_ScaleRotation_Double4x4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Compose_ScaleRotation_Double4x4(GeneratedComponent):
    """Compose_ScaleRotation_Double4x4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Compose_ScaleRotation_Double4x4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Compose_ScaleRotation_Double4x4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "rotation": "Rotation",
        "scale": "Scale",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    rotation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    scale: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    update_order: FieldInt | None = None