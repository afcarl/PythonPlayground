def exp_by_squaring(x, n):
    if n < 0:
        x = 1 / x;
        n = -n;
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x = x * x
            n = n / 2
        else:
            y = x * y
            x = x * x
            n = (n - 1) / 2
    return x * y


print exp_by_squaring(2,20)