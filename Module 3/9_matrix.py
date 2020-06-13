if __name__ == '__main__':
    x, y = input().split(',')
    x = int(x)
    y = int(y)

    final_lst = []
    for i in range(0, x):
        lst = []
        for j in range(0, y):

            lst.append(i*j)

        final_lst.append(lst)

    print(final_lst)
