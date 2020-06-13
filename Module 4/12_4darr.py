import numpy as np

if __name__ == '__main__':

    # 4-d array
    fourd_arr = np.random.randint(0,10,size=(3,4,3,4))

    # solution by passing a tuple of axes

    sum = fourd_arr.sum(axis=(-2, -1))
    print(fourd_arr)
    print(sum)