a=int(input())
alist=set(input().split())
b=int(input())
blist=set(input().split())

print(len(alist.difference(blist)))