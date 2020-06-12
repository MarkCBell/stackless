
# This provides a function decorator that implements Tail Call Optimisation.
# For why you would not want to do this, see:
#  http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html and
#  http://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html

from decorator import decorator
import inspect

NONTERMINAL = object()

@decorator
def stackless(func, *args, **kwargs):
    stack = inspect.stack()
    if sum(1 for x in inspect.stack() if x.function == stack[0].function) <= 1:  # If first time.
        out = func(*args, **kwargs)
        while isinstance(out, tuple) and out and out[0] == NONTERMINAL:
            _, callee, args, kwargs = out
            out = callee(*args, **kwargs)
        return out
    else:
        return (NONTERMINAL, func, args, kwargs)

@stackless
def factoial(x, y=1):
    return factoial(x-1, y*x) if x > 0 else y

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



