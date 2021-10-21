from typing import List, NewType, Optional, Union

from cargo_parse.models.cargo_toml import CoreModel


class BaseDependency(CoreModel):
    name: str
    features: Optional[List[str]]
    optional: bool = False


class CratesIoDependency(BaseDependency):
    version: str


class CustomRegistryDependency(BaseDependency):
    version: str
    registry: str


class GitDependency(BaseDependency):
    git: str
    branch: Optional[str]


class PathDependency(BaseDependency):
    path: str


class MultipleGitDependency(GitDependency):
    """Git dependency with crates.io version specified."""

    version: str


class MultiplePathDependency(PathDependency):
    """Path dependency with crates.io version specified."""

    version: str


Dependency = NewType(
    "Dependency",
    Union[
        CustomRegistryDependency,
        MultipleGitDependency,
        GitDependency,
        MultiplePathDependency,
        PathDependency,
        CratesIoDependency,
    ],
)
