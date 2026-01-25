"""Generated component: NAND_Multi_Int4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import SyncList


@dataclass
class NAND_Multi_Int4(GeneratedComponent):
    """NAND_Multi_Int4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.NAND_Multi_Int4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.NAND_Multi_Int4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "operands": "Operands",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    operands: SyncList | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None