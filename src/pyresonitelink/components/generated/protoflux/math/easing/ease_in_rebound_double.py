"""Generated component: EaseInReboundDouble.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EaseInReboundDouble(GeneratedComponent):
    """EaseInReboundDouble component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInReboundDouble
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInReboundDouble"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "rebound_amplitude": "ReboundAmplitude",
        "time": "Time",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    rebound_amplitude: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    update_order: FieldInt | None = None