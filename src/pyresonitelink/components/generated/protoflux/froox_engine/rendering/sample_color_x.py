"""Generated component: SampleColorX.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleColorX(GeneratedComponent):
    """SampleColorX component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.SampleColorX
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.SampleColorX"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "direction": "Direction",
        "enabled": "Enabled",
        "far_clip": "FarClip",
        "near_clip": "NearClip",
        "on_sampled": "OnSampled",
        "on_sample_start": "OnSampleStart",
        "persistent": "persistent",
        "point": "Point",
        "reference": "Reference",
        "update_order": "UpdateOrder",
    }

    direction: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    enabled: FieldBool | None = None
    far_clip: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    near_clip: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    on_sampled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_sample_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    reference: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None