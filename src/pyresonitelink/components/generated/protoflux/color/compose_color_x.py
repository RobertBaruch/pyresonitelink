"""Generated component: ComposeColorX.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComposeColorX(GeneratedComponent):
    """ComposeColorX component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ComposeColorX
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ComposeColorX"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_color": "BaseColor",
        "enabled": "Enabled",
        "persistent": "persistent",
        "profile": "Profile",
        "update_order": "UpdateOrder",
    }

    base_color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    profile: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ColorProfile>
    update_order: FieldInt | None = None