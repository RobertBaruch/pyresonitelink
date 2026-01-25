"""Generated component: ConstructZitaParameters.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ConstructZitaParameters(GeneratedComponent):
    """ConstructZitaParameters component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.ConstructZitaParameters
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.ConstructZitaParameters"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "crossover": "Crossover",
        "enabled": "Enabled",
        "eq1frequency": "EQ1Frequency",
        "eq1level": "EQ1Level",
        "eq2frequency": "EQ2Frequency",
        "eq2level": "EQ2Level",
        "high_frequency_damping": "HighFrequencyDamping",
        "in_delay": "InDelay",
        "level": "Level",
        "mix": "Mix",
        "persistent": "persistent",
        "rt60low": "RT60Low",
        "rt60mid": "RT60Mid",
        "update_order": "UpdateOrder",
    }

    crossover: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    enabled: FieldBool | None = None
    eq1frequency: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    eq1level: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    eq2frequency: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    eq2level: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    high_frequency_damping: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    in_delay: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    level: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    mix: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    persistent: FieldBool | None = None
    rt60low: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    rt60mid: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    update_order: FieldInt | None = None