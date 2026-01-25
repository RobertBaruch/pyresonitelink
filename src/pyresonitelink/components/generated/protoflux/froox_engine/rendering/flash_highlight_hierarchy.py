"""Generated component: FlashHighlightHierarchy.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FlashHighlightHierarchy(GeneratedComponent):
    """FlashHighlightHierarchy component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.FlashHighlightHierarchy
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.FlashHighlightHierarchy"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "duration": "Duration",
        "enabled": "Enabled",
        "exclude_colliders": "ExcludeColliders",
        "exclude_disabled": "ExcludeDisabled",
        "exclude_meshes": "ExcludeMeshes",
        "hierarchy_root": "HierarchyRoot",
        "next": "Next",
        "persistent": "persistent",
        "track_position": "TrackPosition",
        "update_order": "UpdateOrder",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    duration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    exclude_colliders: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    exclude_meshes: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    hierarchy_root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    track_position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    update_order: FieldInt | None = None