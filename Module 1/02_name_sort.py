def name_sort():
    name_list = []
    while True:
        name = input("Enter the names:(Enter exit to finish)")
        if( name.upper() == "EXIT"):
            break
        else:
            name_list.append(name)
    name_list.sort()
    for i in name_list:
        print(i)


if __name__ == '__main__':
    name_sort()