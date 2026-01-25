"""Generated component: ComputeBoundingBox.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComputeBoundingBox(GeneratedComponent):
    """ComputeBoundingBox component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.ComputeBoundingBox
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.ComputeBoundingBox"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "coordinate_space": "CoordinateSpace",
        "enabled": "Enabled",
        "include_inactive": "IncludeInactive",
        "instance": "Instance",
        "only_with_tag": "OnlyWithTag",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    coordinate_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    enabled: FieldBool | None = None
    include_inactive: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    instance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    only_with_tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None