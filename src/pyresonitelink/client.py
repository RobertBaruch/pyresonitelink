"""ResoniteLink client.

We don't expect concurrent requests; request() blocks until the response is received.
"""

import json
import uuid

import websockets

from .data import codec
from .data import messages
from .data import responses


class Client:
    """ResoniteLink client."""

    _websocket: websockets.ClientConnection | None

    def __init__(self) -> None:
        self._websocket = None

    async def connect(self, port: int, host: str = "localhost") -> None:
        """Connects to the ResoniteLink server."""
        if self._websocket is not None:
            return

        uri = f"ws://{host}:{port}"
        async with websockets.connect(uri) as websocket:
            self._websocket = websocket

    async def request(self, message: messages.Message) -> responses.Response:
        """Sends a message to the ResoniteLink server and returns the response."""
        if self._websocket is None:
            raise RuntimeError("Client is not connected")

        if message.messageId is None:
            message.messageId = str(uuid.uuid4())

        encoded_data = codec.encode(message)
        json_data = json.dumps(encoded_data, ensure_ascii=False)

        await self._websocket.send(json_data.encode("utf-8"), text=True)

        # If the message has a binary payload, send it after the json data.
        if isinstance(message, messages.BinaryPayloadMessage):
            binary_payload = message.encode_binary_payload()
            if binary_payload is not None:
                await self._websocket.send(binary_payload, text=False)

        # There doesn't seem to be binary payload responses yet.
        response_data = await self._websocket.recv()
        response = codec.decode_response(json.loads(response_data))
        return response

    async def close(self) -> None:
        """Closes the connection to the ResoniteLink server."""
        if self._websocket is not None:
            await self._websocket.close()
            self._websocket = None
