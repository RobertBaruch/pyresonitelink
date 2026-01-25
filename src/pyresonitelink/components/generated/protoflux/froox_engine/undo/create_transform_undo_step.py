"""Generated component: CreateTransformUndoStep.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class CreateTransformUndoStep(GeneratedComponent):
    """CreateTransformUndoStep component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateTransformUndoStep
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateTransformUndoStep"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "save_parent": "SaveParent",
        "save_position": "SavePosition",
        "save_rotation": "SaveRotation",
        "save_scale": "SaveScale",
        "target": "Target",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    save_parent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    save_position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    save_rotation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    save_scale: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None