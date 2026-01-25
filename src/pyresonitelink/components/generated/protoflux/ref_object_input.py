"""Generated component: RefObjectInput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class RefObjectInputBase(GeneratedComponent):
    """Base class for RefObjectInput<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class RefObjectInputSlot(RefObjectInputBase):
    """RefObjectInput<Slot> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.RefObjectInput<[FrooxEngine]FrooxEngine.Slot>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.Slot


@dataclass
class RefObjectInputUser(RefObjectInputBase):
    """RefObjectInput<User> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.RefObjectInput<[FrooxEngine]FrooxEngine.User>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "target": "Target",
    }

    target: Reference | None = None  # -> FrooxEngine.User


# Type alias for any RefObjectInput variant
RefObjectInput = RefObjectInputSlot | RefObjectInputUser