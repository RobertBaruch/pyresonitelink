"""Generated component: LogN_Double3_Double.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class LogN_Double3_Double(GeneratedComponent):
    """LogN_Double3_Double component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.LogN_Double3_Double
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.LogN_Double3_Double"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base": "Base",
        "enabled": "Enabled",
        "n": "N",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    base: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    enabled: FieldBool | None = None
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None