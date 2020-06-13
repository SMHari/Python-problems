import numpy as np

if __name__ == '__main__':
    arr = [np.nan, 1 , 2 ,np.nan, 3, 4, 5]
    arr_np = np.array(arr,dtype=float)
    print(arr_np[~np.isnan(arr_np)])