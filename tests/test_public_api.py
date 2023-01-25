from hypothesis import given, settings
from hypothesis.strategies import from_type, sampled_from, dictionaries
from mock import patch, MagicMock
from pytest import raises
from requests import Response

from gemini_public_api.api import GeminiPublicAPI
from gemini_public_api.exceptions import RateLimit, ServerError, MarketError, ResourceMoved

from gemini_public_api import public_endpoints
from gemini_public_api import public_sandbox_endpoints

MAX_EXAMPLES: int = 100


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_symbols(mock):
    GeminiPublicAPI.get_symbols()
    mock.assert_called_once_with(endpoint=public_endpoints.SYMBOLS)


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_symbols_sandbox(mock):
    GeminiPublicAPI.get_symbols(sandbox=True)
    mock.assert_called_once_with(endpoint=public_sandbox_endpoints.SYMBOLS)


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_symbol_details(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_symbol_details(symbol=symbol)
        mock.assert_called_once_with(endpoint=public_endpoints.SYMBOL_DETAILS.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_symbol_details_sandbox(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_symbol_details(symbol=symbol, sandbox=True)
        mock.assert_called_once_with(endpoint=public_sandbox_endpoints.SYMBOL_DETAILS.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
def test_get_network(token):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_network(token=token)
        mock.assert_called_once_with(endpoint=public_endpoints.NETWORK.format(token=token))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(token=from_type(str))
def test_get_network_sandbox(token):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_network(token=token, sandbox=True)
        mock.assert_called_once_with(endpoint=public_sandbox_endpoints.NETWORK.format(token=token))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_ticker(symbol=symbol)
        mock.assert_called_once_with(endpoint=public_endpoints.PUBLIC_TICKER.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_sandbox(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_ticker(symbol=symbol, sandbox=True)
        mock.assert_called_once_with(endpoint=public_sandbox_endpoints.PUBLIC_TICKER.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_v2(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_ticker_v2(symbol=symbol)
        mock.assert_called_once_with(endpoint=public_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(symbol=from_type(str))
def test_get_ticker_v2_sandbox(symbol):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_ticker_v2(symbol=symbol, sandbox=True)
        mock.assert_called_once_with(endpoint=public_sandbox_endpoints.PUBLIC_TICKER_V2.format(symbol=symbol))

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
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_candles(symbol=symbol, time_frame=time_frame)
        mock.assert_called_once_with(endpoint=public_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame))

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
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_candles(symbol=symbol, time_frame=time_frame, sandbox=True)
        mock.assert_called_once_with(
            endpoint=public_sandbox_endpoints.CANDLES.format(symbol=symbol, time_frame=time_frame)
        )

    run_test()


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_free_promos(mock):
    GeminiPublicAPI.get_free_promos()
    mock.assert_called_once_with(endpoint=public_endpoints.FREE_PROMOS)


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_free_promos_sandbox(mock):
    GeminiPublicAPI.get_free_promos(sandbox=True)
    mock.assert_called_once_with(endpoint=public_sandbox_endpoints.FREE_PROMOS)


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
def test_get_current_order_book(symbol, bid_limit, ask_limit):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_current_order_book(symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit)
        mock.assert_called_once_with(
            endpoint=public_endpoints.CURRENT_ORDER_BOOK.format(
                symbol=symbol,
                bid_limit=bid_limit,
                ask_limit=ask_limit
            )
        )

    run_test()


@settings(max_examples=MAX_EXAMPLES)
@given(
    symbol=from_type(str),
    bid_limit=from_type(int),
    ask_limit=from_type(int)
)
def test_get_current_order_book_sandbox(symbol, bid_limit, ask_limit):
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_current_order_book(symbol=symbol, bid_limit=bid_limit, ask_limit=ask_limit, sandbox=True)
        mock.assert_called_once_with(
            endpoint=public_sandbox_endpoints.CURRENT_ORDER_BOOK.format(
                symbol=symbol,
                bid_limit=bid_limit,
                ask_limit=ask_limit
            )
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
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_trade_history(
            symbol=symbol,
            timestamp=timestamp,
            limit_trades=limit_trades,
            include_breaks=include_breaks
        )
        mock.assert_called_once_with(
            endpoint=public_endpoints.TRADE_HISTORY.format(
                symbol=symbol,
                timestamp=timestamp,
                limit_trades=limit_trades,
                include_breaks=str(include_breaks).lower()
            )
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
    @patch('gemini_public_api.api.GeminiPublicAPI._get')
    def run_test(mock):
        GeminiPublicAPI.get_trade_history(
            symbol=symbol,
            timestamp=timestamp,
            limit_trades=limit_trades,
            include_breaks=include_breaks,
            sandbox=True
        )
        mock.assert_called_once_with(
            endpoint=public_sandbox_endpoints.TRADE_HISTORY.format(
                symbol=symbol,
                timestamp=timestamp,
                limit_trades=limit_trades,
                include_breaks=str(include_breaks).lower()
            )
        )

    run_test()


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_price_feed(mock):
    GeminiPublicAPI.get_price_feed()
    mock.assert_called_once_with(endpoint=public_endpoints.PRICE_FEED)


@patch('gemini_public_api.api.GeminiPublicAPI._get')
def test_get_price_feed_sandbox(mock):
    GeminiPublicAPI.get_price_feed(sandbox=True)
    mock.assert_called_once_with(endpoint=public_sandbox_endpoints.PRICE_FEED)


@patch('requests.get')
def test__get_raises_rate_limit(mock):
    response: Response = MagicMock()
    response.status_code = 429

    mock.return_value = response

    with raises(expected_exception=RateLimit):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_server_error_on_code_500(mock):
    response: Response = MagicMock()
    response.status_code = 500

    mock.return_value = response

    with raises(expected_exception=ServerError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_server_error_on_code_502(mock):
    response: Response = MagicMock()
    response.status_code = 502

    mock.return_value = response

    with raises(expected_exception=ServerError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_server_error_on_code_503(mock):
    response: Response = MagicMock()
    response.status_code = 503

    mock.return_value = response

    with raises(expected_exception=ServerError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_market_error_on_code_400(mock):
    response: Response = MagicMock()
    response.status_code = 400

    mock.return_value = response

    with raises(expected_exception=MarketError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_market_error_on_code_403(mock):
    response: Response = MagicMock()
    response.status_code = 403

    mock.return_value = response

    with raises(expected_exception=MarketError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_market_error_on_code_404(mock):
    response: Response = MagicMock()
    response.status_code = 404

    mock.return_value = response

    with raises(expected_exception=MarketError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_market_error_on_code_406(mock):
    response: Response = MagicMock()
    response.status_code = 406

    mock.return_value = response

    with raises(expected_exception=MarketError):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_300(mock):
    response: Response = MagicMock()
    response.status_code = 300

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_301(mock):
    response: Response = MagicMock()
    response.status_code = 301

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_302(mock):
    response: Response = MagicMock()
    response.status_code = 302

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_303(mock):
    response: Response = MagicMock()
    response.status_code = 303

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_304(mock):
    response: Response = MagicMock()
    response.status_code = 304

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_305(mock):
    response: Response = MagicMock()
    response.status_code = 305

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_306(mock):
    response: Response = MagicMock()
    response.status_code = 306

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_resource_moved_on_code_308(mock):
    response: Response = MagicMock()
    response.status_code = 308

    mock.return_value = response

    with raises(expected_exception=ResourceMoved):
        GeminiPublicAPI._get(endpoint='')


@patch('requests.get')
def test__get_raises_generic_exception(mock):
    response: Response = MagicMock()
    response.status_code = 999

    mock.return_value = response

    with raises(expected_exception=Exception):
        GeminiPublicAPI._get(endpoint='')


@settings(max_examples=MAX_EXAMPLES)
@given(json=dictionaries(keys=from_type(str), values=from_type(str)))
def test__get(json):
    @patch('requests.get')
    def run_test(mock):
        response: Response = MagicMock()
        response.status_code = 200
        response.json.return_value = json

        mock.return_value = response

        assert GeminiPublicAPI._get(endpoint='') == json

    run_test()
