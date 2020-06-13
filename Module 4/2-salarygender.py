import numpy as np
import pandas as pd

if __name__ == '__main__':
    # Extracting data from csv
    Data_file = pd.read_csv("SalaryGender.csv")

    # 2. number of men and women with phd

    men_phd= Data_file.query("Gender == 1 and PhD == 1")
    women_phd = Data_file.query("Gender == 0 and PhD == 1")
    print("The number of men with a PhD is : ", len(men_phd))
    print("The number of women with a PhD is :",len(women_phd))
