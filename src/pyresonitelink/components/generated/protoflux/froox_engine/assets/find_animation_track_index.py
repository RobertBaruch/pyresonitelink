"""Generated component: FindAnimationTrackIndex.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FindAnimationTrackIndex(GeneratedComponent):
    """FindAnimationTrackIndex component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.FindAnimationTrackIndex
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.FindAnimationTrackIndex"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "animation": "Animation",
        "enabled": "Enabled",
        "node": "Node",
        "persistent": "persistent",
        "property": "Property",
        "update_order": "UpdateOrder",
    }

    animation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Animation>
    enabled: FieldBool | None = None
    node: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    property: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None