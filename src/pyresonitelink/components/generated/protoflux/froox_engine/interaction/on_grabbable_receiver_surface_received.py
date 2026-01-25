"""Generated component: OnGrabbableReceiverSurfaceReceived.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OnGrabbableReceiverSurfaceReceived(GeneratedComponent):
    """OnGrabbableReceiverSurfaceReceived component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReceiverSurfaceReceived
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReceiverSurfaceReceived"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_received": "OnReceived",
        "persistent": "persistent",
        "source": "Source",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_received: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.GrabbableReceiverSurface>
    update_order: FieldInt | None = None