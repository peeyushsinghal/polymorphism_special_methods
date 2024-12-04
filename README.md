# AdvancedNumber

A Python class that extends the functionality of numeric types with additional operations and features.

## Features

- Arithmetic operations (`+`, `-`, `*`, `/`, `%`)
- Comparison operations (`<`, `>`, `<=`, `>=`, `==`)
- Hashable (can be used in sets and as dictionary keys)
- Boolean conversion
- Callable (returns square of the value)
- Custom string formatting
- Cleanup notification (prints message when object is destroyed)

## Installation

1. Copy `advanced_number.py` to your project directory
2. Import the class: 
```python
from advanced_number import AdvancedNumber
```
## Usage Examples

### Basic Operations
```python
# Create instances
num1 = AdvancedNumber(10)
num2 = AdvancedNumber(5)
Arithmetic operations
sum_result = num1 + num2 # AdvancedNumber(15)
diff_result = num1 - num2 # AdvancedNumber(5)
product = num1 2 # AdvancedNumber(20)
quotient = num1 / num2 # AdvancedNumber(2.0)
remainder = num1 % num2 # AdvancedNumber(0)
```
### Comparison Operations

```python
num1 = AdvancedNumber(10)
num2 = AdvancedNumber(5)
num1 > num2 # True
num2 < num1 # True
num1 >= num2 # True
num2 <= num1 # True
num1 == num2 # False


### Set Operations

```python
#Objects with same value are considered equal
obj1 = AdvancedNumber(10)
obj2 = AdvancedNumber(10)
number_set = {obj1, obj2} # Contains only one element
```

### Boolean Conversion
```python
bool(AdvancedNumber(10)) # True
bool(AdvancedNumber(0)) # False
```

### Callable Objects
```python
num = AdvancedNumber(4)
num() # Returns 16 (squares the value)
```

### Custom Formatting
```python
num = AdvancedNumber(10)
formatted_str = format(num, ".2f") # Returns "10.00"
formatted_str = format(num, "#x") # Returns "0xa"
```

## Testing

Run the tests using pytest:

```bash
pytest test_advanced_number.py
```

## Requirements
- Python 3.6+
- pytest (for running tests)

