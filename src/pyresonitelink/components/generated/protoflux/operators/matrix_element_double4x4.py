"""Generated component: MatrixElement_Double4x4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class MatrixElement_Double4x4(GeneratedComponent):
    """MatrixElement_Double4x4 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.MatrixElement_Double4x4
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.MatrixElement_Double4x4"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "column": "Column",
        "enabled": "Enabled",
        "matrix": "Matrix",
        "persistent": "persistent",
        "row": "Row",
        "update_order": "UpdateOrder",
    }

    column: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    enabled: FieldBool | None = None
    matrix: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    persistent: FieldBool | None = None
    row: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    update_order: FieldInt | None = None