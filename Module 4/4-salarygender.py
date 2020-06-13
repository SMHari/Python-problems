import pandas as pd


if __name__ == '__main__':
    # Extracting data from csv
    Data_file = pd.read_csv("SalaryGender.csv")

    # 2. number of men and women with phd

    total_phd = Data_file.query("PhD == 1")
    print("Total number of people who have a PhD degree is: ",len(total_phd))