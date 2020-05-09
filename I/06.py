# Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j

import numpy as np

n = int(input())
arr = np.fromfunction(lambda i, j: i + j, (n, n))
print(arr)