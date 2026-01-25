"""Generated component: SurrogatePairToUTF32.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SurrogatePairToUTF32(GeneratedComponent):
    """SurrogatePairToUTF32 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.SurrogatePairToUTF32
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.SurrogatePairToUTF32"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "high_surrogate": "HighSurrogate",
        "low_surrogate": "LowSurrogate",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    high_surrogate: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    low_surrogate: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None