"""Generated component: AssetLoadProgress.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AssetLoadProgressBase(GeneratedComponent):
    """Base class for AssetLoadProgress<T> variants."""

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
class AssetLoadProgressITexture2D(AssetLoadProgressBase):
    """AssetLoadProgress<ITexture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.ITexture2D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.ITexture2D>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressTexture2D(AssetLoadProgressBase):
    """AssetLoadProgress<Texture2D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Texture2D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Texture2D>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressTexture3D(AssetLoadProgressBase):
    """AssetLoadProgress<Texture3D> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Texture3D>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Texture3D>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressCubemap(AssetLoadProgressBase):
    """AssetLoadProgress<Cubemap> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Cubemap>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Cubemap>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressVideoTexture(AssetLoadProgressBase):
    """AssetLoadProgress<VideoTexture> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.VideoTexture>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.VideoTexture>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressMesh(AssetLoadProgressBase):
    """AssetLoadProgress<Mesh> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Mesh>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Mesh>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressAudioClip(AssetLoadProgressBase):
    """AssetLoadProgress<AudioClip> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.AudioClip>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.AudioClip>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressShader(AssetLoadProgressBase):
    """AssetLoadProgress<Shader> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Shader>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Shader>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressAnimation(AssetLoadProgressBase):
    """AssetLoadProgress<Animation> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Animation>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Animation>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressFont(AssetLoadProgressBase):
    """AssetLoadProgress<Font> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.Font>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.Font>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


@dataclass
class AssetLoadProgressLocaleResource(AssetLoadProgressBase):
    """AssetLoadProgress<LocaleResource> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AssetLoadProgress<[FrooxEngine]FrooxEngine.LocaleResource>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "tracker": "Tracker",
        "user": "User",
    }

    tracker: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.UsersAssetLoadProgress<FrooxEngine.LocaleResource>>
    user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>


# Type alias for any AssetLoadProgress variant
AssetLoadProgress = (
    AssetLoadProgressITexture2D |
    AssetLoadProgressTexture2D |
    AssetLoadProgressTexture3D |
    AssetLoadProgressCubemap |
    AssetLoadProgressVideoTexture |
    AssetLoadProgressMesh |
    AssetLoadProgressAudioClip |
    AssetLoadProgressShader |
    AssetLoadProgressAnimation |
    AssetLoadProgressFont |
    AssetLoadProgressLocaleResource
)