"""Generated component: WebsocketConnect.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WebsocketConnect(GeneratedComponent):
    """WebsocketConnect component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketConnect
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketConnect"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "client": "Client",
        "enabled": "Enabled",
        "handling_user": "HandlingUser",
        "next": "Next",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "url": "URL",
    }

    client: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.WebsocketClient>
    enabled: FieldBool | None = None
    handling_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    url: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>