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

def MatrixChainOrder(p, n):
    global counter
    counter += 1
    m = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):

                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]

#arr = [1, 2, 3 ,4]
#arr = [10,20,30,40,30]
arr = [5, 2, 4, 3, 7, 9, 7, 8, 6, 1, 3, 7, 6, 5]
size = len(arr)

with Timer() as t:
    count = MatrixChainOrder(arr, size)

print 'Minimum number of multiplications is :', count
print 'Time taken to compute results : %d (milli seconds) ' % (t.interval * 10**6)
print 'Number of recursive calls' , counter