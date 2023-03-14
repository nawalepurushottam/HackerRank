n = int(input())
m = set(input().split(' '))

b = int(input())
c = set(input().split(' '))


d = c.union(m)
print(len(d))
