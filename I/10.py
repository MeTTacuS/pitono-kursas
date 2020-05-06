# Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių

import numpy as np

matrix = np.matrix([[1, 2], [3, 4]])

reiksmes, vektoriai = np.linalg.eig(matrix)
print(reiksmes)
print(vektoriai)