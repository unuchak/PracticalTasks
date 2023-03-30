a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []

for i in range(len(a)):
    if i % 2 == 1:
        b.append(a[i])

print(b)

