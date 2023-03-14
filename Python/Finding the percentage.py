if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # print(student_marks)
    query_name = input()
    if query_name in student_marks:
        a = student_marks[query_name]
        b = sum(a)/len(a)
        c = format(b, '.2f')
        print(c)
