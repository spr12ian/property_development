import sys
from typing import TextIO

class SysHelper:
    def __init__(self):
        pass

    @property
    def executable(self) -> str:
        return sys.executable

    def get_arg(self, index: int) -> str | None:
        if index < len(sys.argv):
            return sys.argv[index]
        else:
            return None

    def get_first_parameter(self) -> str | None:
        return self.get_arg(1)

    def get_parameter(self, index: int) -> str | None:
        return self.get_arg(index)

    @property
    def how_many_args(self) -> int:
        return len(sys.argv)

    @property
    def how_many_parameters(self) -> int:
        return self.how_many_args - 1

    @property
    def platform(self) -> str:
        return sys.platform
    
    @property
    def stdout(self) -> TextIO:
        return sys.stdout
    
    @property
    def version(self) -> str:
        return sys.version
