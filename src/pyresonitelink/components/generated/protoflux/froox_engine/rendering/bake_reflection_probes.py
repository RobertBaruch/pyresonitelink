"""Generated component: BakeReflectionProbes.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BakeReflectionProbes(GeneratedComponent):
    """BakeReflectionProbes component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbes
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbes"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "bake_inactive": "BakeInactive",
        "delay_before_bake": "DelayBeforeBake",
        "enabled": "Enabled",
        "filter_with_tag": "FilterWithTag",
        "on_bake_batch_finished": "OnBakeBatchFinished",
        "on_bake_batch_start": "OnBakeBatchStart",
        "on_before_probe_bake": "OnBeforeProbeBake",
        "on_probe_baked": "OnProbeBaked",
        "persistent": "persistent",
        "root": "Root",
        "update_order": "UpdateOrder",
    }

    bake_inactive: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    delay_before_bake: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    filter_with_tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    on_bake_batch_finished: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_bake_batch_start: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_before_probe_bake: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_probe_baked: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    root: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    update_order: FieldInt | None = None