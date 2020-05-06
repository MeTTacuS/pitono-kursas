# Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).

size = 8

if int(size % 2) != 0 or size < 0:
  print("Skaicius turi buti lyginis")
else:
  arr = [None]*size
  arr[::2] = [[0, 1] * int(size / 2) for _ in range(0, int(size / 2))]
  arr[1::2] = [[0, 1] * int(size / 2) for _ in range(0, int(size / 2))]

  for item in arr:
    print(item, end="\n")