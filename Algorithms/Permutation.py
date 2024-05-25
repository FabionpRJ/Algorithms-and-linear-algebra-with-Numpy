import numpy as np

# This class is responsible for permuting the matrix, changing the row positions, and creating a permutation matrix.

class Permutation:
    def __init__(self, array, line_1=0,line_2=0):
        self.array = array
        self.line_1 = line_1
        self.line_2 = line_2
        

    def permutate(self):
        ...
