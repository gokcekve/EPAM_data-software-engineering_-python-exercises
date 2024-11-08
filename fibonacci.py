def get_fib(n):
    """Get a Nth element of the Fibonacci sequence."""
    if n == 1: # base case
        value = 0
    elif n == 2: # base case
        value = 1
    else:
        value = get_fib(n - 2) + get_fib(n - 1) # recursive call

    return value

# test
print(get_fib(13))