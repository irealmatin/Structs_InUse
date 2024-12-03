#The sparse matrix can be defined as the matrix that has a greater number of zero elements than the non-zero elements.

#------------------------------------------------------------------------------------------------------#
#-----------------------------------------------code---------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

class SparseMatrix:
    def __init__(self , rows , cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def __len__(self) :
        return self.rows * self.cols
    
    def __getitem__(self , index):
        return self.data.get(index , 0)
    
    def __setitem__(self , index , value):
        if value != 0:
            self.data[index] = value
        elif index in self.data :
            del self.data[value]
    
    def __add__(self , other) :
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must valid for addition.")
        
        result_matrix = SparseMatrix(self.rows , self.cols)
        result_matrix.data = self.data.copy()

        for index,value in other.data.items():
            result_matrix[index] += value
        
        return result_matrix
    
    def __str__(self):
        rows = []
        for i in range(self.rows):
            for j in range(self.cols):
                rows.append(str(self[i,j]).rjust(5))
            rows.append("\n")
        return ''.join(rows)
    
    def __mul__(self , other):
        assert self.cols == other.rows , "matrix 1 cols should equal to matrix 2 rows"

        result_matrix = SparseMatrix(self.rows , other.cols)
        for i in range(self.rows) :
            for j in range(other.cols):
                for m in range(self.cols):
                    result_matrix[i,j] += self[i,m] * other[m,j]
        return result_matrix
    
    def __delitem__(self , index):
        return self.data.pop(index , None)

    

if __name__ == "__main__":
    mat1 = SparseMatrix(3, 3)
    mat1[1, 0] = 3
    mat1[2, 1] = 2
    mat1[1, 1] = 3
    mat1[2, 4] = 10
    print("mat1 Sparse Matrix:")
    print(mat1)

    mat2 = SparseMatrix(3, 3)
    mat2[1 , 0] = 11
    mat2[2, 1] = 2
    mat2[1, 2] = 3
    mat2[2, 3] = 8
    print("mat2 Sparse Matrix:")
    print(mat2)

    print("addition of mat1 , mat2 :")
    mat3 = mat1 + mat2
    print(mat3)
    print("multiplication of mat1 , mat2 :")
    mat3 = mat1 * mat2
    print(mat3)
