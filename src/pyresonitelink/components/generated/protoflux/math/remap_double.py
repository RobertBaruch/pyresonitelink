"""Generated component: Remap_Double.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Remap_Double(GeneratedComponent):
    """Remap_Double component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Remap_Double
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Remap_Double"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "in_max": "InMax",
        "in_min": "InMin",
        "out_max": "OutMax",
        "out_min": "OutMin",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    in_max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    in_min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    out_max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    out_min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>