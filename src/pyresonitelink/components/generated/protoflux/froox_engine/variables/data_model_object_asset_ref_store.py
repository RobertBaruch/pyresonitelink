"""Generated component: DataModelObjectAssetRefStore.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class DataModelObjectAssetRefStoreBase(GeneratedComponent):
    """Base class for DataModelObjectAssetRefStore<T> variants."""

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
class DataModelObjectAssetRefStoreAnimation(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Animation> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Animation>"

    pass


@dataclass
class DataModelObjectAssetRefStoreAudioClip(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<AudioClip> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.AudioClip>"

    pass


@dataclass
class DataModelObjectAssetRefStoreBinary(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Binary> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Binary>"

    pass


@dataclass
class DataModelObjectAssetRefStoreCubemap(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Cubemap> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Cubemap>"

    pass


@dataclass
class DataModelObjectAssetRefStoreDesktopTexture(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<DesktopTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.DesktopTexture>"

    pass


@dataclass
class DataModelObjectAssetRefStoreDocument(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Document> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Document>"

    pass


@dataclass
class DataModelObjectAssetRefStoreFont(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Font> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Font>"

    pass


@dataclass
class DataModelObjectAssetRefStoreFontSet(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<FontSet> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.FontSet>"

    pass


@dataclass
class DataModelObjectAssetRefStoreGaussianSplat(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<GaussianSplat> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.GaussianSplat>"

    pass


@dataclass
class DataModelObjectAssetRefStoreLocaleResource(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<LocaleResource> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.LocaleResource>"

    pass


@dataclass
class DataModelObjectAssetRefStoreMaterial(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Material> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Material>"

    pass


@dataclass
class DataModelObjectAssetRefStoreMaterialPropertyBlock(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<MaterialPropertyBlock> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.MaterialPropertyBlock>"

    pass


@dataclass
class DataModelObjectAssetRefStoreMesh(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Mesh> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Mesh>"

    pass


@dataclass
class DataModelObjectAssetRefStorePointRenderBuffer(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<PointRenderBuffer> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.PointRenderBuffer>"

    pass


@dataclass
class DataModelObjectAssetRefStoreRenderTexture(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<RenderTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.RenderTexture>"

    pass


@dataclass
class DataModelObjectAssetRefStoreSavedObject(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<SavedObject> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.SavedObject>"

    pass


@dataclass
class DataModelObjectAssetRefStoreShader(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Shader> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Shader>"

    pass


@dataclass
class DataModelObjectAssetRefStoreSprite(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Sprite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Sprite>"

    pass


@dataclass
class DataModelObjectAssetRefStoreTexture2D(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Texture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Texture2D>"

    pass


@dataclass
class DataModelObjectAssetRefStoreTexture3D(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<Texture3D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.Texture3D>"

    pass


@dataclass
class DataModelObjectAssetRefStoreTrailsRenderBuffer(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<TrailsRenderBuffer> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.TrailsRenderBuffer>"

    pass


@dataclass
class DataModelObjectAssetRefStoreVideoTexture(DataModelObjectAssetRefStoreBase):
    """DataModelObjectAssetRefStore<VideoTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelObjectAssetRefStore<[FrooxEngine]FrooxEngine.VideoTexture>"

    pass


# Type alias for any DataModelObjectAssetRefStore variant
DataModelObjectAssetRefStore = (
    DataModelObjectAssetRefStoreAnimation |
    DataModelObjectAssetRefStoreAudioClip |
    DataModelObjectAssetRefStoreBinary |
    DataModelObjectAssetRefStoreCubemap |
    DataModelObjectAssetRefStoreDesktopTexture |
    DataModelObjectAssetRefStoreDocument |
    DataModelObjectAssetRefStoreFont |
    DataModelObjectAssetRefStoreFontSet |
    DataModelObjectAssetRefStoreGaussianSplat |
    DataModelObjectAssetRefStoreLocaleResource |
    DataModelObjectAssetRefStoreMaterial |
    DataModelObjectAssetRefStoreMaterialPropertyBlock |
    DataModelObjectAssetRefStoreMesh |
    DataModelObjectAssetRefStorePointRenderBuffer |
    DataModelObjectAssetRefStoreRenderTexture |
    DataModelObjectAssetRefStoreSavedObject |
    DataModelObjectAssetRefStoreShader |
    DataModelObjectAssetRefStoreSprite |
    DataModelObjectAssetRefStoreTexture2D |
    DataModelObjectAssetRefStoreTexture3D |
    DataModelObjectAssetRefStoreTrailsRenderBuffer |
    DataModelObjectAssetRefStoreVideoTexture
)