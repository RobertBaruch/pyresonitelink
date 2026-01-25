"""Generated component: ApproximatelyNot_Double.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ApproximatelyNot_Double(GeneratedComponent):
    """ApproximatelyNot_Double component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ApproximatelyNot_Double
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ApproximatelyNot_Double"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
        "b": "B",
        "enabled": "Enabled",
        "epsilon": "Epsilon",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    b: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    enabled: FieldBool | None = None
    epsilon: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None