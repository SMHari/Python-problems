import pandas as pd
import numpy as np
if __name__ == '__main__':
    Data_file = pd.read_csv("SalaryGender.csv")

    # age and PhD columns in one DataFrame
    df = pd.DataFrame(Data_file)
    var = df[["Age", "PhD"]]
    print(var)

    # data of all people who don’t have a PhD
    to_delete = df[df["PhD"] == 0].index
    dropped = Data_file.drop(to_delete)
    print(len(dropped))


