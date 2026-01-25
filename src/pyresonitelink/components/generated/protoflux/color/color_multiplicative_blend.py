"""Generated component: ColorMultiplicativeBlend.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ColorMultiplicativeBlend(GeneratedComponent):
    """ColorMultiplicativeBlend component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorMultiplicativeBlend
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Color.ColorMultiplicativeBlend"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "enabled": "Enabled",
        "persistent": "persistent",
        "source": "Source",
        "update_order": "UpdateOrder",
    }

    destination: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    update_order: FieldInt | None = None