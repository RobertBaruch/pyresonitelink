"""Generated component: AllowJoin.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AllowJoin(GeneratedComponent):
    """AllowJoin component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.AllowJoin
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.AllowJoin"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "handle": "Handle",
        "next": "Next",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    handle: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.JoinRequestHandle>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None