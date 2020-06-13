import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 50)

if __name__ == '__main__':
    #################################################################
    # Reading Csv files
    Ds_csv = pd.read_csv("DSScoreTerm1.csv")
    Mat_csv = pd.read_csv("MathScoreTerm1.csv")
    Phy_csv = pd.read_csv("PhysicsScoreTerm1.csv")

    # print(Ds_csv)
    #################################################################
    # removing name and ethnicity column (to ensure confidentiality)

    After_drop_Ds = Ds_csv.drop(columns=["Name", "Ethinicity"])
    After_drop_Mat = Mat_csv.drop(columns=["Name", "Ethinicity"])
    After_drop_Phy = Phy_csv.drop(columns=["Name", "Ethinicity"])

    # print(After_drop_Ds)
    # print(After_drop_Mat)
    # print(After_drop_Phy)

    ##################################################################
    # Fill missing score data with zero

    Ds_remove_nan = After_drop_Ds.fillna(0)
    Mat_remove_nan = After_drop_Mat.fillna(0)
    Phy_remove_nan = After_drop_Phy.fillna(0)

    # verification of any Nan values.This returns empty frame as the nan is replaced by zero
    # print(Ds_remove_nan[Ds_remove_nan.isna().any(axis=1)])
    # print(Mat_remove_nan[Mat_remove_nan.isna().any(axis=1)])
    # print(Phy_remove_nan[Phy_remove_nan.isna().any(axis=1)])

    ##################################################################
    # Merge the three files

    Dfs_all = [Ds_remove_nan, Mat_remove_nan, Phy_remove_nan]
    Merged_Dfs = pd.concat(Dfs_all)

    # print(Merged_Dfs)
    ##################################################################
    # Change Sex(M/F) Column to 1/2 for further analysis

    sex = {'M': 1, 'F': 2}
    Merged_Dfs.Sex = [sex[item] for item in Merged_Dfs.Sex]
    # print(Merged_Dfs)

    ##################################################################
    # Store the data in new file – ScoreFinal.csv

    Merged_Dfs.to_csv("ScoreFinal.csv", header=True, index=False)

    ##################################################################
    # Enhancements

    # Convert ethnicity to numerical value
    # Loaded csv are Ds_csv, Mat_csv, Phy_csv
    # since Merged_Dfs doesn't have ethnicity column
    ethnicity = {'White American': 1, 'European American': 2, 'Hispanic': 3, 'African American': 4}

    Ds_csv.Ethinicity = [ethnicity[item] for item in Ds_csv.Ethinicity]
    Mat_csv.Ethinicity = [ethnicity[item] for item in Mat_csv.Ethinicity]
    Phy_csv.Ethinicity = [ethnicity[item] for item in Phy_csv.Ethinicity]

    # print(Ds_csv)
    # print(Mat_csv)
    # print(Phy_csv)

    ##################################################################
    # Fill the missing score for a student to the average of the class
    # already processed Merged_Dfs
    # finding missing rows in Dataframe

    # print(Ds_csv[Ds_csv.isnull().any(axis=1)], Ds_csv.isnull().sum())
    # print(Mat_csv[Ds_csv.isnull().any(axis=1)], Mat_csv.isnull().sum())
    # print(Phy_csv[Ds_csv.isnull().any(axis=1)], Phy_csv.isnull().sum())

    # populating the missing values in Dataframe score with average

    Ds_Score_fill = Ds_csv["Score"].fillna(Ds_csv["Score"].mean())
    Mat_Score_fill = Mat_csv["Score"].fillna(Mat_csv["Score"].mean())
    Phy_Score_fill = Phy_csv["Score"].fillna(Phy_csv["Score"].mean())
