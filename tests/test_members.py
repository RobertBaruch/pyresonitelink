"""Unit tests for the members module."""

# pylint: disable=missing-function-docstring,missing-class-docstring

import re
from typing import Any

import numpy as np

from pyresonitelink.data import (
    FieldBool,
    FieldFloat,
    FieldInt,
    FieldString,
    Reference,
    decode,
)
from pyresonitelink.data.members import (
    EmptyElement,
    FieldEnum,
    Member,
    SyncList,
    SyncObject,
)

# UUID v4 pattern: 8-4-4-4-12 hex chars, with version 4 in 3rd group
# and variant bits (8, 9, a, b) in 4th group
UUID_V4_PATTERN = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


def _is_valid_uuid_v4(value: str) -> bool:
    """Check if a string is a valid UUID v4."""
    return bool(UUID_V4_PATTERN.match(value))


class TestMemberUuidGeneration:
    """Tests for automatic UUID v4 generation on Member and subclasses."""

    def test_member_generates_uuid_v4(self) -> None:
        member = Member()
        assert _is_valid_uuid_v4(member.id)

    def test_field_bool_generates_uuid_v4(self) -> None:
        field = FieldBool(value=True)
        assert _is_valid_uuid_v4(field.id)

    def test_field_int_generates_uuid_v4(self) -> None:
        field = FieldInt(value=np.int32(42))
        assert _is_valid_uuid_v4(field.id)

    def test_field_float_generates_uuid_v4(self) -> None:
        field = FieldFloat(value=np.float32(3.14))
        assert _is_valid_uuid_v4(field.id)

    def test_field_string_generates_uuid_v4(self) -> None:
        field = FieldString(value="hello")
        assert _is_valid_uuid_v4(field.id)

    def test_reference_generates_uuid_v4(self) -> None:
        ref = Reference(targetId="target-123")
        assert _is_valid_uuid_v4(ref.id)

    def test_sync_list_generates_uuid_v4(self) -> None:
        sync_list = SyncList()
        assert _is_valid_uuid_v4(sync_list.id)

    def test_sync_object_generates_uuid_v4(self) -> None:
        sync_obj = SyncObject()
        assert _is_valid_uuid_v4(sync_obj.id)

    def test_empty_element_generates_uuid_v4(self) -> None:
        empty = EmptyElement()
        assert _is_valid_uuid_v4(empty.id)

    def test_field_enum_generates_uuid_v4(self) -> None:
        enum_field = FieldEnum(value="SomeValue")
        assert _is_valid_uuid_v4(enum_field.id)


class TestMemberUuidUniqueness:
    """Tests that each construction generates a unique UUID."""

    def test_multiple_members_have_unique_ids(self) -> None:
        members = [Member() for _ in range(100)]
        ids = {m.id for m in members}
        assert len(ids) == 100

    def test_multiple_field_bools_have_unique_ids(self) -> None:
        fields = [FieldBool(value=True) for _ in range(100)]
        ids = {f.id for f in fields}
        assert len(ids) == 100

    def test_mixed_types_have_unique_ids(self) -> None:
        items = [
            Member(),
            FieldBool(value=True),
            FieldInt(value=np.int32(1)),
            FieldString(value="test"),
            Reference(),
            SyncList(),
            SyncObject(),
            EmptyElement(),
            FieldEnum(value="Test"),
        ]
        ids = {item.id for item in items}
        assert len(ids) == len(items)


class TestMemberExplicitId:
    """Tests that explicit id parameter overrides the default UUID."""

    def test_member_explicit_id(self) -> None:
        member = Member(id="custom-id")
        assert member.id == "custom-id"

    def test_field_bool_explicit_id(self) -> None:
        field = FieldBool(id="my-bool-id", value=True)
        assert field.id == "my-bool-id"

    def test_field_int_explicit_id(self) -> None:
        field = FieldInt(id="my-int-id", value=np.int32(42))
        assert field.id == "my-int-id"

    def test_reference_explicit_id(self) -> None:
        ref = Reference(id="ref-id", targetId="target")
        assert ref.id == "ref-id"

    def test_sync_list_explicit_id(self) -> None:
        sync_list = SyncList(id="list-id")
        assert sync_list.id == "list-id"

    def test_empty_string_id_allowed(self) -> None:
        member = Member(id="")
        assert member.id == ""


class TestMemberDeserializationPreservesId:
    """Tests that deserialization from JSON preserves the id."""

    def test_decode_field_bool_preserves_id(self) -> None:
        json_data: dict[str, Any] = {
            "$type": "bool",
            "id": "preserved-bool-id",
            "value": True,
        }
        decoded = decode(json_data)
        assert decoded.id == "preserved-bool-id"

    def test_decode_field_int_preserves_id(self) -> None:
        json_data: dict[str, Any] = {
            "$type": "int",
            "id": "preserved-int-id",
            "value": 42,
        }
        decoded = decode(json_data)
        assert decoded.id == "preserved-int-id"

    def test_decode_field_string_preserves_id(self) -> None:
        json_data: dict[str, Any] = {
            "$type": "string",
            "id": "preserved-string-id",
            "value": "hello",
        }
        decoded = decode(json_data)
        assert decoded.id == "preserved-string-id"

    def test_decode_reference_preserves_id(self) -> None:
        json_data: dict[str, Any] = {
            "$type": "reference",
            "id": "preserved-ref-id",
            "targetId": "target-123",
        }
        decoded = decode(json_data)
        assert decoded.id == "preserved-ref-id"

    def test_decode_without_id_generates_uuid(self) -> None:
        # When id is missing from JSON, a new UUID should be generated
        json_data: dict[str, Any] = {"$type": "bool", "value": True}
        decoded = decode(json_data)
        assert _is_valid_uuid_v4(decoded.id)

    def test_decode_empty_element_preserves_id(self) -> None:
        json_data: dict[str, Any] = {"$type": "empty", "id": "empty-id"}
        decoded = decode(json_data)
        assert decoded.id == "empty-id"

    def test_decode_enum_preserves_id(self) -> None:
        json_data: dict[str, Any] = {
            "$type": "enum",
            "id": "enum-id",
            "value": "SomeValue",
            "enumType": "SomeEnumType",
        }
        decoded = decode(json_data)
        assert decoded.id == "enum-id"
