if __name__ == '__main__':
    a,b,c,n = int(input()),int(input()),int(input()),int(input())
    # print(a,b,c,n)
    lst = [[x,y,z] for x in range(0,a+1) for y in range(0,b+1) for z in range(0,c+1) if (x+y+z)!=n]
    print(lst)