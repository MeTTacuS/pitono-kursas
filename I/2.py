# Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].

n = int(input())
arr = []
for _ in range(0, n):
  arr.extend([1, 2, 3])
print(arr)