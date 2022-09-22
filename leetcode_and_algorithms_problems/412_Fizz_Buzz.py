n = 15

res = []

for i in range(1, n + 1):
    s = ''
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
    else:
        s = str(i)
    res.append(s)

print(res)

print(['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)])
