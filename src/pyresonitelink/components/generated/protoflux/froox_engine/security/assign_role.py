"""Generated component: AssignRole.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AssignRole(GeneratedComponent):
    """AssignRole component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.AssignRole
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.AssignRole"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "handle": "Handle",
        "next": "Next",
        "persistent": "persistent",
        "role_name": "RoleName",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    handle: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.JoinRequestHandle>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    role_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None