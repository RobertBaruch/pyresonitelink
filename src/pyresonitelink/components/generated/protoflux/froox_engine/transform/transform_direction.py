"""Generated component: TransformDirection.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TransformDirection(GeneratedComponent):
    """TransformDirection component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.TransformDirection
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.TransformDirection"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "from_space": "FromSpace",
        "persistent": "persistent",
        "source_direction": "SourceDirection",
        "to_space": "ToSpace",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    from_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    persistent: FieldBool | None = None
    source_direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    to_space: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None