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

* **Michal Polit**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
