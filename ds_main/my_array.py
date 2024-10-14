

class StaticArray:
    def __init__(self , size):

        self.size = size
        self.array = [None] * size
        self.current_len = 0

    
    def insert(self , number , position):
        if self.is_full == True:
            raise Exception("OPS . array is full !")
        
        if position < 0 or position > self.current_len :
            raise Exception("OPS . plz consider the bounderies!")
        
        # now shifting each number to insert new number
        for num in range(number - 1 , position , -1 ):
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
    

    def delete():
        pass


    def __len__(self):
        """return the size of array"""
        return self.size
    



# obj = StaticArray(15)
# print(obj.is_empty())
# obj.insert(2 , 0)