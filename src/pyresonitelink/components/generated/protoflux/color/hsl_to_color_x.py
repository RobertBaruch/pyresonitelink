"""Generated component: HSL_ToColorX.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class HSL_ToColorX(GeneratedComponent):
    """HSL_ToColorX component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSL_ToColorX
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.HSL_ToColorX"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "h": "H",
        "l": "L",
        "persistent": "persistent",
        "s": "S",
        "target_profile": "TargetProfile",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    h: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    l: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    s: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    target_profile: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ColorProfile>
    update_order: FieldInt | None = None