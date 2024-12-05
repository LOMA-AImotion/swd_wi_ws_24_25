def f(x:int, y:int, z:int = 100) -> int:
    return (x + y)*z

print(f(10, 5))

from functools import partial
g = partial(f, 5)

print(g(20)) # sollte 25 sein
h = partial(g, 30)
print(h(z=10)) # sollte 35 sein 

partial_kw = partial(h, z=1)
print(partial_kw())

def drei_summe(x, y, z):
    return x + y + z

ein_summe = partial(drei_summe, 10, 20)
print(ein_summe(100))