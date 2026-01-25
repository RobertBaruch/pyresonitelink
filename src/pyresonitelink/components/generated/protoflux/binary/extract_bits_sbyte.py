"""Generated component: ExtractBits_sbyte.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ExtractBits_sbyte(GeneratedComponent):
    """ExtractBits_sbyte component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_sbyte
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ExtractBits_sbyte"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "integer": "Integer",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    integer: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None