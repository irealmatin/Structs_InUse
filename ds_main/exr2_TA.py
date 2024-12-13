# Matin Mohammadi : 40011173069
# Second series of data structure exercises
# *Note : I used the class written in this link : https://github.com/STRstark/Ds-Classes-In-Python/blob/main/DataStructures-Py/Stack.py

class Stack:
    __Data =[]
    __Max_Capacity = 0
    __Top = -1
    
    def __init__(self , capacity):
        self.__Data = [None] * capacity
        self.__Max_Capacity = capacity
        
    def __str__(self):
        return f"{self.__Data}"
    
    def IsFull(self) :
        return self.__Top == self.__Max_Capacity-1
    
    def IsEmpty(self) :
        return self.__Top == -1
    
    def Push(self , value) :
        if self.IsFull() :
            raise OverflowError("Stack OverFlow")    
        
        self.__Top +=1
        self.__Data[self.__Top] = value
        
    def Pop(self):
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow , You are trying to pop from an empty list")
        
        self.__Top -=1
        return self.__Data[self.__Top+1]
    
    def Peak(self):
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow , You are trying to peak from an empty list")
        
        return self.__Data[self.__Top]

    def infix_to_postfix(self, infix_expression):
        """
        logic : convert an infix expression into a postfix expression
        Time complexity : O(n)
        """
        operators_priority = {'+': 1, '*': 2, '/': 2, '-': 1}  # Set operator priority[*>+ or 2>1]
        valid_operators = operators_priority.keys()
        stack = Stack(self.__Max_Capacity)
        list_postfix = []  # Store final postfix expression

        for exp in infix_expression:
            if exp.isalnum():  # when no operator exist : ["ABPQ"]
                list_postfix.append(exp)
            elif exp == '(':
                stack.Push(exp)
            elif exp == ')':
                while not stack.IsEmpty() and stack.Peak() != '(':
                    list_postfix.append(stack.Pop())
                stack.Pop()  
            elif exp in valid_operators:
                while (not stack.IsEmpty() and \
                      stack.Peak() != '(' and \
                      operators_priority[exp] <= operators_priority[stack.Peak()]):
                    list_postfix.append(stack.Pop())
                stack.Push(exp)

        while not stack.IsEmpty():
            list_postfix.append(stack.Pop())

        return ''.join(list_postfix)


    def infix_to_prefix(self, infix_expression):
        """
        logic : Converts an infix expression to prefix.
        Time Complexity: O(n)
        """
        reversed_expression = []
        for char in infix_expression[::-1]:
            if char == '(':
                reversed_expression.append(')')
            elif char == ')':
                reversed_expression.append('(')
            else:
                reversed_expression.append(char)
        reversed_expression = ''.join(reversed_expression)

        postfix = self.infix_to_postfix(reversed_expression)
        return postfix[::-1]


    def postfix_to_infix(self , postfix_expression):
        """
        logic : convert postfix expression to an infix one
        Time Complexity : O(n)
        """
        stack = Stack(self.__Max_Capacity)

        def is_allnum(x):
            return x.isalnum()

        for char in postfix_expression:
            if is_allnum(char):
                stack.Push(char)  
            else:
                if stack.__Top < 1:
                    raise ValueError("Invalid postfix expression")

                op1 = stack.Pop() 
                op2 = stack.Pop()  

                new_expr = f'({op2}{char}{op1})'
                stack.Push(new_expr)  

        if stack.__Top != 0:
            raise ValueError("Invalid postfix expression")

        return stack.Pop()
    
    def copy(self):
        new_stack = Stack(self.__Max_Capacity)
        new_stack.__Top = self.__Top  
        new_stack.__Data = self.__Data[:] 
        return new_stack

    @staticmethod
    def merge_stacks(stack1, stack2):
        """
        logic : merge and sort two sorted stacks 
        Time Complexity : O(m+n)
        """
        copy_stack1 = stack1.copy() # to prevent the initial stacks from being damaged
        copy_stack2 = stack2.copy()

        capacity = copy_stack1.__Max_Capacity + copy_stack2.__Max_Capacity
        temp_stack = Stack(capacity)

        while not copy_stack1.IsEmpty() or not copy_stack2.IsEmpty():
            if copy_stack1.IsEmpty():
                temp_stack.Push(copy_stack2.Pop())
            elif copy_stack2.IsEmpty():
                temp_stack.Push(copy_stack1.Pop())
            else:
                if copy_stack1.Peak() >= copy_stack2.Peak():
                    temp_stack.Push(copy_stack1.Pop())
                else:
                    temp_stack.Push(copy_stack2.Pop())

        result_stack = Stack(capacity)
        temp_list = [] 

        while not temp_stack.IsEmpty():
            temp_list.append(temp_stack.Pop())

        temp_list.reverse() # base on the question[....ميخواهيم به صورت نزولي ] , the biggest value should be in tail of stack[desending order]

        for item in temp_list:
            result_stack.Push(item)

        return result_stack



        


if __name__ == "__main__":
    capacity = 20
    stack = Stack(capacity)

    infix_expression = "((a*b)+c)/2".upper()

    postfix_expression = stack.infix_to_postfix(infix_expression)
    print("testing Postfix Expression:\n", postfix_expression)
    print("------------------------------------------------------------------")
    infix_expression = "((a*b)+c)/2".upper()
    prefix_expression = stack.infix_to_prefix(infix_expression)
    print("testing Prefix Expression:", prefix_expression)
    print("-------------------------------------------------------------------")
    print("testing postfix to infix :\n")
    postfix_expression = "AB*C+2/"
    try:
        infix_expression = stack.postfix_to_infix(postfix_expression)
        print(f"Postfix: {postfix_expression}\nInfix: {infix_expression}")
    except ValueError as e:
        print(f"Error: {e}")
    print("--------------------------------------------------------------------")

    stack1 = Stack(5)
    stack2 = Stack(5)
    for item in [1, 3, 5,6,10]:
        stack1.Push(item)
    for item in [2,4,6,18]:
        stack2.Push(item)

    merged_stack = Stack.merge_stacks(stack1, stack2)
    print("testing Merged stack:\n",merged_stack)


# outputs
"""
testing Postfix Expression:
 AB*C+2/
------------------------------------------------------------------
testing Prefix Expression: /+*ABC2
-------------------------------------------------------------------
testing postfix to infix :

Postfix: AB*C+2/
Infix: (((A*B)+C)/2)
--------------------------------------------------------------------
testing Merged stack:
 [18, 10, 6, 6, 5, 4, 3, 2, 1, None]
"""
