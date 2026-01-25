"""Generated component: Slerp_doubleQ.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Slerp_doubleQ(GeneratedComponent):
    """Slerp_doubleQ component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.Slerp_doubleQ
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quaternions.Slerp_doubleQ"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "from_": "From",
        "lerp": "Lerp",
        "persistent": "persistent",
        "to": "To",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    update_order: FieldInt | None = None