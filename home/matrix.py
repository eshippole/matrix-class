import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def dot_product(vectorA, vectorB):
    result = 0
    for i in range(len(vectorA)):
        result += vectorA[i] * vectorB[i]
    return result
    

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            deter = (a * d) - (b * c)
            return deter


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        diagonalSum = []
        
        for i in range(self.h):
            diagonalSum.append(self[i][i])
            summation = sum(diagonalSum)
        return summation
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
            
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        determ = self.determinant()
        
        if determ == 0:
            raise(ValueError, "Determinant can not be 0")
            
        if self.h == 1:
            determ = self.determinant()
            matrix_inverse = [[1/determ]]
            
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            factor = 1./determ
            matrix_inverse = [[d,-b],[-c,a]]
            for i in range(len(matrix_inverse)):
                for j in range(len(matrix_inverse[0])):
                    matrix_inverse[i][j] = factor * matrix_inverse[i][j]
        return Matrix(matrix_inverse)
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        
        for j in range(self.w):
            transposed_row = []
            for i in range(self.h):
                transposed = self[i][j]
                transposed_row.append(transposed)
            matrix_transpose.append(transposed_row)
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        else:
            
            matrix_sum = []
            
            for i in range(self.h):
                rows = []
                for j in range(self.w):
                    sum_matrix = self.g[i][j] + other.g[i][j]
                    rows.append(sum_matrix)
                matrix_sum.append(rows)
            return Matrix(matrix_sum)
                    
        #   
        # TODO - your code here
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        negative_matrix = []
        
        for i in range(self.h):
            rows = []
            for j in range(self.w):
                negative_scalar = self.g[i][j] * -1
                rows.append(negative_scalar)
            negative_matrix.append(rows)
        return Matrix(negative_matrix)
        #   
        # TODO - your code here
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        else:
            matrix_sub = []
            
            for i in range(self.h):
                rows = []
                for j in range(self.w):
                    sub_matrix = self.g[i][j] - other.g[i][j]
                    rows.append(sub_matrix)
                matrix_sub.append(rows)
            return Matrix(matrix_sub)
        #   
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        mult_result = []
        transposeB = other.T()
        
        for i in range(self.h):
            row_result = []
            for j in range(transposeB.h):
                dp = dot_product(self.g[i], transposeB.g[j])
                row_result.append(dp)
            mult_result.append(row_result)
        return Matrix(mult_result)
                
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
            new_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.g[i][j] * other)
                new_matrix.append(row)
            return Matrix(new_matrix)
            #   
            # TODO - your code here
            #
            