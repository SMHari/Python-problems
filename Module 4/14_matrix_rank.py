import numpy as np

if __name__ == '__main__':
    rand_matrix = np.random.randint(0,10,size=(4,4))
    matrix = np.matrix(rand_matrix)
    print("The random matrix is:\n",matrix)
    matrix_rank = np.linalg.matrix_rank(matrix)
    print("The rank of the above matrix :", matrix_rank)