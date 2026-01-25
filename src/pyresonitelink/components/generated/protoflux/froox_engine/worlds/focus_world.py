"""Generated component: FocusWorld.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FocusWorld(GeneratedComponent):
    """FocusWorld component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.FocusWorld
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.FocusWorld"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "close_current": "CloseCurrent",
        "enabled": "Enabled",
        "on_fail": "OnFail",
        "on_focused": "OnFocused",
        "on_not_found": "OnNotFound",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "url": "URL",
        "world_link": "WorldLink",
    }

    close_current: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_focused: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    url: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>
    world_link: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.IWorldLink>