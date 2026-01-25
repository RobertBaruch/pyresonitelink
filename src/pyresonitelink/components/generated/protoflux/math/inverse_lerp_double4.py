"""Generated component: InverseLerp_Double4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class InverseLerp_Double4(GeneratedComponent):
    """InverseLerp_Double4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.InverseLerp_Double4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.InverseLerp_Double4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "from_": "From",
        "persistent": "persistent",
        "to": "To",
        "update_order": "UpdateOrder",
        "value": "Value",
    }

    enabled: FieldBool | None = None
    from_: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    persistent: FieldBool | None = None
    to: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    update_order: FieldInt | None = None
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>