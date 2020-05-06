# Atvirkštinę matricą

import numpy as np

matrix = np.array([[1, 2], [3, 4]]) 
try:
  inv_matrix = np.linalg.inv(matrix) 
except np.linalg.LinAlgError:
  print("Pasirinkta matrica neturi atvirkstines")
else:
  print(matrix) 
  print(inv_matrix)
  print(np.dot(matrix, inv_matrix))

# ARBA
print("\nKitas variantas\n")
matrix = np.matrix([[1, 2], [3, 4]])
try:
  inv_matrix = matrix.I 
except np.linalg.LinAlgError:
  print("Pasirinkta matrica neturi atvirkstines")
else:
  print(matrix) 
  print(inv_matrix)
