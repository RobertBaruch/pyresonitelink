"""Generated component: TwitchRewardRedeemEvent.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TwitchRewardRedeemEvent(GeneratedComponent):
    """TwitchRewardRedeemEvent component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchRewardRedeemEvent
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.Twitch.TwitchRewardRedeemEvent"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "interface": "Interface",
        "on_redeem": "OnRedeem",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    interface: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.TwitchInterface>
    on_redeem: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None