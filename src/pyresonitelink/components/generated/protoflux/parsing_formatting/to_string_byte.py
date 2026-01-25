"""Generated component: ToString_Byte.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ToString_Byte(GeneratedComponent):
    """ToString_Byte component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_Byte
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ParsingFormatting.ToString_Byte"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "format": "Format",
        "format_provider": "FormatProvider",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "v": "V",
    }

    enabled: FieldBool | None = None
    format: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_provider: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.IFormatProvider>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    v: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>