accounts = [[1, 5], [7, 3], [3, 5]]

all_money = []

for acc in accounts:
    m = 0
    for b in acc:
        m += b
    all_money.append(m)

print(max(all_money))

# print(max(map(sum, accounts)))
