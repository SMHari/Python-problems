import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 1. Reading and storing of CSV into each columns

    # Extracting data from csv
    Data_file = pd.read_csv("SalaryGender.csv")
    # storing data in each column
    Salary_col = np.array(Data_file["Salary"])
    Gender_col = np.array(Data_file["Gender"])
    Age_col = np.array(Data_file["Age"])
    phd_col = np.array(Data_file["PhD"])

    # just for additional reference and printing of columns
    print(Salary_col)
    print(Gender_col)
    print(Age_col)
    print(phd_col)

