import time
from contextlib import contextmanager
@contextmanager
def log(function):
    print "entered function ",__name__
    yield
    print "exiting function",__name__


class Timer(object):
    def __enter__(self):
        self.start = time.clock()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.clock()
        self.interval = self.end - self.start


with Timer() as t:
    for _ in range(1000):
        print _,

print '\nTime taken(seconds) : ',t.interval

def f1():
    print 'Inside f1'

with log(f1):
    print 'start'