# Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus

import sympy as sp

x = sp.Symbol('x')
y = x ** 2 + 1

neapib_int = sp.integrate(y, x)
print(neapib_int)

apib_int = sp.integrate(y, (x, 1, 2))
print(apib_int)