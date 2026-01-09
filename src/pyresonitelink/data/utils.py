"""Utility functions for the data module."""

from dataclasses import field
from typing import Any

# Metadata key for marking fields to ignore during JSON encoding/decoding
JSON_IGNORE_KEY = "__json_ignore__"


def json_ignore(**kwargs: Any) -> Any:
    """Create a dataclass field that is ignored during JSON encoding/decoding.

    This is a wrapper around dataclasses.field() that adds metadata to mark
    the field as ignored by the JSON codec.

    Args:
        **kwargs: Arguments passed to dataclasses.field() (e.g., default, default_factory).

    Returns:
        A dataclass field with json_ignore metadata.

    Example:
        @dataclass
        class MyMessage(Message):
            name: str = ""
            payload: bytearray = json_ignore(default_factory=bytearray)
    """
    metadata = kwargs.pop("metadata", {})
    metadata[JSON_IGNORE_KEY] = True
    return field(metadata=metadata, **kwargs)  # pylint: disable=invalid-field-call
