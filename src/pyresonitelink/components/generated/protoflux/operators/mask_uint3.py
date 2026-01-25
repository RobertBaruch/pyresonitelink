"""Generated component: Mask_Uint3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Mask_Uint3(GeneratedComponent):
    """Mask_Uint3 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Mask_Uint3
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Mask_Uint3"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "mask": "Mask",
        "on_false": "OnFalse",
        "on_true": "OnTrue",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    mask: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    on_false: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    on_true: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None