"""Generated component: AsyncRangeLoopInt.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AsyncRangeLoopInt(GeneratedComponent):
    """AsyncRangeLoopInt component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncRangeLoopInt
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncRangeLoopInt"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "end": "End",
        "loop_end": "LoopEnd",
        "loop_iteration": "LoopIteration",
        "loop_start": "LoopStart",
        "persistent": "persistent",
        "start": "Start",
        "step_size": "StepSize",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    end: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    loop_end: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    loop_iteration: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    loop_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    step_size: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None