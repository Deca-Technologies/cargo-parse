from typing import List, Optional

from cargo_parse.models.badges import Badges
from cargo_parse.models.core import CoreModel
from cargo_parse.models.dependency import Dependency
from cargo_parse.models.features import Feature
from cargo_parse.models.lib import Lib
from cargo_parse.models.package import Package
from cargo_parse.models.patch import Patch
from cargo_parse.models.profile import Profile
from cargo_parse.models.workspace import Workspace


class Manifest(CoreModel):
    package: Package
    lib: Optional[Lib]
    dependencies: Optional[List[Dependency]]
    dev_dependencies: Optional[List[Dependency]]
    build_dependencies: Optional[List[Dependency]]
    badges: Optional[Badges]
    patch: Optional[List[Patch]]
    features: Optional[List[Feature]]
    workspace: Optional[Workspace]
    profile: Optional[List[Profile]]
