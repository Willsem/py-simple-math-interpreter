from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER    = 0
    PLUS      = 1
    MINUS     = 2
    MULTIPLY  = 3
    DIVIDE    = 4
    LPAREN    = 5
    RPAREN    = 6
    LESS      = 7
    LESSEQUAL = 8
    MORE      = 9
    MOREEQUAL = 10
    EQUAL     = 11

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
