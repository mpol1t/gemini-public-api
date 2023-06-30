import aiohttp


class SessionContextManager:
    """
    A context manager for aiohttp's ClientSession.

    This class ensures that a ClientSession is automatically closed
    when no longer needed.

    This class can be used with an `async with` statement.

    Example
    -------

    .. code-block:: python

        async with SessionContextManager() as session:
            async with session.get('http://httpbin.org/get') as resp:
                print(resp.status)
                print(await resp.text())

    Attributes
    ----------
    session
        An instance of aiohttp's ClientSession.
    """

    async def __aenter__(self):
        """
        Enter the runtime context related to this object.

        A new ClientSession object is created and returned.
        """
        self.session = aiohttp.ClientSession()
        return self.session

    async def __aexit__(self, exc_type, exc, tb):
        """
        Exit the runtime context related to this object.

        The ClientSession object is closed.
        """
        await self.session.close()
