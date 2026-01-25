"""Generated component: NearestUserHead.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class NearestUserHead(GeneratedComponent):
    """NearestUserHead component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.NearestUserHead
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.NearestUserHead"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "ignore_afk": "IgnoreAFK",
        "ignore_user": "IgnoreUser",
        "persistent": "persistent",
        "reference": "Reference",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    ignore_afk: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    ignore_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    persistent: FieldBool | None = None
    reference: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None