#!/usr/bin/env python

"""
Produces load on all available CPU cores
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import time, math
import datetime

def f(x):
    while True:
        startTime = datetime.datetime.now()
        while (datetime.datetime.now() - startTime).microseconds / 1000000.0 < 0.8:
           math.factorial(100)
        time.sleep(0.2)


if __name__ == '__main__':
    processes = cpu_count()
    print '-' * 20
    print 'Running load on CPU'
    print 'Utilizing %d cores' % processes
    print '-' * 20
    pool = Pool(processes)
    pool.map(f, range(processes))
