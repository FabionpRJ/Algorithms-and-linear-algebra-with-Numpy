import numpy as np

# This file is responsible for storing my linear algebra algorithms
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

#---------------------------------------------- BACK SUBSTITUTION --------------------------------
# Algorithm to find solutions in upper triangular matrices.
# 
# Receives a Upper Triangular matrix, and a solution matrix
#
# Output: Find the value of the unknows that leave the collumns in the solution matrix.
#
# Upper_matrix * y = Solution
def back_substitution(upper_matrix, solution):
    vector_y = np.zeros((upper_matrix.shape[1],1))                                                #
    for i in range((upper_matrix.shape[0]-1),-1,-1):               #Execute over the rows
        value = 0 
        for j in range(i+1,upper_matrix.shape[1]):           #Execute over the collumns... on the right
            if i != j:
                value += upper_matrix[i][j]*vector_y[j][0]
        vector_y[i][0] = (solution[i][0] - value)/upper_matrix[i][i]  #Define one solution element
        value = 0                                               #resets the values...
    return vector_y
    



#---------------------------------------------- GAUSSIAN ELIMINATION --------------------------------
# Decompose Matrices in Upper and Lower Matrices
# 
# Receives a nxn matrix
#
# Output: Upper and Lower Matrix
#


def gaussian_elimination(matrix):
    Upper_matrix = np.copy(matrix)
    #Lower_matrix = np.identity(matrix.shape[0])
    for i in range(1,Upper_matrix.shape[0]):                                         # Starting with the row[1] (second row)
        pivot = Upper_matrix[i-1][i-1].tolist()
        for j in range(i,Upper_matrix.shape[0]):
            divisor_factor = Upper_matrix[j][i-1]/pivot

            for k in range(Upper_matrix.shape[0]):
                Upper_matrix[j][k] = Upper_matrix[j][k] - Upper_matrix[i-1][k]*divisor_factor
    
    return Upper_matrix

