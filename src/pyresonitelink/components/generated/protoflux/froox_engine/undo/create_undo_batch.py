"""Generated component: CreateUndoBatch.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class CreateUndoBatch(GeneratedComponent):
    """CreateUndoBatch component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateUndoBatch
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateUndoBatch"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create": "Create",
        "description": "Description",
        "enabled": "Enabled",
        "on_created": "OnCreated",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    create: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    description: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    enabled: FieldBool | None = None
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None