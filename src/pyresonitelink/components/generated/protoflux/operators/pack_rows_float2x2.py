"""Generated component: PackRows_Float2x2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackRows_Float2x2(GeneratedComponent):
    """PackRows_Float2x2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackRows_Float2x2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackRows_Float2x2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "row0": "Row0",
        "row1": "Row1",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    row0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    row1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    update_order: FieldInt | None = None