"""Generated component: RenderToTextureAsset.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RenderToTextureAsset(GeneratedComponent):
    """RenderToTextureAsset component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.RenderToTextureAsset
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.RenderToTextureAsset"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "camera": "Camera",
        "enabled": "Enabled",
        "format": "Format",
        "on_failed": "OnFailed",
        "on_rendered": "OnRendered",
        "on_render_started": "OnRenderStarted",
        "persistent": "persistent",
        "quality": "Quality",
        "resolution": "Resolution",
        "update_order": "UpdateOrder",
    }

    camera: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Camera>
    enabled: FieldBool | None = None
    format: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_rendered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_render_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    quality: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    resolution: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    update_order: FieldInt | None = None