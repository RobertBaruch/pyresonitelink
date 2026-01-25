"""Generated component: PackColumns_Double3x3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackColumns_Double3x3(GeneratedComponent):
    """PackColumns_Double3x3 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackColumns_Double3x3
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.PackColumns_Double3x3"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "column0": "Column0",
        "column1": "Column1",
        "column2": "Column2",
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    column0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    column1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    column2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None