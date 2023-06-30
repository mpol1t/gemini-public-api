from typing import Optional

from aiohttp import ClientSession

import gemini_public_api.public_endpoints as production
import gemini_public_api.public_sandbox_endpoints as sandbox


async def get_symbols(session: ClientSession, use_sandbox: bool = False):
    """
    Asynchronously retrieves all available trading symbols.

    :param session: aiohttp client session.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(url=sandbox.SYMBOLS if use_sandbox else production.SYMBOLS)


async def get_symbol_details(session: ClientSession, symbol: str, use_sandbox: bool = False):
    """
    Asynchronously retrieves detailed information for a specific symbol.

    :param session: aiohttp client session.
    :param symbol: symbol for which details are required.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.SYMBOL_DETAILS.format(symbol=symbol) if use_sandbox else production.SYMBOL_DETAILS.format(
            symbol=symbol)
    )


async def get_network(session: ClientSession, token: str, use_sandbox: bool = False):
    """
    Asynchronously retrieves the network status of a token.

    :param session: aiohttp client session.
    :param token: token for which network status is required.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.NETWORK.format(token=token) if use_sandbox else production.NETWORK.format(token=token)
    )


async def get_ticker(session: ClientSession, symbol: str, use_sandbox: bool = False):
    """
    Asynchronously retrieves the ticker for a specific symbol.

    :param session: aiohttp client session.
    :param symbol: symbol for which ticker is required.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.PUBLIC_TICKER.format(
            symbol=symbol) if use_sandbox else production.PUBLIC_TICKER.format(symbol=symbol)
    )


async def get_ticker_v2(session: ClientSession, symbol: str, use_sandbox: bool = False):
    """
    Asynchronously retrieves the ticker (version 2) for a specific symbol.

    :param session: aiohttp client session.
    :param symbol: symbol for which ticker (version 2) is required.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.PUBLIC_TICKER_V2.format(
            symbol=symbol) if use_sandbox else production.PUBLIC_TICKER_V2.format(symbol=symbol)
    )


async def get_candles(session: ClientSession, symbol: str, time_frame: str, use_sandbox: bool = False):
    """
    Asynchronously retrieves the candles data for a specific symbol and time frame.

    :param session: aiohttp client session.
    :param symbol: symbol for which candles data is required.
    :param time_frame: time frame for the candles data.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.CANDLES.format(
            symbol=symbol, time_frame=time_frame
        ) if use_sandbox else production.CANDLES.format(symbol=symbol, time_frame=time_frame)
    )


async def get_free_promos(session: ClientSession, use_sandbox: bool = False):
    """
    Asynchronously retrieves all available free promotions.

    :param session: aiohttp client session.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(url=sandbox.FREE_PROMOS if use_sandbox else production.FREE_PROMOS)


async def get_current_order_book(
        session: ClientSession,
        symbol: str,
        bid_limit: int = 500,
        ask_limit: int = 500,
        use_sandbox: bool = False
):
    """
    Asynchronously retrieves the current order book for a specific symbol.

    :param session: aiohttp client session.
    :param symbol: symbol for which order book is required.
    :param bid_limit: limit for bid orders.
    :param ask_limit: limit for ask orders.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.CURRENT_ORDER_BOOK.format(symbol=symbol) if use_sandbox else production.CURRENT_ORDER_BOOK.format(
            symbol=symbol),
        params={'bid_limit': bid_limit, 'ask_limit': ask_limit}
    )


async def get_trade_history(
        session: ClientSession,
        symbol: str,
        timestamp: Optional[int] = None,
        limit_trades: int = 500,
        include_breaks: bool = False,
        use_sandbox: bool = False
):
    """
    Asynchronously retrieves the trade history for a specific symbol.

    :param session: aiohttp client session.
    :param symbol: symbol for which trade history is required.
    :param timestamp: starting timestamp for the trade history.
    :param limit_trades: limit for number of trades in the history.
    :param include_breaks: flag to include breaks in the trade history.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(
        url=sandbox.TRADE_HISTORY.format(symbol=symbol) if use_sandbox else production.TRADE_HISTORY.format(
            symbol=symbol),
        params={
            'timestamp':      timestamp,
            'limit_trades':   limit_trades,
            'include_breaks': str(include_breaks).lower()
        } if timestamp is not None else {
            'limit_trades':   limit_trades,
            'include_breaks': str(include_breaks).lower()
        }
    )


async def get_price_feed(session: ClientSession, use_sandbox: bool = False):
    """
    Asynchronously retrieves the price feed.

    :param session: aiohttp client session.
    :param use_sandbox: flag to use sandbox endpoints.
    :return: Coroutine that needs to be awaited on, returns aiohttp client response.
    """
    return session.get(url=sandbox.PRICE_FEED if use_sandbox else production.PRICE_FEED)
