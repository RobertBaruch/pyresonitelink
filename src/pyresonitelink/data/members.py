"""Member types for ResoniteLink data model.

This module contains the Member base class and its derived types including
Reference, SyncList, SyncObject, EmptyElement, and FieldEnum.
"""

from dataclasses import dataclass, field


@dataclass
class Member:
    """Base class for all member types.

    Members are elements that belong to components or sync objects and can be
    referenced by their unique ID.
    """

    id: str | None = None


@dataclass
class Reference(Member):
    """A reference to another member or worker.

    References point to other elements in the data model by their ID.
    """

    targetId: str | None = None
    targetType: str | None = None


@dataclass
class SyncList(Member):
    """A synchronized list of members."""

    elements: list[Member] = field(default_factory=list[Member])


@dataclass
class SyncObject(Member):
    """A synchronized object containing named members."""

    members: dict[str, Member] = field(default_factory=dict[str, Member])


@dataclass
class EmptyElement(Member):
    """An empty placeholder element in a list."""


@dataclass
class FieldEnum(Member):
    """A field containing an enum value represented as a string."""

    value: str | None = None
    enumType: str | None = None
