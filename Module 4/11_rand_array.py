import numpy as np

if __name__ == '__main__':
    np_rand_arr = np.random.randint(1, 1000, size=(3, 3))

    # sorting by 1st column
    sort_column1 = np_rand_arr[np_rand_arr[:, 0].argsort()]
    # sorting by 2nd column
    sort_column2 = np_rand_arr[np_rand_arr[:, 1].argsort()]
    # sorting by 3rd column
    sort_column3 = np_rand_arr[np_rand_arr[:, 2].argsort()]
    print("Original array:\n", np_rand_arr)
    print("Sorted by first column:\n", sort_column1)
    print("Sorted by Second column:\n", sort_column2)
    print("Sorted by third column:\n", sort_column3)
