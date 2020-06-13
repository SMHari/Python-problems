import numpy as np

if __name__ == '__main__':
    # elemnts with 0 to 10 array

    # numpy array
    arr_np = np.arange(0,11)
    arr_negate = ~arr_np[arr_np[2:9]]
    print("Array original:", arr_np)
    print("Negated array between 3 to 9:", arr_negate)
