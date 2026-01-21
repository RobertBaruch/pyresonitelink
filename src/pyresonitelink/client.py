"""ResoniteLink client.

We don't expect concurrent requests; request() blocks until the response is received.

I strongly suggest using the async versions of the functions.
"""

import asyncio
import json
import uuid

import websockets

from .data import codec
from .data import messages
from .data import responses


MAX_RESPONSE_SIZE: int = 64 * 1024 * 1024
DEFAULT_TIMEOUT: float = 10


class Client:
    """ResoniteLink client."""

    _websocket: websockets.ClientConnection | None
    _loop: asyncio.AbstractEventLoop | None

    def __init__(self) -> None:
        self._websocket = None
        self._loop = None

    async def connect(
        self, port: int, host: str = "localhost", max_size: int = MAX_RESPONSE_SIZE
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

        # Hacky fix for first request fails.
        try:
            await self.get_slot(messages.GetSlot(slotId="Root", depth=0))
        except websockets.exceptions.ConnectionClosedError:
            self._websocket = await websockets.connect(uri, max_size=max_size)
            await self.get_slot(messages.GetSlot(slotId="Root", depth=0))

    def sync_connect(
        self,
        port: int,
        host: str = "localhost",
        timeout: float = DEFAULT_TIMEOUT,
        max_size: int = MAX_RESPONSE_SIZE,
    ) -> None:
        """Connects to the ResoniteLink server synchronously."""
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(
            asyncio.wait_for(self.connect(port, host, max_size), timeout=timeout)
        )

    async def request_json(
        self, message: messages.Message, debug: bool = False
    ) -> dict[str, codec.JsonValue]:
        """Sends a message to the ResoniteLink server and returns the JSON response."""
        if self._websocket is None:
            raise RuntimeError("Client is not connected")

        if message.messageId is None:
            message.messageId = str(uuid.uuid4())

        encoded_data = codec.encode(message)
        json_data = json.dumps(encoded_data, ensure_ascii=False)
        if debug:
            print("=================================")
            print(f"Request: {json_data}")

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
        if debug:
            print(f"Response: {json_response}")
            print()
        return json_response

    async def request(
        self, message: messages.Message, debug: bool = False
    ) -> responses.Response:
        """Sends a message to the ResoniteLink server and returns the response."""
        json_response = await self.request_json(message, debug)
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

    async def send_message[T](
        self, request: messages.Message, response_type: type[T], debug: bool = False
    ) -> T:
        """Sends a message to the ResoniteLink server and waits for the response."""
        response = await self.request(request, debug)
        assert isinstance(
            response, response_type
        ), f"Expected response Response, got {type(response)}"
        return response

    def sync_send_message[T](
        self,
        request: messages.Message,
        response_type: type[T],
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> T:
        """Sends a message to the ResoniteLink server and waits for the response."""
        if self._loop is None:
            raise RuntimeError("Client is not connected")
        return self._loop.run_until_complete(
            asyncio.wait_for(
                self.send_message(request, response_type, debug), timeout=timeout
            )
        )

    async def get_slot(
        self, request: messages.GetSlot, debug: bool = False
    ) -> responses.SlotData:
        """Sends a GetSlot request and waits for the response."""
        return await self.send_message(request, responses.SlotData, debug)

    def sync_get_slot(
        self,
        request: messages.GetSlot,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.SlotData:
        """Sends a GetSlot request and waits for the response."""
        return self.sync_send_message(request, responses.SlotData, debug, timeout)

    async def get_component(
        self, request: messages.GetComponent
    ) -> responses.ComponentData:
        """Sends a GetComponent request and waits for the response."""
        return await self.send_message(request, responses.ComponentData)

    def sync_get_component(
        self,
        request: messages.GetComponent,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.ComponentData:
        """Sends a GetComponent request and waits for the response."""
        return self.sync_send_message(request, responses.ComponentData, debug, timeout)

    async def add_slot(
        self, request: messages.AddSlot, debug: bool = False
    ) -> responses.Response:
        """Sends an AddSlot request and waits for the response."""
        return await self.send_message(request, responses.Response, debug)

    def sync_add_slot(
        self,
        request: messages.AddSlot,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends an AddSlot request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def update_slot(
        self, request: messages.UpdateSlot, debug: bool = False
    ) -> responses.Response:
        """Sends an UpdateSlot request and waits for the response."""
        return await self.send_message(request, responses.Response, debug)

    def sync_update_slot(
        self,
        request: messages.UpdateSlot,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends an UpdateSlot request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def remove_slot(
        self, request: messages.RemoveSlot, debug: bool = False
    ) -> responses.Response:
        """Sends a RemoveSlot request and waits for the response."""
        return await self.send_message(request, responses.Response, debug)

    def sync_remove_slot(
        self,
        request: messages.RemoveSlot,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends a RemoveSlot request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def add_component(self, request: messages.AddComponent) -> responses.Response:
        """Sends an AddComponent request and waits for the response."""
        return await self.send_message(request, responses.Response)

    def sync_add_component(
        self,
        request: messages.AddComponent,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends an AddComponent request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def update_component(
        self, request: messages.UpdateComponent, debug: bool = False
    ) -> responses.Response:
        """Sends an UpdateComponent request and waits for the response."""
        return await self.send_message(request, responses.Response, debug)

    def sync_update_component(
        self,
        request: messages.UpdateComponent,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends an UpdateComponent request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def remove_component(
        self, request: messages.RemoveComponent, debug: bool = False
    ) -> responses.Response:
        """Sends a RemoveComponent request and waits for the response."""
        return await self.send_message(request, responses.Response, debug)

    def sync_remove_component(
        self,
        request: messages.RemoveComponent,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.Response:
        """Sends a RemoveComponent request and waits for the response."""
        return self.sync_send_message(request, responses.Response, debug, timeout)

    async def import_texture_2d_file(
        self, request: messages.ImportTexture2DFile, debug: bool = False
    ) -> responses.AssetData:
        """Sends an ImportTexture2DFile request and waits for the response."""
        return await self.send_message(request, responses.AssetData, debug)

    def sync_import_texture_2d_file(
        self,
        request: messages.ImportTexture2DFile,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.AssetData:
        """Sends an ImportTexture2DFile request and waits for the response."""
        return self.sync_send_message(request, responses.AssetData, debug, timeout)

    async def import_texture_2d_rawdata(
        self, request: messages.ImportTexture2DRawData, debug: bool = False
    ) -> responses.AssetData:
        """Sends an ImportTexture2DRawData request and waits for the response."""
        return await self.send_message(request, responses.AssetData, debug)

    def sync_import_texture_2d_rawdata(
        self,
        request: messages.ImportTexture2DRawData,
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> responses.AssetData:
        """Sends an ImportTexture2DRawData request and waits for the response."""
        return self.sync_send_message(request, responses.AssetData, debug, timeout)
