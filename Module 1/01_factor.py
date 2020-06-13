def func():
    factor = []
    even = []
    odd = []
    n = int(input("Enter the number to find the factor:"))
    for i in range(1, n):
        if (n % i) == 0:
            factor.append(i)
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
    print("Factors are:", factor)
    print("odd numbered factor:", odd)
    print("Even numbered factor:", even)


if __name__ == '__main__':
    func()
