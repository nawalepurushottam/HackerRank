N = int(input())
list1 = []
for x in range(N):
    x = input().split()
    if 'append' in x:
        list1.append(int(x[-1]))
    elif 'insert' in x:
        list1.insert(int(x[-2]), int(x[-1]))
    elif 'print' in x:
        print(list1)
    elif 'remove' in x:
        list1.remove(int(x[-1]))
    elif 'sort' in x:
        list1.sort()
    elif 'pop' in x:
        list1.pop()
    elif 'reverse' in x:
        list1.reverse()
