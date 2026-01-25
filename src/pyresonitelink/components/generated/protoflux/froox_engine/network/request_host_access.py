"""Generated component: RequestHostAccess.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RequestHostAccess(GeneratedComponent):
    """RequestHostAccess component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.RequestHostAccess
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.RequestHostAccess"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "host": "Host",
        "on_denied": "OnDenied",
        "on_granted": "OnGranted",
        "on_ignored": "OnIgnored",
        "persistent": "persistent",
        "port": "Port",
        "reason": "Reason",
        "scope": "Scope",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    host: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    on_denied: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_granted: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_ignored: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    port: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    reason: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    scope: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.HostAccessScope>
    update_order: FieldInt | None = None