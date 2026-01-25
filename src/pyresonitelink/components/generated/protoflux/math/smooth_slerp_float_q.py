"""Generated component: SmoothSlerp_floatQ.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SmoothSlerp_floatQ(GeneratedComponent):
    """SmoothSlerp_floatQ component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SmoothSlerp_floatQ
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SmoothSlerp_floatQ"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "input": "Input",
        "persistent": "persistent",
        "speed": "Speed",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    persistent: FieldBool | None = None
    speed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None