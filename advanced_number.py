import typing
import operator

class AdvancedNumber:
    def __init__(self, value: typing.Union[int,float]):
        self._value = value

    @property
    def value(self) -> typing.Union[int,float]:
        return self._value

    def __str__(self) -> str:
        return f"Value: {self._value}"

    def __repr__(self) -> str:
        return f"AdvancedNumber({self._value})"
    
    def __add__(self, other: 'AdvancedNumber') -> 'AdvancedNumber':
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self._value + other._value)
        return NotImplemented
    
    def __radd__(self, other: typing.Union[int,float]) -> 'AdvancedNumber':
        return AdvancedNumber(other + self._value)
    
    def __sub__(self, other: 'AdvancedNumber') -> 'AdvancedNumber':
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self._value - other._value)
        return NotImplemented
    
    def __rsub__(self, other: typing.Union[int,float]) -> 'AdvancedNumber':
        return AdvancedNumber(other - self._value)
    
    def __mul__(self, other: 'AdvancedNumber') -> 'AdvancedNumber':
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self._value * other._value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self._value * other)
        return NotImplemented   
    
    def __rmul__(self, other: typing.Union[int,float]) -> 'AdvancedNumber':
        return AdvancedNumber(other * self._value)
    
    def __truediv__(self, other: 'AdvancedNumber') -> 'AdvancedNumber':
        if isinstance(other, AdvancedNumber):
            if other._value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return AdvancedNumber(self._value / other._value)
        return NotImplemented
    
    def __mod__(self, other: 'AdvancedNumber') -> 'AdvancedNumber':
        if isinstance(other, AdvancedNumber):
            if other._value == 0:
                raise ZeroDivisionError("Cannot perform modulo by zero")
            return AdvancedNumber(self._value % other._value)
        return NotImplemented    

    def __rmod__(self, other: typing.Union[int,float]) -> 'AdvancedNumber':
        return AdvancedNumber(other % self._value)
    
    def __lt__(self, other: 'AdvancedNumber') -> bool:
        if isinstance(other, AdvancedNumber):
            return self._value < other._value
        return NotImplemented
    
    def __gt__(self, other: 'AdvancedNumber') -> bool:
        if isinstance(other, AdvancedNumber):
            return self._value > other._value
        return NotImplemented
    
    def __le__(self, other: 'AdvancedNumber') -> bool:
        if isinstance(other, AdvancedNumber):
            return self._value <= other._value
        return NotImplemented
    
    def __ge__(self, other: 'AdvancedNumber') -> bool:
        if isinstance(other, AdvancedNumber):
            return self._value >= other._value
        return NotImplemented
    
    def __eq__(self, other: 'AdvancedNumber') -> bool:
        if isinstance(other, AdvancedNumber):
            return self._value == other._value
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __bool__(self) -> bool:
        return bool(self._value)
    
    def __call__(self) -> int:
        return self._value ** 2
    
    def __format__(self, format_spec: str) -> str:
        if format_spec.startswith('#x'):
            return f"0x{int(self._value):x}"
        if "f" in format_spec:
            precision = format_spec.split('.')[1][0]
            return f"{self._value:.{precision}f}"
        return str(self)
    
    def __del__(self):
        print(f"AdvancedNumber with value {self._value} is being destroyed")
    
    
    
    