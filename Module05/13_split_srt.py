
names = "Oleh Ivan Stefan Yan IO"

l = names.split() # розділити рядок

l.sort(key = len) # відсортувати

print(l)

res = "|".join(l,) # зробити рядком знову

print(res)

print(str(l))