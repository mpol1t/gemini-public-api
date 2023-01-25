from typing import Dict, List, Union, Any, Text

import requests

from gemini_public_api import public_endpoints
from gemini_public_api import public_sandbox_endpoints
from gemini_public_api.exceptions import (
    RateLimit, MarketError, ServerError, ResourceMoved,
)


class GeminiPublicAPI:
    """
    Represents public Gemini REST API.
    """

    @classmethod
    def get_symbols(cls, sandbox: bool = False) -> List[Text]:
        """
        Retrieves list of strings representing available symbols.

        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    List of symbols currently traded at Gemini marketplace.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.SYMBOLS) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.SYMBOLS
        )

    @classmethod
    def get_symbol_details(cls, symbol: str, sandbox: bool = False) -> Dict[Text, Any]:
        """
        Retrieves symbol details.

        :param symbol:  Gemini symbol.
        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    Dictionary with symbol details.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.SYMBOL_DETAILS.format(symbol=symbol)) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.SYMBOL_DETAILS.format(symbol=symbol)
        )

    @classmethod
    def get_network(cls, token: str, sandbox: bool = False) -> Dict[Text, Any]:
        """
        Retrieves associated network for a requested token.

        :param token:  Gemini symbol.
        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    Dictionary with symbol details.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.NETWORK.format(token=token)) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.NETWORK.format(token=token)
        )

    @classmethod
    def get_ticker(cls, symbol: str, sandbox: bool = False) -> Dict[Text, Any]:
        """
        Retrieves ticker data for a given symbol.

        :param symbol:  Gemini symbol.
        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    Ticker data.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.PUBLIC_TICKER.format(symbol=symbol)) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.PUBLIC_TICKER.format(symbol=symbol)
        )

    @classmethod
    def get_ticker_v2(cls, symbol: str, sandbox: bool = False) -> Dict[Text, Any]:
        """
        Retrieves ticker data for a given symbol using V2 API.

        :param symbol:  Gemini symbol.
        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    Ticker data.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol)) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol)
        )

    @classmethod
    def get_candles(cls, symbol: str, time_frame: str, sandbox: bool = False) -> List[List[float]]:
        """
        Retrieves candle data for a symbol.

        :param symbol:      Gemini symbol.
        :param time_frame:  Either '1m', '5m', '15m', '30m', '1hr', '6hr' or '1day'.
        :param sandbox:     If true, uses Gemini sandbox environment.

        :return:    Candle data.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(
            endpoint=public_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame)) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame))

    @classmethod
    def get_free_promos(cls, sandbox: bool = False) -> Dict[Text, Any]:
        """
        Retrieves symbols that currently have fee promos.

        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    Symbols that currently have fee promos.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.FREE_PROMOS) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.FREE_PROMOS)

    @classmethod
    def get_current_order_book(
            cls,
            symbol: str,
            bid_limit: int = 500,
            ask_limit: int = 500,
            sandbox: bool = False
    ) -> Dict[Text, Any]:
        """
        Retrieves current order book for a symbol.

        :param symbol:      Gemini symbol.
        :param bid_limit:   Number of bids to retrieve (max 500).
        :param ask_limit:   Number of asks to retrieve (max 500).
        :param sandbox:     If true, uses Gemini sandbox environment.

        :return:    Current order book.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(
            endpoint=public_endpoints.CURRENT_ORDER_BOOK.format(
                symbol=symbol,
                bid_limit=bid_limit,
                ask_limit=ask_limit
            )
        ) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.CURRENT_ORDER_BOOK.format(
                symbol=symbol,
                bid_limit=bid_limit,
                ask_limit=ask_limit
            )
        )

    @classmethod
    def get_trade_history(
            cls,
            symbol: str,
            timestamp: int,
            limit_trades: int = 500,
            include_breaks: bool = False,
            sandbox: bool = False
    ) -> List[Dict]:
        """
        Retrieves trades that have executed since the specified timestamp for a given symbol.

        :param symbol:          Gemini symbol.
        :param timestamp:       Unix timestamp representing start of the interval.
        :param limit_trades:    Number of trades to retrieve (max 500).
        :param include_breaks:  If true, broken trades will be included in the list.
        :param sandbox:         If true, uses Gemini sandbox environment.

        :return:    List of trades.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(
            endpoint=public_endpoints.TRADE_HISTORY.format(
                symbol=symbol,
                timestamp=timestamp,
                limit_trades=limit_trades,
                include_breaks=str(include_breaks).lower()
            )
        ) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.TRADE_HISTORY.format(
                symbol=symbol,
                timestamp=timestamp,
                limit_trades=limit_trades,
                include_breaks=str(include_breaks).lower()
            )
        )

    @classmethod
    def get_price_feed(cls, sandbox: bool = False) -> List[Dict]:
        """
        Retrieves current price feed.

        :param sandbox: If true, uses Gemini sandbox environment.

        :return:    List of current prices for every Gemini symbol.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        return cls._get(endpoint=public_endpoints.PRICE_FEED) if sandbox else cls._get(
            endpoint=public_sandbox_endpoints.PRICE_FEED)

    @classmethod
    def _get(cls, endpoint: str, timeout: int = 5) -> Union[Dict, List]:
        """
        Low-level function that handles communication with the Gemini API.

        :param endpoint:    Gemini endpoint.
        :param timeout:     Connection timeout.

        :return:            API response.

        :raises:    RateLimit
        :raises:    ServerError
        :raises:    MarketError
        :raises:    ResourceMoved
        :raises:    JSONDecodeError
        :raises:    ConnectionError
        :raises:    Timeout
        :raises:    Exception
        """
        response = requests.get(endpoint, timeout=timeout)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            raise RateLimit(response.json()['message'])
        elif response.status_code in {500, 502, 503}:
            raise ServerError(response.json()['message'])
        elif response.status_code in {400, 403, 404, 406}:
            raise MarketError(response.json()['message'])
        elif response.status_code in {300, 301, 302, 303, 304, 305, 306, 308}:
            raise ResourceMoved(response.json()['message'])
        else:
            raise Exception(response.json()['message'])
