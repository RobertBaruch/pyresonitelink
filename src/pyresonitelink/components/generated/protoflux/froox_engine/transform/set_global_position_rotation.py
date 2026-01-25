"""Generated component: SetGlobalPositionRotation.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SetGlobalPositionRotation(GeneratedComponent):
    """SetGlobalPositionRotation component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.SetGlobalPositionRotation
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.SetGlobalPositionRotation"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "instance": "Instance",
        "next": "Next",
        "persistent": "persistent",
        "position": "Position",
        "rotation": "Rotation",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    instance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    rotation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    update_order: FieldInt | None = None