

if __name__ == '__main__':
    str = input("ENTER THE SENTENCE:")
    lst = str.split()
    dup_rem = set(lst)
    result = list(sorted(dup_rem))
    sortedstr = ' '.join(result)
    print(sortedstr)
