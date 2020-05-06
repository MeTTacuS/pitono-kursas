# Pasirinktos funkcijos išvestinę

import sympy as sp

x = sp.Symbol('x')
y = x ** 2 + 1

dif = y.diff(x)
print(dif)