"""Generated component: GetAsset.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class GetAssetBase(GeneratedComponent):
    """Base class for GetAsset<T> variants."""

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
class GetAssetAnimation(GetAssetBase):
    """GetAsset<Animation> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Animation>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Animation>>


@dataclass
class GetAssetAudioClip(GetAssetBase):
    """GetAsset<AudioClip> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.AudioClip>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.AudioClip>>


@dataclass
class GetAssetBinary(GetAssetBase):
    """GetAsset<Binary> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Binary>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Binary>>


@dataclass
class GetAssetCubemap(GetAssetBase):
    """GetAsset<Cubemap> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Cubemap>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Cubemap>>


@dataclass
class GetAssetDesktopTexture(GetAssetBase):
    """GetAsset<DesktopTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.DesktopTexture>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.DesktopTexture>>


@dataclass
class GetAssetDocument(GetAssetBase):
    """GetAsset<Document> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Document>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Document>>


@dataclass
class GetAssetFont(GetAssetBase):
    """GetAsset<Font> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Font>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Font>>


@dataclass
class GetAssetFontSet(GetAssetBase):
    """GetAsset<FontSet> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.FontSet>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.FontSet>>


@dataclass
class GetAssetGaussianSplat(GetAssetBase):
    """GetAsset<GaussianSplat> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.GaussianSplat>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.GaussianSplat>>


@dataclass
class GetAssetLocaleResource(GetAssetBase):
    """GetAsset<LocaleResource> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.LocaleResource>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.LocaleResource>>


@dataclass
class GetAssetMaterial(GetAssetBase):
    """GetAsset<Material> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Material>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Material>>


@dataclass
class GetAssetMaterialPropertyBlock(GetAssetBase):
    """GetAsset<MaterialPropertyBlock> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.MaterialPropertyBlock>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.MaterialPropertyBlock>>


@dataclass
class GetAssetMesh(GetAssetBase):
    """GetAsset<Mesh> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Mesh>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Mesh>>


@dataclass
class GetAssetPointRenderBuffer(GetAssetBase):
    """GetAsset<PointRenderBuffer> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.PointRenderBuffer>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.PointRenderBuffer>>


@dataclass
class GetAssetRenderTexture(GetAssetBase):
    """GetAsset<RenderTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.RenderTexture>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.RenderTexture>>


@dataclass
class GetAssetSavedObject(GetAssetBase):
    """GetAsset<SavedObject> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.SavedObject>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.SavedObject>>


@dataclass
class GetAssetShader(GetAssetBase):
    """GetAsset<Shader> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Shader>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Shader>>


@dataclass
class GetAssetSprite(GetAssetBase):
    """GetAsset<Sprite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Sprite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Sprite>>


@dataclass
class GetAssetTexture2D(GetAssetBase):
    """GetAsset<Texture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Texture2D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Texture2D>>


@dataclass
class GetAssetTexture3D(GetAssetBase):
    """GetAsset<Texture3D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.Texture3D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.Texture3D>>


@dataclass
class GetAssetTrailsRenderBuffer(GetAssetBase):
    """GetAsset<TrailsRenderBuffer> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.TrailsRenderBuffer>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.TrailsRenderBuffer>>


@dataclass
class GetAssetVideoTexture(GetAssetBase):
    """GetAsset<VideoTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<[FrooxEngine]FrooxEngine.VideoTexture>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "provider": "Provider",
    }

    provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IAssetProvider<FrooxEngine.VideoTexture>>


# Type alias for any GetAsset variant
GetAsset = (
    GetAssetAnimation |
    GetAssetAudioClip |
    GetAssetBinary |
    GetAssetCubemap |
    GetAssetDesktopTexture |
    GetAssetDocument |
    GetAssetFont |
    GetAssetFontSet |
    GetAssetGaussianSplat |
    GetAssetLocaleResource |
    GetAssetMaterial |
    GetAssetMaterialPropertyBlock |
    GetAssetMesh |
    GetAssetPointRenderBuffer |
    GetAssetRenderTexture |
    GetAssetSavedObject |
    GetAssetShader |
    GetAssetSprite |
    GetAssetTexture2D |
    GetAssetTexture3D |
    GetAssetTrailsRenderBuffer |
    GetAssetVideoTexture
)