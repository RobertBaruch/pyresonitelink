"""Generated component: ColorXToHexCode.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ColorXToHexCode(GeneratedComponent):
    """ColorXToHexCode component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXToHexCode
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXToHexCode"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "color": "Color",
        "enabled": "Enabled",
        "include_alpha": "IncludeAlpha",
        "persistent": "persistent",
        "prefix": "Prefix",
        "short_form": "ShortForm",
        "update_order": "UpdateOrder",
    }

    color: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    enabled: FieldBool | None = None
    include_alpha: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    persistent: FieldBool | None = None
    prefix: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    short_form: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    update_order: FieldInt | None = None