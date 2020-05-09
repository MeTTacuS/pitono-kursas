# Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].

import numpy as np

n = int(input())
arr = np.tile([1, 2, 3], n)
print(arr)