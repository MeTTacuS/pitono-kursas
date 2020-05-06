# Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.

import numpy as np

matrix = np.random.rand(3, 5)
print(matrix)

# Suma
print(matrix.sum())

# Eiluciu sumos
print(matrix.sum(axis = 1))

# Stulpleiu sumos
print(matrix.sum(axis = 0))