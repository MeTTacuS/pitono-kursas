# Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.

start = -1.3
end = 2.5
step = (end - start) / 64

arr = []
i = -1.3
while i < end:
  arr.append(float("{:.5f}".format(i)))
  i += step

print(arr)