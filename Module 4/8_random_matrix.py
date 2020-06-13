import numpy as np

if __name__ == '__main__':
    random_mat = np.random.randint(1, 1000, size=(10, 10))
    print(random_mat)
    print("Max value in random matrix is :", np.max(random_mat))
    print("Min value in random matrix is :", np.min(random_mat))
