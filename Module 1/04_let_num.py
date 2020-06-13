def let_num():
    name = input("Enter the desired name")
    name_list = list(name)
    digit_list=[]
    alpha_list=[]
    for i in name_list:
        if i.isdigit():
            digit_list.append(i)
        else:
            alpha_list.append(i)

    print("LETTERS:", len(alpha_list))
    print("DIGITS:",len(digit_list))


if __name__ == '__main__':
    let_num()