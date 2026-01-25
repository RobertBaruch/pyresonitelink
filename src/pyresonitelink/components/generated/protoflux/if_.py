"""Generated component: If.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class If(GeneratedComponent):
    """If component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.If
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.If"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "enabled": "Enabled",
        "on_false": "OnFalse",
        "on_true": "OnTrue",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    condition: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    on_false: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_true: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None