def binaryToDecimal(n):
    return int(n,2)


if __name__ == '__main__':
    d = input().split(',')
    d_list = list(d)
    op = []
    for i in range(0, len(d_list)):
        x = binaryToDecimal(d_list[i])
        if x % 5 == 0:
            op.append(d_list[i])

    out = ','.join([str(elem) for elem in op])
    print(out)

