"""Generated component: CreateSpawnUndoStep.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class CreateSpawnUndoStep(GeneratedComponent):
    """CreateSpawnUndoStep component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateSpawnUndoStep
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateSpawnUndoStep"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "description": "Description",
        "enabled": "Enabled",
        "next": "Next",
        "persistent": "persistent",
        "target": "Target",
        "update_order": "UpdateOrder",
    }

    description: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    enabled: FieldBool | None = None
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None