import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #  1. reading data
    sales_csv = pd.read_csv("sales_data.csv")

    # 2. Describing data
    sales_csv.describe()
    # print(sales_csv.describe())

    # 3. filter the data
    sales_csv_filtered = sales_csv.filter(['name', 'net_price', 'date'])
    # grouping by name
    sales_csv_grp = sales_csv_filtered.groupby('name')
    # print(sales_csv_grp)

    # 4. Plotting graph for total sales(quantity) by each customer

    sales_total = sales_csv.groupby('name')['quantity'].sum().reset_index()
    # print(sales_total)
    name = sales_total["name"].tolist()
    quantity = sales_total["quantity"].tolist()
    plt.xlabel("Customer name")
    plt.ylabel("Total sales")
    plt.title("name vs total sales")
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-small'
    )
    plt.bar(name, quantity)
    plt.legend()
    plt.show()


