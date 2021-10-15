from typing import List

from cargo_parse.models.core import CoreModel
from cargo_parse.models.dependency import Dependency


class Patch(CoreModel):
    source: str
    dependencies: List[Dependency]
