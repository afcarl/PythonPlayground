import time
import sys


class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.clock()
        self.interval = self.end - self.start

counter = 0

def memoized_matrix_chain(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = float("inf")
    return lookup_chain(m, p, 0, n-1)

def lookup_chain(m, p, i, j):
    global counter
    counter += 1
    if m[i][j] < float("inf"):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i]*p[k+1]*p[j+1]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

#p = [30, 35, 15, 5, 10, 20, 25]
#arr = [10,20,30,40,30]
arr = [5, 2, 4, 3, 7, 9, 7, 8, 6, 1, 3, 7, 6, 5]
with Timer() as t:
    count =  memoized_matrix_chain(arr)

print 'Minimum number of multiplications is :', count
print 'Time taken to compute results : %d (milli seconds) ' % (t.interval * 10**6)
print 'Number of recursive calls' , counter