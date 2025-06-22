[![codecov](https://codecov.io/gh/mpol1t/gemini-public-api/branch/main/graph/badge.svg?token=LV1BARCUF9)](https://codecov.io/gh/mpol1t/gemini-public-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gemini-public-api)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mpol1t/gemini-public-api/python-app.yml)
![GitHub](https://img.shields.io/github/license/mpol1t/gemini-public-api)

⚠️ **This project is archived and no longer maintained.** ⚠️

This repository and the associated PyPI package (`gemini-public-api`) are no longer supported. No future updates will be released.

Feel free to fork or take over maintenance if needed.

# Gemini Public API 

The gemini-public-api is an unofficial Python implementation of the public Gemini REST API. It provides a simple interface for interacting with the Gemini cryptocurrency exchange, supporting both synchronous and asynchronous communication.


## Installation

To get the Gemini Public API Python client running on your local machine, use pip:

```
pip3 install gemini-public-api
```

Please make sure that you have Python 3.6 or newer, as this library requires it.

## Usage

### Synchronous Usage

```python
from gemini_public_api import api

symbols = api.get_symbols()
print(symbols.json())
```

### Asynchronous Usage

The library relies on the `aiohttp` package for truly asynchronous execution. The `SessionContextManager` context manager is used for making async requests. Here's how to fetch the available symbols asynchronously:

```python
from gemini_public_api.aiohttp import api
from gemini_public_api.aiohttp.session_context_manager import SessionContextManager

async with SessionContextManager() as session:
    response = await api.get_symbols(session)
    
    async with response as resp:
        data = await resp.json()
        print(data)
```

Alternatively, without the context manager:

```python
import aiohttp

from gemini_public_api.aiohttp import api

session = aiohttp.ClientSession()

response = await api.get_symbols(session)
 
async with response as resp:
   data = await resp.json()
   print(data)

await session.close()
```

## Dependencies

`gemini-public-api` is built with:

* [poetry](https://python-poetry.org/docs/) -  A tool for dependency management and packaging in Python.
* [hypothesis](https://hypothesis.readthedocs.io/en/latest/) - A powerful, flexible, and easy-to-use library for property-based testing.
* [requests](https://docs.python-requests.org/en/latest/) - The definitive library for making HTTP requests in Python.
* [aiohttp](https://docs.aiohttp.org/en/stable/) - An asynchronous HTTP client/server framework for asyncio and Python.

## Authors

* **mpol1t**

## License

This project is licensed under the MIT License
