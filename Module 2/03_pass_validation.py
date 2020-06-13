import re

def validate(n):
    name_list = list(n)
    digit_list = []
    alpha_list = []
    for i in name_list:
        if i.isdigit():
            digit_list.append(i)
        else:
            alpha_list.append(i)
    if len(alpha_list) != 0 and len(digit_list) != 0:
        return True
    else:
        return False


usr = input("Enter the UserName:")
pwd = input("Enter the password:")
pwdlen = len(pwd)
if re.match(r'[A-Za-z0-9@#$%^&+=]{6,12}', pwd):
    status = validate(pwd)
    if status:
        print("Success")
    else:
        print("Password doesn't met the requirements. Please try again.")

else:
    print("Enter valid password. length must be between 6 and 12")
