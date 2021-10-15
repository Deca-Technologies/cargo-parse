from pydantic import Field

from typing import Any, Dict, List, Optional, Union, NewType

from cargo_parse.models.badges import Badges
from cargo_parse.models.core import CoreModel
from cargo_parse.models.lib import Lib
from cargo_parse.models.package import Package
from cargo_parse.models.profile import Profile
from cargo_parse.models.workspace import Workspace

Version = NewType('Version', str)
Table = NewType('Table', Dict[str, Any])
DependencyData = NewType('DependencyData', Union[Version, Table])
PatchData = NewType('PatchData', Dict[str, DependencyData])
FeaturesData = NewType('FeaturesData', List[str])
ProfileData = NewType('ProfileData', Dict[str, Any])


class CargoTomlData(CoreModel):
    lib: Optional[Lib]
    package: Package
    dependencies: Optional[Dict[str, DependencyData]]
    dev_dependencies: Optional[Dict[str, DependencyData]] = Field(None, alias="dev-dependencies")
    build_dependencies: Optional[Dict[str, DependencyData]] = Field(None, alias="build-dependencies")
    badges: Optional[Badges]
    patch: Optional[Dict[str, PatchData]]
    features: Optional[Dict[str, FeaturesData]]
    workspace: Optional[Workspace]
    profile: Optional[Dict[str, ProfileData]]

