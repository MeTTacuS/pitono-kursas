# Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.

import numpy as np

arr = np.ones((12, 12))
arr[1:11, 1:11] = 0
print(arr)