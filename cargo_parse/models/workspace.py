from typing import List, Optional

from cargo_parse.models.core import CoreModel


class Workspace(CoreModel):
    members: List[str]
    exclude: Optional[List[str]]
