from hypothesis import given, settings
from hypothesis.strategies import from_type, sampled_from
from mock import patch

import gemini_public_api.api as api
from gemini_public_api import public_endpoints
from gemini_public_api import public_sandbox_endpoints

MAX_EXAMPLES: int = 100


@patch('requests.get')
def test_get_symbols(mock):
    api.get_symbols()
    mock.assert_called_once_with(url=public_endpoints.SYMBOLS)


@patch('requests.get')
def test_get_symbols_sandbox(mock):
    api.get_symbols(use_sandbox=True)
    mock.assert_called_once_with(url=public_sandbox_endpoints.SYMBOLS)


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_symbol_details(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_symbol_details(symbol=symbol)
        mock.assert_called_once_with(url=public_endpoints.SYMBOL_DETAILS.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_symbol_details_sandbox(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_symbol_details(symbol=symbol, use_sandbox=True)
        mock.assert_called_once_with(url=public_sandbox_endpoints.SYMBOL_DETAILS.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
def test_get_network(token):
    @patch('requests.get')
    def run_test(mock):
        api.get_network(token=token)
        mock.assert_called_once_with(url=public_endpoints.NETWORK.format(token=token))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
def test_get_network_sandbox(token):
    @patch('requests.get')
    def run_test(mock):
        api.get_network(token=token, use_sandbox=True)
        mock.assert_called_once_with(url=public_sandbox_endpoints.NETWORK.format(token=token))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_ticker(symbol=symbol)
        mock.assert_called_once_with(url=public_endpoints.PUBLIC_TICKER.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_sandbox(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_ticker(symbol=symbol, use_sandbox=True)
        mock.assert_called_once_with(url=public_sandbox_endpoints.PUBLIC_TICKER.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_v2(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_ticker_v2(symbol=symbol)
        mock.assert_called_once_with(url=public_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_v2_sandbox(symbol):
    @patch('requests.get')
    def run_test(mock):
        api.get_ticker_v2(symbol=symbol, use_sandbox=True)
        mock.assert_called_once_with(url=public_sandbox_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))

    run_test()


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
def test_get_candles(symbol, time_frame):
    @patch('requests.get')
    def run_test(mock):
        api.get_candles(symbol=symbol, time_frame=time_frame)
        mock.assert_called_once_with(url=public_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame))

    run_test()


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
def test_get_candles_sandbox(symbol, time_frame):
    @patch('requests.get')
    def run_test(mock):
        api.get_candles(symbol=symbol, time_frame=time_frame, use_sandbox=True)
        mock.assert_called_once_with(
            url=public_sandbox_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame)
        )

    run_test()


@patch('requests.get')
def test_get_free_promos(mock):
    api.get_free_promos()
    mock.assert_called_once_with(url=public_endpoints.FREE_PROMOS)


@patch('requests.get')
def test_get_free_promos_sandbox(mock):
    api.get_free_promos(use_sandbox=True)
    mock.assert_called_once_with(url=public_sandbox_endpoints.FREE_PROMOS)


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
def test_get_current_order_book(symbol, bid_limit, ask_limit):
    @patch('requests.get')
    def run_test(mock):
        api.get_current_order_book(symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit)
        mock.assert_called_once_with(
            url=public_endpoints.CURRENT_ORDER_BOOK.format(symbol=symbol),
            params={'bid_limit': bid_limit, 'ask_limit': ask_limit}
        )

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
def test_get_current_order_book_sandbox(symbol, bid_limit, ask_limit):
    @patch('requests.get')
    def run_test(mock):
        api.get_current_order_book(symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit, use_sandbox=True)
        mock.assert_called_once_with(
            url=public_sandbox_endpoints.CURRENT_ORDER_BOOK.format(symbol=symbol),
            params={'bid_limit': bid_limit, 'ask_limit': ask_limit}
        )

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    timestamp=from_type(int),
    limit_trades=from_type(int),
    include_breaks=from_type(bool)
)
def test_get_trade_history(symbol, timestamp, limit_trades, include_breaks):
    @patch('requests.get')
    def run_test(mock):
        api.get_trade_history(
            symbol=symbol,
            timestamp=timestamp,
            limit_trades=limit_trades,
            include_breaks=include_breaks
        )
        mock.assert_called_once_with(
            url=public_endpoints.TRADE_HISTORY.format(symbol=symbol),
            params={
                'timestamp':      timestamp,
                'limit_trades':   limit_trades,
                'include_breaks': str(include_breaks).lower()
            }
        )

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    timestamp=from_type(int),
    limit_trades=from_type(int),
    include_breaks=from_type(bool)
)
def test_get_trade_history_sandbox(symbol, timestamp, limit_trades, include_breaks):
    @patch('requests.get')
    def run_test(mock):
        api.get_trade_history(
            symbol=symbol,
            timestamp=timestamp,
            limit_trades=limit_trades,
            include_breaks=include_breaks,
            use_sandbox=True
        )
        mock.assert_called_once_with(
            url=public_sandbox_endpoints.TRADE_HISTORY.format(symbol=symbol),
            params={
                'timestamp':      timestamp,
                'limit_trades':   limit_trades,
                'include_breaks': str(include_breaks).lower()
            }
        )

    run_test()


@patch('requests.get')
def test_get_price_feed(mock):
    api.get_price_feed()
    mock.assert_called_once_with(url=public_endpoints.PRICE_FEED)


@patch('requests.get')
def test_get_price_feed_sandbox(mock):
    api.get_price_feed(use_sandbox=True)
    mock.assert_called_once_with(url=public_sandbox_endpoints.PRICE_FEED)
