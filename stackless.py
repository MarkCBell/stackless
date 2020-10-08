
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
    if all(frame.function != stack[0].function for frame in stack[1:]):  # If first time.
        out = func(*args, **kwargs)
        while isinstance(out, tuple) and out and out[0] == NONTERMINAL:
            _, callee, args, kwargs = out
            out = callee(*args, **kwargs)
        return out
    else:
        return (NONTERMINAL, func, args, kwargs)

