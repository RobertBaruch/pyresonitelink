"""Generated component: AssetInput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AssetInputBase(GeneratedComponent):
    """Base class for AssetInput<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class AssetInputITexture2D(AssetInputBase):
    """AssetInput<ITexture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AssetInput<[FrooxEngine]FrooxEngine.ITexture2D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.IAssetProvider<FrooxEngine.ITexture2D>


@dataclass
class AssetInputTexture2D(AssetInputBase):
    """AssetInput<Texture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AssetInput<[FrooxEngine]FrooxEngine.Texture2D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.IAssetProvider<FrooxEngine.Texture2D>


@dataclass
class AssetInputAudioClip(AssetInputBase):
    """AssetInput<AudioClip> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AssetInput<[FrooxEngine]FrooxEngine.AudioClip>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.IAssetProvider<FrooxEngine.AudioClip>


@dataclass
class AssetInputVideoTexture(AssetInputBase):
    """AssetInput<VideoTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AssetInput<[FrooxEngine]FrooxEngine.VideoTexture>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.IAssetProvider<FrooxEngine.VideoTexture>


@dataclass
class AssetInputMesh(AssetInputBase):
    """AssetInput<Mesh> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AssetInput<[FrooxEngine]FrooxEngine.Mesh>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.IAssetProvider<FrooxEngine.Mesh>


# Type alias for any AssetInput variant
AssetInput = (
    AssetInputITexture2D |
    AssetInputTexture2D |
    AssetInputAudioClip |
    AssetInputVideoTexture |
    AssetInputMesh
)