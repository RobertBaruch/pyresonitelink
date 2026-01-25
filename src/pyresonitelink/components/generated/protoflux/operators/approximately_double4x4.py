"""Generated component: Approximately_Double4x4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class Approximately_Double4x4(GeneratedComponent):
    """Approximately_Double4x4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Approximately_Double4x4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.Approximately_Double4x4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "b": "B",
        "enabled": "Enabled",
        "epsilon": "Epsilon",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    b: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    enabled: FieldBool | None = None
    epsilon: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None