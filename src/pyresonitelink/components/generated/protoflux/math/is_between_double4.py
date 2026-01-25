"""Generated component: IsBetween_Double4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class IsBetween_Double4(GeneratedComponent):
    """IsBetween_Double4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.IsBetween_Double4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.IsBetween_Double4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "max": "Max",
        "min": "Min",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>