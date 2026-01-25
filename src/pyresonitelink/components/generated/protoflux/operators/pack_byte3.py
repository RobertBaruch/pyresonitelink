"""Generated component: Pack_Byte3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Pack_Byte3(GeneratedComponent):
    """Pack_Byte3 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Byte3
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_Byte3"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "x": "X",
        "y": "Y",
        "z": "Z",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    y: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    z: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>