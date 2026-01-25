"""Generated component: StartAsyncTask.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class StartAsyncTask(GeneratedComponent):
    """StartAsyncTask component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.StartAsyncTask
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.StartAsyncTask"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_failed": "OnFailed",
        "on_started": "OnStarted",
        "persistent": "persistent",
        "task_start": "TaskStart",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    task_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    update_order: FieldInt | None = None