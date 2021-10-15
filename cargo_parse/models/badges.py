from enum import Enum, unique

from cargo_parse.models.core import CoreModel


@unique
class Status(str, Enum):
    ACTIVELY_DEVELOPED = "actively-developed"
    PASSIVELY_MAINTAINED = "passively-maintained"
    AS_IS = "as-is"
    EXPERIMENTAL = "experimental"
    LOOKING_FOR_MAINTAINER = "looking-for-maintainer"
    DEPRECATED = "deprecated"
    NONE = "none"


class Maintenance(CoreModel):
    status: Status


class Badges(CoreModel):
    maintenance: Maintenance
