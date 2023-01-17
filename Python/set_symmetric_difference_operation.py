n1=int(input())
english=set(input().split())
n2=int(input())
french=set(input().split())

print(len(english.symmetric_difference(french)))

#set difference gives union of set_A and set_B without the intersection between the two.