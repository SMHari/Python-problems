if __name__ == '__main__':
    nlst=[]
    lt =[]
    x=int(input())
    for _ in range(x):
        name = input()
        score = float(input())
        nlst.append([name,score])
        lt.append(score)

    s = sorted(set(lt))
    second_lowest = s[1]
    for name, score in sorted(nlst):
        if score == second_lowest:
            print(name)