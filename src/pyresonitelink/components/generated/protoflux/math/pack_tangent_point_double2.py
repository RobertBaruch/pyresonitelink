"""Generated component: PackTangentPointDouble2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackTangentPointDouble2(GeneratedComponent):
    """PackTangentPointDouble2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PackTangentPointDouble2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.PackTangentPointDouble2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "tangent": "Tangent",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    tangent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>