# Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).

import numpy as np

arr = np.zeros((8, 8))
arr[::2, ::2] = 1
arr[1::2, 1::2] = 1
print(arr)


  # arr = [None]*size
  # arr[::2] = [[0, 1] * int(size / 2) for _ in range(0, int(size / 2))]
  # arr[1::2] = [[0, 1] * int(size / 2) for _ in range(0, int(size / 2))]