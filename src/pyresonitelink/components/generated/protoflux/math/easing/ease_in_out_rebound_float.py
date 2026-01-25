"""Generated component: EaseInOutReboundFloat.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EaseInOutReboundFloat(GeneratedComponent):
    """EaseInOutReboundFloat component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInOutReboundFloat
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Easing.EaseInOutReboundFloat"
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
    rebound_amplitude: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None