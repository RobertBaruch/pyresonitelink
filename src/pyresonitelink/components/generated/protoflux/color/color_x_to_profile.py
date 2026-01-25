"""Generated component: ColorXToProfile.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ColorXToProfile(GeneratedComponent):
    """ColorXToProfile component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXToProfile
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXToProfile"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "enabled": "Enabled",
        "persistent": "persistent",
        "profile": "Profile",
        "update_order": "UpdateOrder",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    profile: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ColorProfile>
    update_order: FieldInt | None = None