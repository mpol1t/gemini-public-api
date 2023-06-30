from unittest.mock import AsyncMock

import pytest
from aiohttp import ClientSession
from hypothesis import given, strategies as st, settings
from hypothesis.strategies import from_type, sampled_from

from gemini_public_api import public_sandbox_endpoints, public_endpoints
from gemini_public_api.aiohttp import api

MAX_EXAMPLES: int = 100


@pytest.mark.asyncio
async def test_get_symbols():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_symbols(session=session, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.SYMBOLS)


@pytest.mark.asyncio
async def test_get_symbols_sandbox():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_symbols(session=session, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.SYMBOLS)


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str)
)
@pytest.mark.asyncio
async def test_get_symbol_details(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_symbol_details(session=session, symbol=symbol, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.SYMBOL_DETAILS.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=st.text()
)
@pytest.mark.asyncio
async def test_get_symbol_details_sandbox(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_symbol_details(session=session, symbol=symbol, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.SYMBOL_DETAILS.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
@pytest.mark.asyncio
async def test_get_network(token):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_network(session=session, token=token, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.NETWORK.format(token=token))


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
@pytest.mark.asyncio
async def test_get_network_sandbox(token):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_network(session=session, token=token, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.NETWORK.format(token=token))


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
@pytest.mark.asyncio
async def test_get_ticker(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_ticker(session=session, symbol=symbol, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.PUBLIC_TICKER.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
@pytest.mark.asyncio
async def test_get_ticker_sandbox(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_ticker(session=session, symbol=symbol, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.PUBLIC_TICKER.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
@pytest.mark.asyncio
async def test_get_ticker_v2(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_ticker_v2(session=session, symbol=symbol, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
@pytest.mark.asyncio
async def test_get_ticker_v2_sandbox(symbol):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_ticker_v2(session=session, symbol=symbol, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    time_frame=sampled_from(
        elements=[
            '1m',
            '5m',
            '15m',
            '30m',
            '1hr',
            '6hr',
            '1day'
        ]
    )
)
@pytest.mark.asyncio
async def test_get_candles(symbol, time_frame):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_candles(session=session, symbol=symbol, time_frame=time_frame, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame))


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    time_frame=sampled_from(
        elements=[
            '1m',
            '5m',
            '15m',
            '30m',
            '1hr',
            '6hr',
            '1day'
        ]
    )
)
@pytest.mark.asyncio
async def test_get_candles_sandbox(symbol, time_frame):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_candles(session=session, symbol=symbol, time_frame=time_frame, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame))


@pytest.mark.asyncio
async def test_get_free_promos():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_free_promos(session=session, use_sandbox=False)
    mock_get.assert_called_once_with(url=public_endpoints.FREE_PROMOS)


@pytest.mark.asyncio
async def test_get_free_promos_sandbox():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_free_promos(session=session, use_sandbox=True)
    mock_get.assert_called_once_with(url=public_sandbox_endpoints.FREE_PROMOS)


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
@pytest.mark.asyncio
async def test_get_current_order_book(symbol, bid_limit, ask_limit):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_current_order_book(
        session=session, symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit, use_sandbox=False
    )
    mock_get.assert_called_once_with(
        url=public_endpoints.CURRENT_ORDER_BOOK.format(symbol=symbol),
        params={'bid_limit': bid_limit, 'ask_limit': ask_limit}
    )


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
@pytest.mark.asyncio
async def test_get_current_order_book_sandbox(symbol, bid_limit, ask_limit):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_current_order_book(
        session=session, symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit, use_sandbox=True
    )
    mock_get.assert_called_once_with(
        url=public_sandbox_endpoints.CURRENT_ORDER_BOOK.format(symbol=symbol),
        params={'bid_limit': bid_limit, 'ask_limit': ask_limit}
    )


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=st.text(),
    timestamp=st.integers(),
    limit_trades=st.integers(),
    include_breaks=st.booleans()
)
@pytest.mark.asyncio
async def test_get_trade_history(symbol, timestamp, limit_trades, include_breaks):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_trade_history(
        session=session,
        symbol=symbol,
        timestamp=timestamp,
        limit_trades=limit_trades,
        include_breaks=include_breaks,
        use_sandbox=False
    )

    mock_get.assert_called_once_with(
        url=public_endpoints.TRADE_HISTORY.format(symbol=symbol),
        params={
            'timestamp':      timestamp,
            'limit_trades':   limit_trades,
            'include_breaks': str(include_breaks).lower()
        }
    )


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=st.text(),
    timestamp=st.integers(),
    limit_trades=st.integers(),
    include_breaks=st.booleans()
)
@pytest.mark.asyncio
async def test_get_trade_history_sandbox(symbol, timestamp, limit_trades, include_breaks):
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_trade_history(
        session=session,
        symbol=symbol,
        timestamp=timestamp,
        limit_trades=limit_trades,
        include_breaks=include_breaks,
        use_sandbox=True
    )

    mock_get.assert_called_once_with(
        url=public_sandbox_endpoints.TRADE_HISTORY.format(symbol=symbol),
        params={
            'timestamp':      timestamp,
            'limit_trades':   limit_trades,
            'include_breaks': str(include_breaks).lower()
        }
    )


@pytest.mark.asyncio
async def test_get_price_feed():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_price_feed(session=session, use_sandbox=False)

    mock_get.assert_called_once_with(url=public_endpoints.PRICE_FEED)


@pytest.mark.asyncio
async def test_get_price_feed_sandbox():
    mock_get = AsyncMock()

    session = ClientSession()
    session.get = mock_get

    await api.get_price_feed(session=session, use_sandbox=True)

    mock_get.assert_called_once_with(url=public_sandbox_endpoints.PRICE_FEED)
