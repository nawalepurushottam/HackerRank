from itertools import combinations

a = input()
b = a.split(" ")
string = sorted(b[0])
size = int(b[1])

for i in range(size+1):
    for j in list(combinations(string, i)):
        if len(j) == 0:
            pass
        else:
            print("".join(j))
