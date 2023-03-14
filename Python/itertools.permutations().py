from itertools import permutations

a = input()
b = a.split(" ")
string = sorted(b[0])
size = int(b[1])

for i in list(permutations(string, size)):
    print("".join(i))
