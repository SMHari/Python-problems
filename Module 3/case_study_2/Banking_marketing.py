lst = []
prof = []
age = []
unique_lst = set({})
unique_age = set({})
age_dict = {}


def process(pro):
    if pro in unique_lst:
        print("Eligible for loan")
    else:
        print("Sorry. Not eligible for loan")


if __name__ == '__main__':

    file = open("../Module 3/case_study_2/bank-data.csv", "r")  # add correct relative path while testing. I've added mine
    file.readline()  # for skipping header line like job,age,y
    for line in file:
        lst = line.split(',')
        prof.append(lst[1])
        age.append(lst[0])

    unique_lst = set(prof)
    unique_age = sorted(set(age))
    # print(unique_lst)
    # print(unique_age)

    age_dict = {"min_age": min(unique_age), "max_age": max(unique_age)}
    # print(age_dict)

    print("Min age for loan eligibility is :", age_dict.get('min_age'))
    print("Max age for loan eligibility is :", age_dict.get('max_age'))

    while True:
        profession = input("Enter the profession for checking loan eligibility:(end to exit) \n").lower()

        if profession == 'end':
            print("Thanks. Quitting...")
            break
        else:
            process(profession)

    file.close()
