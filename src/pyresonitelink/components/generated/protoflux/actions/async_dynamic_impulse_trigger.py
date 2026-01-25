"""Generated component: AsyncDynamicImpulseTrigger.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AsyncDynamicImpulseTrigger(GeneratedComponent):
    """AsyncDynamicImpulseTrigger component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTrigger
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTrigger"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "persistent": "persistent",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None