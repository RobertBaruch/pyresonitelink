"""Generated component: Cast_double3x3_To_double2x2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Cast_double3x3_To_double2x2(GeneratedComponent):
    """Cast_double3x3_To_double2x2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.Cast_double3x3_To_double2x2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.Cast_double3x3_To_double2x2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "input": "Input",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None