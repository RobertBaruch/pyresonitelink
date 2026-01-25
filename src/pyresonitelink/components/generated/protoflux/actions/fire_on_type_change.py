"""Generated component: FireOnTypeChange.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FireOnTypeChange(GeneratedComponent):
    """FireOnTypeChange component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnTypeChange
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnTypeChange"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Type>