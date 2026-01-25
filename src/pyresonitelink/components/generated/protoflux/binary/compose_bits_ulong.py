"""Generated component: ComposeBits_ulong.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ComposeBits_ulong(GeneratedComponent):
    """ComposeBits_ulong component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_ulong
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Binary.ComposeBits_ulong"
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
        "bit32": "Bit32",
        "bit33": "Bit33",
        "bit34": "Bit34",
        "bit35": "Bit35",
        "bit36": "Bit36",
        "bit37": "Bit37",
        "bit38": "Bit38",
        "bit39": "Bit39",
        "bit4": "Bit4",
        "bit40": "Bit40",
        "bit41": "Bit41",
        "bit42": "Bit42",
        "bit43": "Bit43",
        "bit44": "Bit44",
        "bit45": "Bit45",
        "bit46": "Bit46",
        "bit47": "Bit47",
        "bit48": "Bit48",
        "bit49": "Bit49",
        "bit5": "Bit5",
        "bit50": "Bit50",
        "bit51": "Bit51",
        "bit52": "Bit52",
        "bit53": "Bit53",
        "bit54": "Bit54",
        "bit55": "Bit55",
        "bit56": "Bit56",
        "bit57": "Bit57",
        "bit58": "Bit58",
        "bit59": "Bit59",
        "bit6": "Bit6",
        "bit60": "Bit60",
        "bit61": "Bit61",
        "bit62": "Bit62",
        "bit63": "Bit63",
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
    bit32: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit33: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit34: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit35: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit36: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit37: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit38: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit39: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit40: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit41: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit42: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit43: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit44: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit45: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit46: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit47: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit48: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit49: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit50: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit51: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit52: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit53: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit54: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit55: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit56: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit57: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit58: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit59: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit60: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit61: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit62: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit63: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    bit9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None