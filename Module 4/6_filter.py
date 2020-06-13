import numpy as np

if __name__ == '__main__':
    arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    arr_np = np.array(arr)
    print(arr_np)
    print("elements greater than 5 are : ", arr_np[arr_np > 5])
