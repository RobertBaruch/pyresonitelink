"""Generated component: EncapsulatePoint.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EncapsulatePoint(GeneratedComponent):
    """EncapsulatePoint component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulatePoint
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulatePoint"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "bounds": "Bounds",
        "enabled": "Enabled",
        "persistent": "persistent",
        "point": "Point",
        "update_order": "UpdateOrder",
    }

    bounds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None