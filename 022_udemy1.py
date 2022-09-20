smile = '\U0001f600'

for i in range(10):
    t = smile
    for j in range(i):
        t += smile
    print(t)

for k in range(1, 11):
    print(smile * k)

list_11 = [0, 1, 4, 9, 16, 25, 36, 49, [lkasd for lkasd in range(1, 10)], 64, 81, 0, -4, -12,
           [ood * 2 for ood in range(99, 5, -6)], -24, -40]

for x in list_11:
    if isinstance(x, list):
        for x1 in x:
            print(f'{x1} -> ', end='')
        continue
    print(x)

