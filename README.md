[![codecov](https://codecov.io/gh/mpol1t/gemini-public-api/branch/main/graph/badge.svg?token=LV1BARCUF9)](https://codecov.io/gh/mpol1t/gemini-public-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gemini-public-api)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mpol1t/gemini-public-api/python-app.yml)
![GitHub](https://img.shields.io/github/license/mpol1t/gemini-public-api)

# Gemini Public API 

A Python wrapper for the public Gemini API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing
Install package through pip
```
pip3 install gemini-public-api
```

Alternatively, clone the repo

```
git clone https://github.com/michalpolit/gemini-public-api.git
```

and install dependencies

```
poetry install
```


## Running the tests
In order to run tests, dependencies must be installed using
```
poetry install --with test
```

To run the tests

```
coverage run -m pytest
```

To show test coverage

```
coverage report -m
```

## Usage

```python
from gemini_public_api.api import GeminiPublicAPI

symbols = GeminiPublicAPI.get_symbols()
print(symbols)
```

## Built With

* [Poetry](https://python-poetry.org/docs/) - Packaging and dependency management
* [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) - Property-based testing

## Authors

* **mpol1t**

## License

This project is licensed under the MIT License
