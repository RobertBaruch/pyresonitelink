"""Generated component: ComposeFinger.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComposeFinger(GeneratedComponent):
    """ComposeFinger component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodes.ComposeFinger
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.BodyNodes.ComposeFinger"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "chirality": "Chirality",
        "enabled": "Enabled",
        "finger": "Finger",
        "persistent": "persistent",
        "segment": "Segment",
        "update_order": "UpdateOrder",
    }

    chirality: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    enabled: FieldBool | None = None
    finger: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.FingerType>
    persistent: FieldBool | None = None
    segment: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.FingerSegmentType>
    update_order: FieldInt | None = None