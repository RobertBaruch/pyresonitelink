"""Generated component: LookRotation_doubleQ.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class LookRotation_doubleQ(GeneratedComponent):
    """LookRotation_doubleQ component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.LookRotation_doubleQ
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.LookRotation_doubleQ"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "forward": "Forward",
        "persistent": "persistent",
        "up": "Up",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    forward: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    persistent: FieldBool | None = None
    up: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    update_order: FieldInt | None = None