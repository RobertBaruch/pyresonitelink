"""Generated component: NearestUserFoot.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class NearestUserFoot(GeneratedComponent):
    """NearestUserFoot component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.NearestUserFoot
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.NearestUserFoot"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "get_left": "GetLeft",
        "get_right": "GetRight",
        "ignore_afk": "IgnoreAFK",
        "ignore_user": "IgnoreUser",
        "persistent": "persistent",
        "reference": "Reference",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    get_left: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    get_right: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    ignore_afk: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    ignore_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    persistent: FieldBool | None = None
    reference: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None