from typing import List

from cargo_parse.models.core import CoreModel


class Feature(CoreModel):
    name: str
    includes_features: List[str]