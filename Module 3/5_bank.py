import re

default_total_amt = 10000
default_pass = "root"
default_pin = 1212

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


def cash_withdraw(total, take):
    if total > take:
        available = total - take
        print("CASH WITHDRAWN")
        print("Available amt is :", available)
        return available

    else:
        print("That much amt not available in your account")
        return total


def cash_credit(total, credit):
    available = total + credit
    print("CASH CREDITED")
    print("Available amt is :", available)
    return available


def change_password():
    pwd = input("Enter the default password to change your current password:")
    if pwd == default_pass:
        new_pwd = input("Enter password that length must be between 6 and 12 can also have special characters ")
        reenter_pwd = input("Renter the password:")
        if new_pwd == reenter_pwd:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{6,12}', new_pwd):
                status = validate(new_pwd)
                if status:
                    print("Success. Password is set")
                else:
                    print("Password doesn't met the requirements. Please try again.")

            else:
                print("Password doesn't meet the requirements")
        else:
            print("Entered pwd combo is wrong. try again")

    else:
        print("Enter the correct password")


if __name__ == '__main__':

    pin = int(input("Enter pin:"))
    if pin == default_pin:

        while True:
            n = int(input("Enter the choice to be performed: \n 1. cash withdraw \n 2. cash credit \n 3. change "
                          "password "
                          "\n "
                          "press 0 to exit\n"))

            if n == 1:
                amt_withdraw = int(input("Enter the amount to withdraw:"))
                default_total_amt = cash_withdraw(default_total_amt, amt_withdraw)

            elif n == 2:
                amt_credited = int(input("Enter the amount to credit to account:"))
                default_total_amt = cash_credit(default_total_amt, amt_credited)
            elif n == 3:
                change_password()

            elif n == 0:
                print("Thank you")
                break
            else:
                print("Enter available choice")

    else:
        print("Entered PIN is wrong. Try again")
