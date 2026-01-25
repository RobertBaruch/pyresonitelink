"""Generated component: IsNaN_Float3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class IsNaN_Float3(GeneratedComponent):
    """IsNaN_Float3 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.IsNaN_Float3
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.IsNaN_Float3"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>