"""Tests against ResoniteLink for values.

Run as: pytest --port=<resonite-link-port> tests/test_values.py [-s]

-s: outputs print statements
"""

# pylint: disable=protected-access,missing-function-docstring,missing-class-docstring

import uuid

import pytest

from pyresonitelink import client
from pyresonitelink.data import codec
from pyresonitelink.data import messages
from pyresonitelink.data import responses
from pyresonitelink.data import workers


class TestValues:

    @pytest.mark.asyncio(loop_scope="session")
    async def test_get_root_slot(self, resolink: client.Client) -> None:
        json_response = await resolink.request_json(
            messages.GetSlot(slotId="Root", depth=0, includeComponentData=False)
        )
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.SlotData)
        # From this point on, we can use get_slot.

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_slot(self, resolink: client.Client) -> None:
        slot_id = str(uuid.uuid4())
        json_response = await resolink.request_json(
            messages.AddSlot(
                data=workers.Slot(
                    id=slot_id,
                    parent=workers.Reference(
                        targetId=workers.Slot.ROOT_SLOT_ID,
                        targetType="FrooxEngine.Slot",
                    ),
                    name=workers.FieldString(value="Test Slot"),
                )
            )
        )
        assert (
            json_response["success"] is True
        ), f"Response for adding test slot was failure: {json_response}"
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use add_slot.

        response = await resolink.get_slot(
            messages.GetSlot(slotId=slot_id, depth=0, includeComponentData=False)
        )
        assert isinstance(response, responses.SlotData)
        assert response.data is not None
        assert response.data.id == slot_id

        json_response = await resolink.request_json(messages.RemoveSlot(slotId=slot_id))
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use remove_slot.

    @pytest.mark.asyncio(loop_scope="session")
    async def test_add_component(self, resolink: client.Client) -> None:
        slot_id = str(uuid.uuid4())
        response = await resolink.add_slot(
            messages.AddSlot(
                data=workers.Slot(
                    id=slot_id,
                    parent=workers.Reference(
                        targetId=workers.Slot.ROOT_SLOT_ID,
                        targetType="FrooxEngine.Slot",
                    ),
                    name=workers.FieldString(value="Test Slot"),
                )
            ),
        )
        assert isinstance(response, responses.Response)
        assert response.success is True

        # Ensure we can add a test component.
        component_id = str(uuid.uuid4())
        json_response = await resolink.request_json(
            messages.AddComponent(
                containerSlotId=slot_id,
                data=workers.Component(
                    id=component_id,
                    componentType="[FrooxEngine]FrooxEngine.ValueField<bool>",
                ),
            ),
        )
        assert (
            json_response["success"] is True
        ), f"Response for adding test component was failure: {json_response}"
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.Response)
        # From this point on, we can use add_component.

        # Ensure the slot contains the new component
        get_slot_response = await resolink.get_slot(
            messages.GetSlot(slotId=slot_id, depth=0, includeComponentData=True),
        )
        assert get_slot_response.data is not None
        assert get_slot_response.data.components is not None
        assert len(get_slot_response.data.components) > 0
        assert get_slot_response.data.components[0].id == component_id
        # This is an inconsistency in component type namings.
        # See https://github.com/Yellow-Dog-Man/ResoniteLink/issues/31
        assert get_slot_response.data.components[0].componentType == "FrooxEngine.ValueField<bool>"

        # Ensure the component data has the expected members.
        json_response = await resolink.request_json(
            messages.GetComponent(componentId=component_id)
        )
        assert json_response["success"] is True
        response = codec.decode_response(json_response)
        assert isinstance(response, responses.ComponentData)
        assert response.data is not None
        assert response.data.id == component_id
        assert "persistent" in response.data.members
        assert "UpdateOrder" in response.data.members
        assert "Enabled" in response.data.members
        assert "Value" in response.data.members
