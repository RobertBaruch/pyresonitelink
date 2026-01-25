"""Generated component: UserFromUsername.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UserFromUsername(GeneratedComponent):
    """UserFromUsername component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserFromUsername
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserFromUsername"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "allow_partial_match": "AllowPartialMatch",
        "enabled": "Enabled",
        "ignore_case": "IgnoreCase",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "username": "Username",
    }

    allow_partial_match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    ignore_case: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    username: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>