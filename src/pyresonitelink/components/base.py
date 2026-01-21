"""Base for all components."""

from dataclasses import dataclass

import numpy as np

@dataclass
class Component:
    """Base for all components."""

    id: str
    persistent: bool
    update_order: np.int32
    enabled: bool
