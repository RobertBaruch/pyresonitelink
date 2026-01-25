"""Generated component: SigmoidDouble.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SigmoidDouble(GeneratedComponent):
    """SigmoidDouble component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SigmoidDouble
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SigmoidDouble"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "e": "E",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "x": "X",
    }

    e: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>