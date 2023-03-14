x = int(input())
y = int(input())
z = int(input())
n = int(input())

# list comprehension syntax
# newlist = [expression for item in iterable if condition == True]

list1 = [[i, j, k] for i in list(range(x+1))
         for j in list(range(y+1)) for k in list(range(z+1))]
list2 = [a for a in list1 if sum(a) != n]
print(list2)
