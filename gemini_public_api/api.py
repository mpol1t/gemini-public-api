from typing import Dict, List, Union, Any, Text

import requests

from gemini_public_api.exceptions import (
    RateLimit, MarketError, ServerError, ResourceMoved,
)
from gemini_public_api.public_endpoints import (
    SYMBOLS, PUBLIC_TICKER, SYMBOL_DETAILS, PUBLIC_TICKER_V2, CANDLES, CURRENT_ORDER_BOOK,
    TRADE_HISTORY, PRICE_FEED, NETWORK, FREE_PROMOS
)


class GeminiPublicAPI:
    """
    Represents public Gemini REST API.
    """
    @classmethod
    def get_symbols(cls) -> List[Text]:
        """
        Retrieves list of strings representing available symbols.

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
        return cls._get(endpoint=SYMBOLS)

    @classmethod
    def get_symbol_details(cls, symbol: str) -> Dict[Text, Any]:
        """
        Retrieves symbol details.

        :param symbol:  Gemini symbol.

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
        return cls._get(endpoint=SYMBOL_DETAILS.format(symbol=symbol))

    @classmethod
    def get_network(cls, token: str) -> Dict[Text, Any]:
        """
        Retrieves associated network for a requested token.

        :param token:  Gemini symbol.

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
        return cls._get(endpoint=NETWORK.format(token=token))

    @classmethod
    def get_ticker(cls, symbol: str) -> Dict[Text, Any]:
        """
        Retrieves ticker data for a given symbol.

        :param symbol:  Gemini symbol.

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
        return cls._get(endpoint=PUBLIC_TICKER.format(symbol=symbol))

    @classmethod
    def get_ticker_v2(cls, symbol: str) -> Dict[Text, Any]:
        """
        Retrieves ticker data for a given symbol using V2 API.

        :param symbol:  Gemini symbol.

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
        return cls._get(endpoint=PUBLIC_TICKER_V2.format(symbol=symbol))

    @classmethod
    def get_candles(cls, symbol: str, time_frame: str) -> List[List[float]]:
        """
        Retrieves candle data for a symbol.

        :param symbol:      Gemini symbol.
        :param time_frame:  Either '1m', '5m', '15m', '30m', '1hr', '6hr' or '1day'.

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
        return cls._get(endpoint=CANDLES.format(symbol=symbol, time_frame=time_frame))

    @classmethod
    def get_free_promos(cls) -> Dict[Text, Any]:
        """
        Retrieves symbols that currently have fee promos.

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
        return cls._get(endpoint=FREE_PROMOS)

    @classmethod
    def get_current_order_book(cls, symbol: str, bid_limit: int = 0, ask_limit: int = 0) -> Dict[Text, Any]:
        """
        Retrieves current order book for a symbol.

        :param symbol:      Gemini symbol.
        :param bid_limit:   Number of bids to retrieve (max 500).
        :param ask_limit:   Number of asks to retrieve (max 500).

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
            endpoint=CURRENT_ORDER_BOOK.format(
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
            include_breaks: bool = False
    ) -> List[Dict]:
        """
        Retrieves trades that have executed since the specified timestamp for a given symbol.

        :param symbol:          Gemini symbol.
        :param timestamp:       Unix timestamp representing start of the interval.
        :param limit_trades:    Number of trades to retrieve (max 500).
        :param include_breaks:  If true, broken trades will be included in the list.

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
            endpoint=TRADE_HISTORY.format(
                symbol=symbol,
                timestamp=timestamp,
                limit_trades=limit_trades,
                include_breaks=str(include_breaks).lower()
            )
        )

    @classmethod
    def get_price_feed(cls) -> List[Dict]:
        """
        Retrieves current price feed.

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
        return cls._get(endpoint=PRICE_FEED)

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
