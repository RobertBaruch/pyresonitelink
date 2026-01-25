"""Generated component: EaseInElasticDouble.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EaseInElasticDouble(GeneratedComponent):
    """EaseInElasticDouble component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInElasticDouble
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInElasticDouble"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "amplitude": "Amplitude",
        "enabled": "Enabled",
        "period": "Period",
        "persistent": "persistent",
        "time": "Time",
        "update_order": "UpdateOrder",
    }

    amplitude: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    enabled: FieldBool | None = None
    period: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    persistent: FieldBool | None = None
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    update_order: FieldInt | None = None