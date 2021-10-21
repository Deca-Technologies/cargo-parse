# cargo-parse

[![Unit Tests](https://github.com/Deca-Technologies/cargo-parse/actions/workflows/unit_test.yml/badge.svg?branch=main)](https://github.com/Deca-Technologies/cargo-parse/actions/workflows/unit_test.yml)
[![PyPI version](https://badge.fury.io/py/cargo-parse.svg)](https://badge.fury.io/py/cargo-parse)


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


## Usage

Import the `parse_manifest_from_toml` function and use it to parse the contents of `Cargo.toml`:


```python
from cargo_parse import parse_manifest_from_toml

from pathlib import Path

cargo_toml_file = "Cargo.toml"
manifest = parse_manifest_from_toml(Path(cargo_toml_file))

# Print out the package version
print(manifest.package.version)

# Print out the dependencies
if manifest.dependencies is not None:
    print(manifest.dependencies)
else:
    print(f"No dependencies defined in {cargo_toml_file}")
```
