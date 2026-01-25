"""Generated component: BakeReflectionProbe.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BakeReflectionProbe(GeneratedComponent):
    """BakeReflectionProbe component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbe
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbe"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "on_bake_complete": "OnBakeComplete",
        "on_bake_fail": "OnBakeFail",
        "on_bake_start": "OnBakeStart",
        "persistent": "persistent",
        "probe": "Probe",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    on_bake_complete: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_bake_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_bake_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    probe: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.ReflectionProbe>
    update_order: FieldInt | None = None