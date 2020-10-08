
from stackless import stackless

@stackless
def factorial(x, y=1):
    return factorial(x-1, y*x) if x > 0 else y

@stackless
def cumsum(n, a=0):
    return cumsum(n-1, a+n) if n > 0 else a

@stackless
def fibo(n, p=1, q=0):
    return fibo(n-1, p+q, p) if n > 0 else p

@stackless
def f(n, a=0):
    return g(n-1, a+2) if n > 0 else a

@stackless
def g(n, a=0):
    return h(n-1, a+n) if n > 0 else a

@stackless
def h(n, a=0):
    return f(n, a+1) if n > 0 else a

for i in range(20):
    print(i, fibo(i))

# Just to prove that things work.
import sys
sys.setrecursionlimit(20)

print(f(100))



