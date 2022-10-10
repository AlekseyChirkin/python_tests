words = ["a","b","c","ab","bc","abc"]
s = "abc"

print(sum(map(lambda x: ord(x[0]), words)))
