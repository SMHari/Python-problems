def validate(str):
    upper = 0
    lower = 0

    str_list = list(str)
    for i in str_list:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1

    print("UPPER CASE ", upper)
    print("LOWER CASE ", lower)


if __name__ == '__main__':
    str = input()
    validate(str)
