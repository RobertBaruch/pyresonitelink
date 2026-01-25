"""Generated component: EncapsulateBounds.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EncapsulateBounds(GeneratedComponent):
    """EncapsulateBounds component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulateBounds
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.EncapsulateBounds"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "bounds": "Bounds",
        "enabled": "Enabled",
        "other_bounds": "OtherBounds",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    bounds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>
    enabled: FieldBool | None = None
    other_bounds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None