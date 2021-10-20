from typing import List, Optional

from pydantic import Field

from cargo_parse.models.core import CoreModel


class Package(CoreModel):
    name: str
    version: str
    authors: Optional[List[str]]
    description: Optional[str]
    documentation: Optional[str]
    edition: Optional[str]
    build: Optional[str]
    default_run: Optional[str] = Field(None, alias="default-run")
    homepage: Optional[str]
    repository: Optional[str]
    readme: Optional[str]
    keywords: Optional[List[str]]
    categories: Optional[List[str]]
    license: Optional[str]
