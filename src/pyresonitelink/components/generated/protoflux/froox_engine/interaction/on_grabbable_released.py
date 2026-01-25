"""Generated component: OnGrabbableReleased.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OnGrabbableReleased(GeneratedComponent):
    """OnGrabbableReleased component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReleased
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.OnGrabbableReleased"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "grabbable": "Grabbable",
        "on_released": "OnReleased",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    grabbable: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.IGrabbable>
    on_released: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None