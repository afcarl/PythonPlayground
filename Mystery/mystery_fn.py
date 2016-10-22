def mystery(n):
    s = 1
    for i in xrange(n):
        if n % 2 == 0:
            for j in xrange(n):
                s = s * 3
        else:
            s = s * 2
    return s


print mystery(2)