

class StaticArray:
    """a static array wich element should insert next to each other"""
    def __init__(self , size):

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
        return "[" + ", ".join(str(self.array[i]) for i in range(self.current_len)) + "]"
    

if __name__ == '__main__' :
    obj = StaticArray(10)
    print(obj.is_empty())
    obj.insert(2 , 0)
    print(obj)
    obj.insert(5,1)
    print(obj)
    obj.insert(33,2)
    obj.insert(9,3)
    obj.insert(15 , 4)
    obj.delete(1)
    print(obj)
# ---------------------------------------------------------------------------------------------------- #