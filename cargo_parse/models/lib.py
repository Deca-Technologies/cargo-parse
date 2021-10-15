from cargo_parse.models.core import CoreModel

from typing import List, Optional


class Lib(CoreModel):
    crate_type: Optional[List[str]]
    name: Optional[str]
