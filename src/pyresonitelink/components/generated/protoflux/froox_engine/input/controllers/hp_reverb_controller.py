"""Generated component: HPReverbController.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class HPReverbController(GeneratedComponent):
    """HPReverbController component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.HPReverbController
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Controllers.HPReverbController"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "node": "Node",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "user": "User",
    }

    enabled: FieldBool | None = None
    node: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>