"""Generated component: VisemeAnalyzer.

Auto-generated from FrooxEngine.VisemeAnalyzer.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldFloat, FieldInt
from pyresonitelink.data.members import EmptyElement, FieldEnum, Reference


@dataclass
class VisemeAnalyzer(GeneratedComponent):
    """VisemeAnalyzer component.

    ResoniteLink schema for FrooxEngine.VisemeAnalyzer
    """

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.VisemeAnalyzer"
    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.VisemeAnalyzer.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "aa": "aa",
        "ch": "CH",
        "dd": "DD",
        "e": "E",
        "enabled": "Enabled",
        "ff": "FF",
        "ih": "ih",
        "kk": "kk",
        "laughter_probability": "LaughterProbability",
        "nn": "nn",
        "oh": "oh",
        "ou": "ou",
        "persistent": "persistent",
        "pp": "PP",
        "preferred_analyzer": "PreferredAnalyzer",
        "remote_source": "RemoteSource",
        "rr": "RR",
        "silence": "Silence",
        "smoothing": "Smoothing",
        "source": "Source",
        "ss": "SS",
        "th": "TH",
        "update_order": "UpdateOrder",
    }

    aa: EmptyElement | None = None
    ch: EmptyElement | None = None
    dd: EmptyElement | None = None
    e: EmptyElement | None = None
    enabled: FieldBool | None = None
    ff: EmptyElement | None = None
    ih: EmptyElement | None = None
    kk: EmptyElement | None = None
    laughter_probability: EmptyElement | None = None
    nn: EmptyElement | None = None
    oh: EmptyElement | None = None
    ou: EmptyElement | None = None
    persistent: FieldBool | None = None
    pp: EmptyElement | None = None
    preferred_analyzer: FieldEnum | None = None  # VisemeAnalyzerEngine
    remote_source: Reference | None = None  # -> FrooxEngine.MultiValueStream<float>
    rr: EmptyElement | None = None
    silence: EmptyElement | None = None
    smoothing: FieldFloat | None = None
    source: Reference | None = None  # -> FrooxEngine.IWorldAudioDataSource
    ss: EmptyElement | None = None
    th: EmptyElement | None = None
    update_order: FieldInt | None = None