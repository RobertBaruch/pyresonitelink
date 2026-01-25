"""Generated component: WebsocketTextMessageSender.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WebsocketTextMessageSender(GeneratedComponent):
    """WebsocketTextMessageSender component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketTextMessageSender
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketTextMessageSender"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "client": "Client",
        "data": "Data",
        "enabled": "Enabled",
        "on_send_error": "OnSendError",
        "on_send_start": "OnSendStart",
        "on_sent": "OnSent",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    client: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.WebsocketClient>
    data: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    enabled: FieldBool | None = None
    on_send_error: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_send_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_sent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None