import math


def calculate(c, h, d):
    find = (2 * c * d) / h
    return str(math.floor(math.sqrt(find)))


if __name__ == '__main__':
    c = 50
    h = 30
    res = []
    d = input().split(',')
    d_list = list(d)
    for i in range(0, len(d_list)):
        res.append(calculate(c=50, h=30, d=int(d_list[i])))

    out = ','.join([str(elem) for elem in res])
    print(out)
