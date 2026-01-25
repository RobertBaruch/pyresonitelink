"""Generated component: SampleTexture2D_UV.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleTexture2D_UV(GeneratedComponent):
    """SampleTexture2D_UV component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture2D_UV
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.SampleTexture2D_UV"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "texture": "Texture",
        "update_order": "UpdateOrder",
        "uv": "UV",
        "wrap_mode": "WrapMode",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    texture: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Texture2D>
    update_order: FieldInt | None = None
    uv: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    wrap_mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Elements.Assets]Elements.Assets.WrapMode>