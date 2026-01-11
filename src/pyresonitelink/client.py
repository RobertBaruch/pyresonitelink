"""ResoniteLink client.

We don't expect concurrent requests; request() blocks until the response is received.
"""

import asyncio
import json
import uuid

import websockets

from .data import codec
from .data import messages
from .data import responses


class Client:
    """ResoniteLink client."""

    _websocket: websockets.ClientConnection | None
    _loop: asyncio.AbstractEventLoop | None

    def __init__(self) -> None:
        self._websocket = None
        self._loop = None

    async def connect(
        self, port: int, host: str = "localhost", max_size: int = 64 * 1024 * 1024
    ) -> None:
        """Connects to the ResoniteLink server.

        Args:
            port: Port number for the connection.
            host: Host address.
            max_size: Maximum size of incoming messages in bytes. Default is 64MB.
        """
        if self._websocket is not None:
            return

        uri = f"ws://{host}:{port}"
        self._websocket = await websockets.connect(uri, max_size=max_size)

    def sync_connect(
        self,
        port: int,
        host: str = "localhost",
        timeout: float = 10,
        max_size: int = 64 * 1024 * 1024,
    ) -> None:
        """Connects to the ResoniteLink server synchronously."""
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(
            asyncio.wait_for(self.connect(port, host, max_size), timeout=timeout)
        )

    async def request(self, message: messages.Message) -> responses.Response:
        """Sends a message to the ResoniteLink server and returns the response."""
        if self._websocket is None:
            raise RuntimeError("Client is not connected")

        if message.messageId is None:
            message.messageId = str(uuid.uuid4())

        encoded_data = codec.encode(message)
        json_data = json.dumps(encoded_data, ensure_ascii=False)
        print(f"Sending message: {json_data}")

        await self._websocket.send(json_data.encode("utf-8"), text=True)

        # If the message has a binary payload, send it after the json data.
        if (
            isinstance(message, messages.BinaryPayloadMessage)
            and message.payload is not None
        ):
            await self._websocket.send(message.payload, text=False)

        # There doesn't seem to be binary payload responses yet.
        response_data = await self._websocket.recv()
        json_response = json.loads(response_data)
        print(f"Received response: {json_response}")
        response = codec.decode_response(json_response)
        return response

    async def close(self) -> None:
        """Closes the connection to the ResoniteLink server."""
        if self._websocket is not None:
            await self._websocket.close()
            self._websocket = None

    def sync_close(self) -> None:
        """Closes the connection to the ResoniteLink server synchronously."""
        if self._loop is None:
            return
        self._loop.run_until_complete(self.close())
        self._loop.close()

    def send_message[T](
        self, request: messages.Message, response_type: type[T], timeout: float = 10
    ) -> T:
        """Sends a message to the ResoniteLink server and waits for the response."""
        if self._loop is None:
            raise RuntimeError("Client is not connected")
        response = self._loop.run_until_complete(
            asyncio.wait_for(self.request(request), timeout=timeout)
        )
        assert isinstance(
            response, response_type
        ), f"Expected response Response, got {type(response)}"
        return response

    def get_slot(
        self, request: messages.GetSlot, timeout: float = 10
    ) -> responses.SlotData:
        """Sends a GetSlot request and waits for the response."""
        return self.send_message(request, responses.SlotData, timeout)

    def get_component(
        self, request: messages.GetComponent, timeout: float = 10
    ) -> responses.ComponentData:
        """Sends a GetComponent request and waits for the response."""
        return self.send_message(request, responses.ComponentData, timeout)

    def add_slot(
        self, request: messages.AddSlot, timeout: float = 10
    ) -> responses.Response:
        """Sends an AddSlot request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def update_slot(
        self, request: messages.UpdateSlot, timeout: float = 10
    ) -> responses.Response:
        """Sends an UpdateSlot request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def remove_slot(
        self, request: messages.RemoveSlot, timeout: float = 10
    ) -> responses.Response:
        """Sends a RemoveSlot request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def add_component(
        self, request: messages.AddComponent, timeout: float = 10
    ) -> responses.Response:
        """Sends an AddComponent request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def update_component(
        self, request: messages.UpdateComponent, timeout: float = 10
    ) -> responses.Response:
        """Sends an UpdateComponent request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def remove_component(
        self, request: messages.RemoveComponent, timeout: float = 10
    ) -> responses.Response:
        """Sends a RemoveComponent request and waits for the response."""
        return self.send_message(request, responses.Response, timeout)

    def import_texture_2d_file(
        self, request: messages.ImportTexture2DFile, timeout: float = 10
    ) -> responses.AssetData:
        """Sends an ImportTexture2DFile request and waits for the response."""
        return self.send_message(request, responses.AssetData, timeout)

    def import_texture_2d_rawdata(
        self, request: messages.ImportTexture2DRawData, timeout: float = 10
    ) -> responses.AssetData:
        """Sends an ImportTexture2DRawData request and waits for the response."""
        return self.send_message(request, responses.AssetData, timeout)
