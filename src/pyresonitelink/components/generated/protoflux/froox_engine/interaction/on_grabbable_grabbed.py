"""Generated component: OnGrabbableGrabbed.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OnGrabbableGrabbed(GeneratedComponent):
    """OnGrabbableGrabbed component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableGrabbed
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableGrabbed"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "grabbable": "Grabbable",
        "on_grabbed": "OnGrabbed",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    grabbable: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.IGrabbable>
    on_grabbed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None