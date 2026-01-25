"""Generated component: ComposeBits_uint.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComposeBits_uint(GeneratedComponent):
    """ComposeBits_uint component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_uint
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_uint"
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
        "bit16": "Bit16",
        "bit17": "Bit17",
        "bit18": "Bit18",
        "bit19": "Bit19",
        "bit2": "Bit2",
        "bit20": "Bit20",
        "bit21": "Bit21",
        "bit22": "Bit22",
        "bit23": "Bit23",
        "bit24": "Bit24",
        "bit25": "Bit25",
        "bit26": "Bit26",
        "bit27": "Bit27",
        "bit28": "Bit28",
        "bit29": "Bit29",
        "bit3": "Bit3",
        "bit30": "Bit30",
        "bit31": "Bit31",
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
    bit16: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit17: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit18: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit19: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit20: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit21: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit22: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit23: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit24: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit25: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit26: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit27: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit28: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit29: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit30: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit31: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None