import functools
import sys

sys.setrecursionlimit(10000)


@functools.lru_cache
def fibo_steroids(n):
    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n - 1) + fibo_steroids(n - 2)


a = fibo_steroids(2049)
print(a)
