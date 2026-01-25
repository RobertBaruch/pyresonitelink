"""Generated component: ColorAddValueHDR.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ColorAddValueHDR(GeneratedComponent):
    """ColorAddValueHDR component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorAddValueHDR
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorAddValueHDR"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>