from enum import Enum, unique
from typing import Optional

from pydantic import Field

from cargo_parse.models.core import CoreModel


@unique
class Lto(str, Enum):
    FALSE = "false"
    TRUE = "true"
    THIN = "thin"
    OFF = "off"


@unique
class OptLevel(str, Enum):
    NO_OPTIMIZATIONS = "0"
    BASIC_OPTIMIZATIONS = "1"
    SOME_OPTIMIZATIONS = "2"
    ALL_OPTIMIZATIONS = "3"
    OPTIMIZE_FOR_BINARY_SIZE = "s"
    OPTIMIZE_FOR_BINARY_SIZE_TURN_OFF_LOOP_VECTORIZATION = "z"


@unique
class Panic(str, Enum):
    ABORT = "abort"
    UNWIND = "unwind"


@unique
class SplitDebugInfo(str, Enum):
    OFF = "off"
    PACKED = "packed"
    UNPACKED = "unpacked"


class Profile(CoreModel):
    name: str
    opt_level: Optional[OptLevel] = Field(None, alias="opt-level")
    debug: Optional[str]
    split_debuginfo: Optional[SplitDebugInfo] = Field(
        None, alias="split-debuginfo"
    )
    debug_assertions: Optional[bool] = Field(None, alias="debug-assertions")
    overflow_checks: Optional[bool] = Field(None, alias="overflow-checks")
    lto: Optional[Lto]
    panic: Optional[Panic]
    incremental: Optional[bool]
    codegen_units: Optional[int] = Field(None, alias="codegen-units")
    rpath: Optional[bool]
