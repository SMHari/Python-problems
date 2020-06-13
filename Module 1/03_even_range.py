def even():
    eve_list=[]
    start = 1000
    end = 3000
    for i in range(start,end+1):
        if(i%2==0):
            eve_list.append(i)
    print(eve_list)


if __name__ == '__main__':
    even()