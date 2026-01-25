"""Generated component: LocalLeakyImpulseBucket.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class LocalLeakyImpulseBucket(GeneratedComponent):
    """LocalLeakyImpulseBucket component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalLeakyImpulseBucket
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.LocalLeakyImpulseBucket"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "interval": "Interval",
        "maximum_capacity": "MaximumCapacity",
        "overflow": "Overflow",
        "persistent": "persistent",
        "pulse": "Pulse",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    interval: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    maximum_capacity: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    overflow: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    pulse: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None