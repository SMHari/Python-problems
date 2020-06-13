sum=0
n = int(input("Enter the number:"))
for i in range(1,n+1):
    sum+=(i/(i+1))
print(round(sum,2))