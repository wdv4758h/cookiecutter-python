def fib(number: int) -> int:
    """
    Simple Fibonacci function.

    >>> fib(10)
    55
    """
    if number < 2:
        return number
    return fib(number - 1) + fib(number - 2)
