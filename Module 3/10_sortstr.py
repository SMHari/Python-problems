if __name__ == '__main__':
    str = input().split(',')
    x = sorted(set(str))
    out = ','.join(x)
    print(out)