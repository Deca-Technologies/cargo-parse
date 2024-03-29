"""
Example script to demonstrate the usefulness of `cargo-parse`.

In this script, which could run as a GitHub Action, we assert that all Git
dependencies in `Cargo.toml` are using the `master` branch. This check could
run whenever a PR targets the `master` branch.
"""

from pathlib import Path

from cargo_parse import parse_manifest_from_toml
from cargo_parse.models.dependency import GitDependency


PERMITTED_DEPENDENCY_BRANCHES = ["main", "master"]

if __name__ == "__main__":
    manifest = parse_manifest_from_toml(Path("../tests/resources/Cargo.toml"))

    for dependency in manifest.dependencies:
        if isinstance(dependency, GitDependency):
            assert (
                dependency.branch in PERMITTED_DEPENDENCY_BRANCHES
            ), "Branch '{}' of `{}` not in {}".format(
                dependency.branch,
                dependency.name,
                PERMITTED_DEPENDENCY_BRANCHES,
            )
