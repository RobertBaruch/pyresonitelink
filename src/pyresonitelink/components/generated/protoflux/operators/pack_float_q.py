"""Generated component: Pack_FloatQ.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Pack_FloatQ(GeneratedComponent):
    """Pack_FloatQ component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_FloatQ
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Pack_FloatQ"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "w": "W",
        "x": "X",
        "y": "Y",
        "z": "Z",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    w: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    x: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    y: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    z: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>