from typing import List, Optional

from cargo_parse.models.core import CoreModel


class Lib(CoreModel):
    crate_type: Optional[List[str]]
    name: Optional[str]
