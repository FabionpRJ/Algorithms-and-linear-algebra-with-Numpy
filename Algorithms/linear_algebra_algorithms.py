import numpy as np

# This File is responsible for armazain my linear algebra algorithms
#


#---------------------------------------------- PERMUTATION --------------------------------------
# Permutation is the act of changing the order of rows.
# During the process of permutation, we produce a permutation matrix P
# and alter the order of the given matrix.
# Permuting matrices is a fundamental process for various algorithms in linear algebra, 
# such as Gaussian Elimination, so we will start with it.

def permutate_matrix(matrix,row_1=0, row_2=0, Permutation=0):
    if Permutation == 0:
        P = np.zeros((matrix.shape[0],matrix.shape[0])) # Create the matrix P
        for i in range(P.shape[0]):                     # Turns him in the Identity matrix
            P[i][i] = 1                                 # by givin the value 1 to each element in diagonal (Pij, where i = j).
    else:
        P = Permutation

    swap = matrix[row_1].tolist()                       # We turn the rows into lists before assigning their values. 
    matrix[row_1] = matrix[row_2].tolist()              # This is because referencing Matrix[x] references its address.
    matrix[row_2] = swap

    swap = P[row_1].tolist()                            # Doing the same, but for P.
    P[row_1] = P[row_2].tolist()
    P[row_2] = swap
    return matrix, P                                    #Return the matrix, and P

    

