from pathlib import Path
from typing import Dict, List

import toml
from pydantic import parse_obj_as

from cargo_parse.models.cargo_toml import (
    CargoTomlData,
    DependencyData,
    FeaturesData,
    PatchData,
    ProfileData,
)
from cargo_parse.models.dependency import Dependency
from cargo_parse.models.features import Feature
from cargo_parse.models.manifest import Manifest
from cargo_parse.models.patch import Patch
from cargo_parse.models.profile import Profile
from cargo_parse.util import none_if_none


def parse_manifest_from_toml(toml_file: Path) -> Manifest:
    with toml_file.open("r") as file:
        data = toml.load(file)

    cargo_toml_data = CargoTomlData(**data)

    manifest = Manifest(
        lib=cargo_toml_data.lib,
        package=cargo_toml_data.package,
        dependencies=_get_dependencies(cargo_toml_data.dependencies),
        dev_dependencies=_get_dependencies(cargo_toml_data.dev_dependencies),
        build_dependencies=_get_dependencies(
            cargo_toml_data.build_dependencies
        ),
        badges=cargo_toml_data.badges,
        patch=_get_patches(cargo_toml_data.patch),
        features=_get_features(cargo_toml_data.features),
        workspace=cargo_toml_data.workspace,
        profile=_get_profiles(cargo_toml_data.profile),
    )

    return manifest


@none_if_none
def _get_dependencies(
    dependency_data: Dict[str, DependencyData]
) -> List[Dependency]:
    dependencies = []
    for name, dep in dependency_data.items():
        data = {"name": name}
        if isinstance(dep, str):
            data["version"] = dep
        else:
            data.update(dep)
        dependencies.append(data)
    return parse_obj_as(List[Dependency], dependencies)


@none_if_none
def _get_features(features_data: Dict[str, FeaturesData]) -> List[Feature]:
    features = []
    for name, includes_features in features_data.items():
        data = {"name": name, "includes_features": includes_features}
        features.append(data)
    return parse_obj_as(List[Feature], features)


@none_if_none
def _get_patches(patch_data: Dict[str, PatchData]) -> List[Patch]:
    patches = []
    for source, patch in patch_data.items():
        data = {"source": source, "dependencies": _get_dependencies(patch)}
        patches.append(data)
    return parse_obj_as(List[Patch], patches)


@none_if_none
def _get_profiles(profile_data: Dict[str, ProfileData]) -> List[Profile]:
    profiles = []
    for name, profile in profile_data.items():
        data = {"name": name}
        data.update(profile)
        profiles.append(data)
    return parse_obj_as(List[Profile], profiles)
