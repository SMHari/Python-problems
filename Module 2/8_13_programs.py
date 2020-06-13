# 8th program on element intersection
a = [1, 3, 6, 78, 35, 55]
b = [12, 24, 35, 24, 88, 120, 155]
final_list = [x for x in a if x in b]
print(final_list)

# 9th program print list removing duplicates
list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(sorted(set(list)))

# 10th program to print the list after removing the value 24 by list comprehension
list1 = [12, 24, 35, 24, 88, 120, 155]
final = [y for y in list1 if y != 24]
print(final)

# 11th program to print the list after removing the 0th,4th,5th numbers
list2 = [12, 24, 35, 70, 88, 120, 155]
to_pop = [0, 4, 5]
print([list2.pop(z) for z in to_pop[::-1]])

# 12th program to print the list after removing delete numbers which are divisible by 5 and 7
list3 = [12, 24, 35, 70, 88, 120, 155]
fnl = [a for a in list3 if a % 5 != 0 and a % 7 != 0]
print(fnl)

# 13th program to generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random

print(random.sample([m for m in range(1, 1001) if m % 5 == 0 and m % 7 == 0], 5))
