import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    temp_csv = pd.read_csv("CityTemps.csv")

    moscow = temp_csv["Moscow"]
    Sanfransico = temp_csv["San Francisco"]

    plt.hist(moscow, len(moscow), facecolor='blue', label="moscow")
    plt.hist(Sanfransico, len(Sanfransico), facecolor='red',label="San Francisco")

    plt.xlabel("Temperature")
    plt.ylabel("periods frequency")
    plt.title("Temperatures of Mosco and San Francisco")

    plt.legend()

    plt.show()

