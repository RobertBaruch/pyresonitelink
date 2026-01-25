"""Generated component: IsControl.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class IsControl(GeneratedComponent):
    """IsControl component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.IsControl
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.IsControl"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "character": "Character",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    character: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None