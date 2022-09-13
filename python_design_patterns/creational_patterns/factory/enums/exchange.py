from enum import Enum


class Exchange(Enum):
    BSE = "BSE"
    NSE = "NSE"
    
    
    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value