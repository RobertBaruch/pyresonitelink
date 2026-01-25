"""Generated component: StaticLocaleProvider.

Auto-generated from FrooxEngine.StaticLocaleProvider.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt, FieldString, FieldUri


@dataclass
class StaticLocaleProvider(GeneratedComponent):
    """StaticLocaleProvider component.

    ResoniteLink schema for FrooxEngine.StaticLocaleProvider
    """

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.StaticLocaleProvider"
    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.StaticLocaleProvider.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "override_locale": "OverrideLocale",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "url": "URL",
    }

    enabled: FieldBool | None = None
    override_locale: FieldString | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    url: FieldUri | None = None