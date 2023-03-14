from itertools import combinations_with_replacement

n = input().split(' ')
a = sorted(n[0])
b = int(n[1])

a = list(combinations_with_replacement(a, b))

z = set()
for i in a:
    z.add(''.join(i))

for i in sorted(z):
    print(i)
