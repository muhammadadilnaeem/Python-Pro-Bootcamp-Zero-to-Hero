
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def square(n):
    """Return the square of n."""
    return n ** 2

def is_even(n):
    """Return True if n is even, else False."""
    return n % 2 == 0

def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        return "Factorial not defined for negative numbers."
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def reverse_string(s):
    """Return the reversed version of the string s."""
    return s[::-1]