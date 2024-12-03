#------------------------------------------------------------------------------------------------------#
#-----------------------------------------------code---------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

class StaticArray_V1:
    """a static array wich element should insert next to each other"""
    def __init__(self ,size):

        self.size = size
        self.array = [None] * size
        self.current_len = 0

    
    def insert(self , number , position):
        """insert number in specified position"""
        if self.is_full == True:
            raise Exception("OPS . array is full !")
        
        if position < 0 or position > self.current_len :
            raise Exception("OPS . plz consider the bounderies!")
        
        # now shifting each number to insert new number
        for num in range(self.current_len - 1 , position -1 , -1 ):
            self.array[num + 1] = self.array[num]

        self.array[position] = number
        self.current_len += 1 
        


    def is_full(self):
        """check if the array is full or not"""
        return self.current_len == self.size
    
    def is_empty(self):
        """check if array is empty or not"""
        if self.current_len == 0 :
            return True
        return False
    

    def delete(self , position):
        """delete a value in specified"""
        if self.is_empty == True :
            raise Exception("OPS . nothing found to delete ! you have an empty array . ")
        
        if position < 0 or position >= self.current_len :
            raise Exception("OPS . plz consider the bounderies!")

        for num in range(position , self.current_len - 1):
            self.array[num] = self.array[num + 1]

        self.array[self.current_len - 1] = None
        self.current_len -= 1



    def __len__(self):
        """return the size of array"""
        return self.size

    def __str__(self):
        """for make printable array"""
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
    

if __name__ == '__main__' :
    obj = StaticArray_V1(10)
    print(obj.is_empty())
    obj.insert(2 , 0)
    obj.insert(5,1)
    obj.insert(33,2)
    obj.insert(9,3)
    obj.insert(15 , 4)
    obj.delete(1)
    print(obj) #[2, 33, 9, 15, None, None, None, None, None, None]


# ---------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------------- #



class StaticArray_V2(StaticArray_V1) :
    """a static array wich element can insert in optional index(in StaticArray_V1 you should insert next to prev number ->[append]) .
       array - > [2, 33, 9, 15, None, None, None, None, None, None]
       flag  - > [T,T,T,T,F,F,F,F,F,F]
    
    """
    def __init__(self, size):
        super().__init__(size)
        self.array = [None] * size
        self.flag = [False] * size

    def insert(self, number, position):
        """insert number in specified position"""

        if self.is_full():
            raise Exception("OPS. Array is full!")
        elif position < 0 or position >= self.size:
            raise Exception("OPS. Please consider the boundaries!")

        # Check if position is empty
        if not self.flag[position]:
            self.array[position] = number
            self.flag[position] = True
        else:
            # Search for the next available position
            j = position + 1
            while j < len(self.array) and self.flag[j]:
                j += 1

            if j < len(self.array):
                # Shift elements right
                for i in range(j - 1, position - 1, -1):
                    self.array[i + 1] = self.array[i]
                self.array[position] = number
            else:
                # Shift elements left
                t = position - 1
                while t >= 0 and self.flag[t]:
                    t -= 1
                for i in range(t + 1, position):
                    self.array[i - 1] = self.array[i]
                self.array[position] = number
            
            self.flag[position] = True

    def is_full(self):
        return all(self.flag)
    
    def is_empty(self):
        return all(not flags for flags in self.flag)
    
    def delete(self, position):
        if self.is_empty():
            raise Exception("Ops , Array is empty!")
        elif not self.flag[position]:
            raise Exception("Error: No element to delete at this position!")
        
        self.array[position] = None
        self.flag[position] = False
        


    
if __name__ == "__main__" :
    objv2 = StaticArray_V2(10)
    objv2.insert(1,0)
    print(objv2)
    objv2.insert(3,5) # [1, None, None, None, None, 3, None, None, None, None]
    print(objv2.flag) # [True, False, False, False, False, True, False, False, False, False]
    print(objv2.is_empty()) # Pass !
    objv2.insert(22,7)
    print(objv2) # [1, None, None, None, None, 3, None, 22, None, None]
    objv2.delete(0)
    print(objv2) # [None, None, None, None, None, 3, None, 22, None, None]


        
