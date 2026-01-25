"""Generated component: While.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class While(GeneratedComponent):
    """While component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.While
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.While"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "condition": "Condition",
        "enabled": "Enabled",
        "loop_end": "LoopEnd",
        "loop_iteration": "LoopIteration",
        "loop_start": "LoopStart",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    condition: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    loop_end: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    loop_iteration: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    loop_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None