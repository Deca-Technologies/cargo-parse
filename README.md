# cargo-parse

A Python package to parse `Cargo.toml` manifest files.

## Installation

This package is not (yet) published on PyPI. For now, the best way to install the package is to use
[Poetry](https://python-poetry.org/).

Clone this repository and run `poetry install`.

### Install in another environment

To install the package in a system environment, or another virtual
environment besides the Poetry project environment:

1. Build the package wheel with `poetry build`.
2. Install the package using the correct environment's `pip`:
```
<your-python> -m pip install <path-to-repo>/dist/cargo-parse-*.whl
```