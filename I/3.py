# Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.

arr = []
i = 1

while len(arr) < 10:
  if (i % 2 != 0):
    arr.append(i)
  i += 1

print(arr)