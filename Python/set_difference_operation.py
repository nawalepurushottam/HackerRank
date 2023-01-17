n1=int(input())
english=set(input().split())
n2=int(input())
french=set(input().split())

print(len(english.difference(french)))

#set difference gives A - B, which is equal to the elements present in A but not in B