"""Generated component: MultiCosineLerp_Double2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class MultiCosineLerp_Double2(GeneratedComponent):
    """MultiCosineLerp_Double2 component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.MultiCosineLerp_Double2
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.MultiCosineLerp_Double2"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "lerp": "Lerp",
        "operands": "Operands",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None