import json
from pathlib import Path
from typing import Any, Dict

from pytest import fixture

from cargo_parse import __version__
from cargo_parse.parse import parse_manifest_from_toml


@fixture(name="cargo_manifest")
def fixture_cargo_manifest() -> Dict[str, Any]:
    with Path("tests/fixtures/cargo_manifest.json").open(
        "r", encoding="utf8"
    ) as file:
        data = json.load(file)
        return data


def test_parse_manifest_from_toml(cargo_manifest):
    parsed_manifest = parse_manifest_from_toml(
        Path("tests/resources/Cargo.toml")
    )
    parsed_data = json.loads(
        parsed_manifest.json(by_alias=True, exclude_none=True)
    )
    assert parsed_data == cargo_manifest


def test_version():
    assert __version__ == "0.1.0"
