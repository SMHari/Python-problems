def palindrome():
    i = input("Enter the number:")
    a = i[::-1]
    if(i==a):
        print("palindrome")
    else:
        print("Not palindrome")




if __name__ == '__main__':
    palindrome()