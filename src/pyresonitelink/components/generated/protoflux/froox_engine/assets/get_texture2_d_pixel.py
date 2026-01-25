"""Generated component: GetTexture2D_Pixel.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class GetTexture2D_Pixel(GeneratedComponent):
    """GetTexture2D_Pixel component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetTexture2D_Pixel
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetTexture2D_Pixel"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "mip_level": "MipLevel",
        "persistent": "persistent",
        "position": "Position",
        "texture": "Texture",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    mip_level: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    persistent: FieldBool | None = None
    position: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    texture: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Texture2D>
    update_order: FieldInt | None = None