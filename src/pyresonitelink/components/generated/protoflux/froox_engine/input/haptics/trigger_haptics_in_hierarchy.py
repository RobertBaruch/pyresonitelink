"""Generated component: TriggerHapticsInHierarchy.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TriggerHapticsInHierarchy(GeneratedComponent):
    """TriggerHapticsInHierarchy component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Haptics.TriggerHapticsInHierarchy
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Haptics.TriggerHapticsInHierarchy"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "relative_intensity": "RelativeIntensity",
        "target_hierarchy": "TargetHierarchy",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    relative_intensity: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None