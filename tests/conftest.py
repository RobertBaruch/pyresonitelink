"""Pytest configuration for pyresonitelink tests."""

from typing import AsyncGenerator

import pytest
import pytest_asyncio

from pyresonitelink import client


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command line options for tests."""
    parser.addoption(
        "--port",
        action="store",
        type=int,
        help="Port number for ResoniteLink connection",
    )


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def resolink(
    request: pytest.FixtureRequest,
) -> AsyncGenerator[client.Client, None]:
    """Fixture providing a ResoniteLink client."""
    host = "localhost"
    resolink_port = request.config.getoption("--port")
    print(f"Connecting to ws://{host}:{resolink_port}...")
    resolink_client = client.Client()
    await resolink_client.connect(resolink_port, host)
    yield resolink_client
    await resolink_client.close()
