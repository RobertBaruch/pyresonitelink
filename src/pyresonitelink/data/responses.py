"""Response types for ResoniteLink communication.

This module contains response classes received from Resonite after sending messages.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

from .workers import Component, Slot


@dataclass
class Response:
    """Base response from Resonite.

    Indicates success/failure of a request and may contain error information.
    """

    sourceMessageId: str | None = None
    success: bool = False
    errorInfo: str | None = None


@dataclass
class SlotData(Response):
    """Response containing slot data.

    Returned when requesting slot information.
    """

    depth: int = 0
    data: Slot | None = None


@dataclass
class ComponentData(Response):
    """Response containing component data.

    Returned when requesting component information.
    """

    data: Component | None = None


@dataclass
class AssetData(Response):
    """Response containing asset data.

    Returned after importing an asset (e.g., texture).

    Args:
        assetURL: URL of the imported asset. This can be assigned to static
            asset providers. Note: Usually this URL is valid only within the
            session. It is NOT recommended to persist it outside of the
            ResoniteLink session - static asset providers will automatically
            update the URL when the world/item is saved.
    """

    assetURL: str | None = None
