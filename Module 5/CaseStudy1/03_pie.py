import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cars_csv = pd.read_csv("Cars2015.csv")

    Make_list = []
    count_list = []
    #  Selecting only required column from DataFrame
    df = cars_csv.filter(['Make'], axis=1)
    # print(df)

    # Trimming string values of the column values before grping for correct result
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    # print(df)

    # Grouping to find count of sales.
    df = df.groupby(["Make"]).size().reset_index(name="Counts")
    Make_list = df["Make"].tolist()
    count_list = df["Counts"].tolist()

    # for making exploding graph logic. Can also be done in list comprehension
    expod_tup = []
    count_max = max(count_list)
    for i in count_list:
        if i == count_max:
            i = i / 100
            expod_tup.append(i)
        else:
            i = 0
            expod_tup.append(i)
    print(expod_tup)
    explode = tuple(expod_tup)

    # the name of the manufacture with the largest releases is shown exploded in the pie chart

    plt.figure(figsize=(50, 10))
    plt.pie(count_list, labels=Make_list, autopct='%1.1f%%', explode=explode)
    plt.show()
