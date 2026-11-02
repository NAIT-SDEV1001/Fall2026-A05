def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide by zero! {a, b}")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
