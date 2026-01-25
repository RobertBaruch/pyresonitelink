"""Generated component: ComposeBits_ushort.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComposeBits_ushort(GeneratedComponent):
    """ComposeBits_ushort component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_ushort
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_ushort"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "bit0": "Bit0",
        "bit1": "Bit1",
        "bit10": "Bit10",
        "bit11": "Bit11",
        "bit12": "Bit12",
        "bit13": "Bit13",
        "bit14": "Bit14",
        "bit15": "Bit15",
        "bit2": "Bit2",
        "bit3": "Bit3",
        "bit4": "Bit4",
        "bit5": "Bit5",
        "bit6": "Bit6",
        "bit7": "Bit7",
        "bit8": "Bit8",
        "bit9": "Bit9",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    bit0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None