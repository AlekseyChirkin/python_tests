allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

# i = 0
#
# for w in words:
#     if set([*w]).issubset(set([*allowed])):
#         i += 1
# print(i)

print(sum(map(lambda x: set(x).issubset(set(allowed)), words)))
