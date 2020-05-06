# Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j

n = int(input())
arr = [[i + j for i in range(0, n)] for j in range(0, n)]

for item in arr:
  print(item, end="\n")