#The sparse matrix can be defined as the matrix that has a greater number of zero elements than the non-zero elements.

#------------------------------------------------------------------------------------------------------#
#-----------------------------------------------code---------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

class SparseMatrix:
    def __init__(self , rows , cols):
        self.rows = rows
        self.cols = cols
        self.matrix = {}

    def add_value(self , row , col , value):
        if value != 0 :
            self.matrix[(row , col)] = value

    def multiply(self):
        pass

    def add(self):
        pass
    
    def __str__(self):
        pass
