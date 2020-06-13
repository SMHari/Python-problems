import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    hurr_csv = pd.read_csv("Hurricanes.csv")
    x = hurr_csv["Year"]
    y = hurr_csv["Hurricanes"]
    plt.xlabel("Year")
    plt.ylabel("Hurricanes")
    plt.grid(True)
    plt.title("Year vs Hurricane")
    plt.bar(x, y)
    plt.show()
