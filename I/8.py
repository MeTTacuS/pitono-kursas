# Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). 
# Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.

import numpy as np

matrix = np.random.rand(5, 5)
print(matrix)

sorted_array = matrix[np.argsort(matrix[:, 1])]
print(sorted_array)
