"""Generated component: SampleBooleanSpatialVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleBooleanSpatialVariable(GeneratedComponent):
    """SampleBooleanSpatialVariable component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleBooleanSpatialVariable
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleBooleanSpatialVariable"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "enabled": "Enabled",
        "mode": "Mode",
        "name": "Name",
        "persistent": "persistent",
        "point": "Point",
        "update_order": "UpdateOrder",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BooleanSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    persistent: FieldBool | None = None
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    update_order: FieldInt | None = None