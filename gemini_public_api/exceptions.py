class RateLimit(Exception):
    pass


class ResourceMoved(Exception):
    pass


class MarketError(Exception):
    """
    Auction not open or paused, ineligible timing, market not open, or the request was malformed, in the case of private
    API request, missing or malformed Gemini private API authentication headers.
    """
    pass


class ServerError(Exception):
    """
    The server encountered an error, technical issue or the exchange is down for maintenance.
    """
    pass
