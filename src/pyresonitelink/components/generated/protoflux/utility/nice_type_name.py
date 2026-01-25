"""Generated component: NiceTypeName.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class NiceTypeName(GeneratedComponent):
    """NiceTypeName component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.NiceTypeName
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.NiceTypeName"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "close_symbol": "CloseSymbol",
        "enabled": "Enabled",
        "open_symbol": "OpenSymbol",
        "persistent": "persistent",
        "type": "Type",
        "update_order": "UpdateOrder",
    }

    close_symbol: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    enabled: FieldBool | None = None
    open_symbol: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    type: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Type>
    update_order: FieldInt | None = None