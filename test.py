a = [][]
a = [
    [9 if (x == 0 or x == 9 or y == 0 or y == 9) else 0 for x in range(10)]
    for y in range(10)
]
print(a)
