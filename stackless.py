
# This provides a function decorator that implements Tail Call Optimisation.
# For why you would not want to do this, see:
#  http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html and
#  http://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html

from collections import namedtuple
from decorator import decorator
import inspect

Call = namedtuple('Call', ['func', 'args', 'kwargs'])

@decorator
def stackless(func, *args, **kwargs):
    stack = inspect.stack()
    if all(frame.function != stack[0].function for frame in stack[1:]):  # If current frame's function is not already on the stack:
        out = func(*args, **kwargs)
        while isinstance(out, Call):
            out = out.func(*out.args, **out.kwargs)
        return out
    else:
        return Call(func, args, kwargs)

