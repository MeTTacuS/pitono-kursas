# Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.

arr = []

arr.append([1 for i in range(0, 12)])
for i in range(0, 10):
  arr.append([1])
  arr[i + 1].extend([0 for i in range(0, 10)])
  arr[i + 1].extend([1])
arr.append([1 for i in range(0, 12)])

for item in arr:
  print(item, end="\n")