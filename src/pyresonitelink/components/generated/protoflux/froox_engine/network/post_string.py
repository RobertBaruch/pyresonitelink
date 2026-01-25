"""Generated component: POST_String.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class POST_String(GeneratedComponent):
    """POST_String component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.POST_String
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.POST_String"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "media_type": "MediaType",
        "on_denied": "OnDenied",
        "on_error": "OnError",
        "on_response": "OnResponse",
        "on_sent": "OnSent",
        "persistent": "persistent",
        "string": "String",
        "update_order": "UpdateOrder",
        "url": "URL",
    }

    enabled: FieldBool | None = None
    media_type: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    on_denied: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_error: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_response: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_sent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    string: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None
    url: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>