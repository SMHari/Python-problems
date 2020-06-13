if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # print(student_marks)
    query_name = input()
    if query_name in student_marks.keys():
        add = 0.00
        lst = list(student_marks.get(query_name))
        for i in range(len(lst)):
            add += lst[i]
        avg = add / len(lst)
        print(format(avg,'.2f'))
