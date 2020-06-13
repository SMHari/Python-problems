if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        str = input().split()
        com = str[0]
        args = str[1:]
        if com == 'print':
            print(lst)
        else:
            com += "("+ ",".join(args) +")"
            #print(com)
            eval("lst."+com)



