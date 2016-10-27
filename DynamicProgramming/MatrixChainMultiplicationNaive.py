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
def matrix_chain_order(p, i, j):
    global counter
    counter += 1
    if i == j:
        return 0
    minimum = sys.maxint
    k = i
    while k < j:
        count = matrix_chain_order(p,i,k) + matrix_chain_order(p,k+1,j) + p[i-1]*p[k]*p[j]
        if count < minimum:
            minimum = count
        k+=1
    return minimum



arr = [5, 2, 4, 3, 7, 9, 7, 8, 6, 1, 3, 7, 6, 5]
#arr = [30,35,15,5,10,20,25]
#arr = [5, 2, 4, 7, 3, 9, 7, 8, 6, 3, 7, 5, 5]
#arr = [10,20,30,40,30]

count = 0
with Timer() as t:
    count = matrix_chain_order(arr,1,len(arr) - 1)


print count
print 'Time taken to compute results : %d (milli seconds) ' % (t.interval * 10**6)
print 'Number of recursive calls' , counter