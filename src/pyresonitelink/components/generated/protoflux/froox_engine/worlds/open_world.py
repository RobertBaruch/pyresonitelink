"""Generated component: OpenWorld.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class OpenWorld(GeneratedComponent):
    """OpenWorld component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.OpenWorld
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.OpenWorld"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "auto_focus": "AutoFocus",
        "enabled": "Enabled",
        "get_existing": "GetExisting",
        "loading_indicator": "LoadingIndicator",
        "make_private": "MakePrivate",
        "on_open_done": "OnOpenDone",
        "on_open_fail": "OnOpenFail",
        "on_open_start": "OnOpenStart",
        "on_world_ready": "OnWorldReady",
        "persistent": "persistent",
        "relation": "Relation",
        "update_order": "UpdateOrder",
        "url": "URL",
        "world_link": "WorldLink",
    }

    auto_focus: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    get_existing: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    loading_indicator: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    make_private: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_open_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_open_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_open_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_world_ready: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    relation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Userspace+WorldRelation>
    update_order: FieldInt | None = None
    url: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>
    world_link: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IWorldLink>