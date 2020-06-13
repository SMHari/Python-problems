if __name__ == '__main__':
    start = 2000
    end = 3200
    lst = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            lst.append(i)

    result = ','.join([str(i) for i in lst])
    print(result)
