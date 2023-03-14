from itertools import product

A = map(int, input().split())
B = map(int, input().split())

a = product(A, B)
for i in a:
    print(i, end=' ')
