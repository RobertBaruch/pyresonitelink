"""Base for all components."""

from __future__ import annotations  # For forward references

import uuid
from dataclasses import dataclass, field

import numpy as np

from pyresonitelink.data.responses import ComponentData


def _generate_uuid() -> str:
    """Generate a random UUID v4 string.

    Returns:
        A new random UUID v4 as a string.
    """
    return str(uuid.uuid4())


@dataclass
class Component:
    """Base for all components.

    When constructed directly (not through deserialization), the id is
    automatically set to a random UUID v4.
    """

    id: str = field(default_factory=_generate_uuid)
    persistent: bool = True
    update_order: np.int32 = np.int32(0)
    enabled: bool = True

    @staticmethod
    def unmarshal(data: ComponentData) -> Component:
        assert data.data is not None
        assert data.data.componentType is not None
        if data.data.componentType.startswith("[FrooxEngine]FrooxEngine.ValueField<"):
            # Lazy import to avoid circular imports
            from pyresonitelink.components.valuefields.components import (
                ValueFieldComponent,
            )

            return ValueFieldComponent.unmarshal(data)
        raise NotImplementedError(f"Unknown component type: {data.data.componentType}")
