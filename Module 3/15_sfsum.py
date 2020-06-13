import math

if __name__ == '__main__':
    d = input().split(',')
    d_list = list(d)
    results = list(map(int, d_list))
    # sum function add the elements in the iterable as normal addition
    print(sum(results))
    # fsum (float sum)function add the elements in the iterable as floating point numbers with decimal prec
    print(math.fsum(results))
