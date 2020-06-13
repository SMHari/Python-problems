str = input("Enter the character to find the count")
str_set= sorted(set(str))

for i in str_set:
    print(i,str.count(i))
