import inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sn

if __name__ == '__main__':
    # 1. Data collection
    SclData_csv = pd.read_csv("middle_tn_schools.csv")
    print(SclData_csv.head())
    SclData_csv.describe()

    # 2.Group by school ratings
    scl_rating_grped = SclData_csv.groupby("school_rating").describe()
    print(scl_rating_grped.head())

    # 3.Correlation analysis
    reduced_lunch_col = SclData_csv["reduced_lunch"]
    school_rating_col = SclData_csv["school_rating"]
    corelation_analysis = reduced_lunch_col.corr(school_rating_col)
    print(corelation_analysis)

    # 4. Scatter plot

    scatter_plot = SclData_csv.plot.scatter(x="reduced_lunch", y="school_rating", c='Red')
    plt.show()
    # SclData_csv.plot(kind='scatter',x = "reduced_lunch",y ="school_rating",c='Red')
    # plt.show()

    # 5. Correlation Matrix

    CorrMatrix = SclData_csv.corr()
    sn.heatmap(CorrMatrix, annot=True)
    plt.show()
