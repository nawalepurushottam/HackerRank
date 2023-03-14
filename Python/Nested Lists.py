if __name__ == '__main__':
    list1 = []
    score1 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        i = [name, score]
        list1.append(i)
        score1.append(score)

    a = min(score1)
    for i in range(len(score1)):
        if a in score1:
            score1.remove(a)
    b = min(score1)
    list1.sort()
    for i in range(len(list1)):
        if list1[i][1] == b:
            print(list1[i][0])
