def naiveFib(n):
    """
    Naive implementation of nth Fibonacci number generator
    Time complexity - O(1.6^n)
    :param n: The nth term
    :return: The nth fibonnaci number
    """
    if n ==  0:
        return 0
    elif n == 1:
        return 1
    else:
        return naiveFib(n-1) + naiveFib(n-2)


def betterFib(n):
    """
    Better implementation of nth Fibonacci number generator
    Time complexity - O(n)
    Space complexity - O(n)
    :param n: The nth term
    :return: The nth fibonnaci number
    """
    fib = [None] * n
    #print fib
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif fib[n-1] is not None:
        return fib[n-1]
    else :
        fib[n-1] = betterFib(n-1) + betterFib(n-2)
        return fib[n-1]


def fibonacci(n):
    """
    Improved implementation of nth Fibonacci number generator
    Time complexity - O(n)
    Space complexity - O(1)
    :param n: The nth term
    :return: The nth fibonnaci number
    """
    fib = [None] * 3
    fib[0] = 0
    fib[1] = 1
    if n == 0:
        return fib[0]
    for _ in xrange(n+1):
        if _ >= 2:
            fib[2] = fib[1] + fib[0]
            fib[0] = fib[1]
            fib[1] = fib[2]
    return fib[1]

print naiveFib(6)
print betterFib(6)
print fibonacci(6)