"""Generated component: ImpulseMultiplexer.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class ImpulseMultiplexer(GeneratedComponent):
    """ImpulseMultiplexer component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseMultiplexer
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ImpulseMultiplexer"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "impulses": "Impulses",
        "index": "Index",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    impulses: SyncList | None = None
    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None