import pytest
from aiohttp import ClientSession

from gemini_public_api.aiohttp.session_context_manager import SessionContextManager


@pytest.mark.asyncio
async def test_session_context_manager():
    # Create an instance of SessionContextManager and use it as an async context manager
    manager = SessionContextManager()
    session = None

    async with manager as s:
        session = s
        assert isinstance(session, ClientSession)

    # Assert that the session is closed after exiting the context
    assert session.closed
