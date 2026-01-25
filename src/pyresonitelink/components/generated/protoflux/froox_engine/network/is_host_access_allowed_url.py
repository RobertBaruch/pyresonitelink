"""Generated component: IsHostAccessAllowedUrl.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class IsHostAccessAllowedUrl(GeneratedComponent):
    """IsHostAccessAllowedUrl component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.IsHostAccessAllowedUrl
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.IsHostAccessAllowedUrl"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "host": "Host",
        "persistent": "persistent",
        "scope": "Scope",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    host: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>
    persistent: FieldBool | None = None
    scope: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.HostAccessScope>
    update_order: FieldInt | None = None