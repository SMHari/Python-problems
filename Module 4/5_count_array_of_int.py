import numpy as np
import pandas as pd

if __name__ == '__main__':
    arr = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
    # printing unique occurence
    arr_uniq_count, occurence = np.unique(arr, return_counts=True)
    # print(arr_uniq_count)
    print(occurence)
