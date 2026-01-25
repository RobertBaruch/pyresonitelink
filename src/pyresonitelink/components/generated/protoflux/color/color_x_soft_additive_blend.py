"""Generated component: ColorXSoftAdditiveBlend.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ColorXSoftAdditiveBlend(GeneratedComponent):
    """ColorXSoftAdditiveBlend component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXSoftAdditiveBlend
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorXSoftAdditiveBlend"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
        "persistent": "persistent",
        "source": "Source",
        "update_order": "UpdateOrder",
    }

    destination: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    update_order: FieldInt | None = None