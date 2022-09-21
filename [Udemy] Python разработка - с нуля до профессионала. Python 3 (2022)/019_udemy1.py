s = 'hi, Python'

print(s)

print(min(s))
for n in enumerate(s):
    print(f'element: "{n}", min "{min(s)}", max "{max(s)}"')
    print(f'element: "{n}", num {ord(min(s))}, num {ord(max(s))}')

from random import shuffle

k = [*s]
shuffle(k)
print(k)
