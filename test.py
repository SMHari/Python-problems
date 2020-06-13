# a=[]
# n = int(input())
# for i in range(n):
#     a.append(i)
# print(a)
#


# dic = {'name': 'hari','age':22}
# print(dic)
# s = str(dic)
# print(s)
# print(list(s))

lst = [12, 24, 35, 70, 88, 120, 155]
lst = [x for x in lst if x % 5 != 0 and x % 7 != 0]
print(lst)  # [12, 24, 88]

list3 = [12, 24, 35, 70, 88, 120, 155]
fnl = [x for x in list3 if x%5 !=0 and x%7!=0]
print(fnl)



#
# divisible = [5, 7]
# list2 = [12, 24, 35, 70, 88, 120, 155]
# div5 = []
# for y in list2:
#     for z in divisible:
#         print(y, z)
#         calc = int(y % z)
#         print(calc)
#         if calc == 0:
#             div5.append(y)
# val = sorted(set(div5))
# print(val)
# print(list2)
# for i in val:
#     list2.remove(i)
#     print(list2)
# res = [list2.remove(i) for i in val]
# print(res)

# list2 = [12, 24, 35, 70, 88, 120, 155]
# to_pop = [0, 4, 5]
# [list2.pop(z) for z in to_pop[::-1]]
# print(list2)
