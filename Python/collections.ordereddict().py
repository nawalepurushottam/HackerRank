N=int(input())

dict={}
for i in range(N):
    item=input().split()
    itemname=' '.join(item[:-1])
    itemprice=int(item[-1])
    if(dict.get(itemname)):
        dict[itemname]+=itemprice
    else:
        dict[itemname]=itemprice

for i in dict:
    print(i,dict[i])
