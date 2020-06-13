import numpy as np

if __name__ == '__main__':
    rand_arr = np.random.randint(0, 100, size=(3, 3))
    print(rand_arr)
    # by using roll function

    swap_arr = np.roll(rand_arr, -1, axis=0)
    print("Swapped revere using roll : \n", swap_arr)

    # by this reassigning procedure

    rand_arr[[0, 1]] = rand_arr[[1, 0]]
    print("Swapped 0th and 1st row :\n", rand_arr)
