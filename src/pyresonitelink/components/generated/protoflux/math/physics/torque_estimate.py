"""Generated component: TorqueEstimate.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TorqueEstimate(GeneratedComponent):
    """TorqueEstimate component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Physics.TorqueEstimate
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Physics.TorqueEstimate"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "drag": "Drag",
        "enabled": "Enabled",
        "initial_torque": "InitialTorque",
        "persistent": "persistent",
        "time": "Time",
        "update_order": "UpdateOrder",
    }

    drag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    initial_torque: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    persistent: FieldBool | None = None
    time: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None