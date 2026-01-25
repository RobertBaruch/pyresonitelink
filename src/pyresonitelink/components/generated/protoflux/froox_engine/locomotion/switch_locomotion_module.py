"""Generated component: SwitchLocomotionModule.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SwitchLocomotionModule(GeneratedComponent):
    """SwitchLocomotionModule component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.SwitchLocomotionModule
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.SwitchLocomotionModule"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "exact_match": "ExactMatch",
        "module_name": "ModuleName",
        "on_not_found": "OnNotFound",
        "on_switched": "OnSwitched",
        "persistent": "persistent",
        "target_user": "TargetUser",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    exact_match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    module_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_switched: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    target_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    update_order: FieldInt | None = None