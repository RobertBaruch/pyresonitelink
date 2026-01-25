"""Generated component: BakeMeshes.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BakeMeshes(GeneratedComponent):
    """BakeMeshes component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.BakeMeshes
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.BakeMeshes"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "assets_slot": "AssetsSlot",
        "collider_handling": "ColliderHandling",
        "destroy_original": "DestroyOriginal",
        "enabled": "Enabled",
        "grabbable_handling": "GrabbableHandling",
        "include_inactive": "IncludeInactive",
        "on_baked": "OnBaked",
        "on_bake_started": "OnBakeStarted",
        "persistent": "persistent",
        "root": "Root",
        "skinned_mesh_mode": "SkinnedMeshMode",
        "undoable": "Undoable",
        "update_order": "UpdateOrder",
    }

    assets_slot: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    collider_handling: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ComponentHandling>
    destroy_original: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    grabbable_handling: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ComponentHandling>
    include_inactive: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_baked: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_bake_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    skinned_mesh_mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    undoable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    update_order: FieldInt | None = None