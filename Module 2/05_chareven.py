str = input("Enter the string:")
str_list = list(str)
finalstr = ""
for i in str_list:
    idx = str_list.index(i)
    if idx % 2 == 0:
        finalstr += i

print(finalstr)
