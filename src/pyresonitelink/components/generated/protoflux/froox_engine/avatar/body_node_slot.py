"""Generated component: BodyNodeSlot.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BodyNodeSlot(GeneratedComponent):
    """BodyNodeSlot component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodeSlot
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodeSlot"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "node": "Node",
        "persistent": "persistent",
        "source": "Source",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    node: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    persistent: FieldBool | None = None
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    update_order: FieldInt | None = None