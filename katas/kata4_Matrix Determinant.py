import numpy
def determinant(matrix):
    M = round(numpy.linalg.det(matrix), 0)         
    print(M)




determinant([[1]]) 
determinant([[1, 2],[1, 2]])
determinant([[2,4,2],[3,1,1],[1,2,0]])