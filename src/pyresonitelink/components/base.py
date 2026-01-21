"""Base for all components."""

from __future__ import annotations  # For forward references
from dataclasses import dataclass

import numpy as np

from pyresonitelink.data.responses import ComponentData

@dataclass
class Component:
    """Base for all components."""

    id: str
    persistent: bool
    update_order: np.int32
    enabled: bool

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
