"""Generated component: TransformBounds.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TransformBounds(GeneratedComponent):
    """TransformBounds component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.TransformBounds
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.TransformBounds"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "bounds": "Bounds",
        "enabled": "Enabled",
        "persistent": "persistent",
        "source_space": "SourceSpace",
        "target_space": "TargetSpace",
        "update_order": "UpdateOrder",
    }

    bounds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    source_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    target_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None