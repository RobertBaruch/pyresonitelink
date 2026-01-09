"""Message types for ResoniteLink communication.

This module contains message classes used to send commands to Resonite.
"""

from dataclasses import dataclass

from .workers import Component, Slot


@dataclass
class Message:
    """Base class for all messages/commands sent to Resonite."""

    messageId: str | None = None


# =============================================================================
# Slot Messages
# =============================================================================


@dataclass
class GetSlot(Message):
    """Request to fetch slot data.

    Args:
        slotId: Unique ID of the slot to fetch. Use "Root" for the root slot.
        depth: How deep to fetch the hierarchy.
            0 = only the requested slot
            1 = include immediate children
            -1 = fetch everything
        includeComponentData: Whether to fetch full component data or just references.
    """

    slotId: str | None = None
    depth: int = 0
    includeComponentData: bool = False


@dataclass
class AddUpdateSlotData(Message):
    """Base for slot add/update messages."""

    data: Slot | None = None


@dataclass
class AddSlot(AddUpdateSlotData):
    """Request to add a new slot."""

    pass


@dataclass
class UpdateSlot(AddUpdateSlotData):
    """Request to update an existing slot."""

    pass


@dataclass
class RemoveSlot(Message):
    """Request to remove a slot.

    Args:
        slotId: The ID of the slot to remove.
    """

    slotId: str | None = None


# =============================================================================
# Component Messages
# =============================================================================


@dataclass
class GetComponent(Message):
    """Request to fetch component data.

    Args:
        componentId: The ID of the component to fetch.
    """

    componentId: str | None = None


@dataclass
class AddUpdateComponent(Message):
    """Base for component add/update messages."""

    data: Component | None = None


@dataclass
class AddComponent(AddUpdateComponent):
    """Request to add a new component to a slot.

    Args:
        containerSlotId: The ID of the slot to add the component to.
        data: The component data to add.
    """

    containerSlotId: str | None = None


@dataclass
class UpdateComponent(AddUpdateComponent):
    """Request to update an existing component."""

    pass


@dataclass
class RemoveComponent(Message):
    """Request to remove a component.

    Args:
        componentId: The ID of the component to remove.
    """

    componentId: str | None = None
