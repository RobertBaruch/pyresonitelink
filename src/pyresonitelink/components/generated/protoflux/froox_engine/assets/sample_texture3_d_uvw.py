"""Generated component: SampleTexture3D_UVW.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleTexture3D_UVW(GeneratedComponent):
    """SampleTexture3D_UVW component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture3D_UVW
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture3D_UVW"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "texture": "Texture",
        "update_order": "UpdateOrder",
        "uvw": "UVW",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    texture: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Texture3D>
    update_order: FieldInt | None = None
    uvw: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>