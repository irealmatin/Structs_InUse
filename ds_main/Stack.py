class Stack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._data = [None] * capacity
        self._max_capacity = capacity
        self._top = -1

    def __str__(self):
        return str(self._data[:self._top + 1])

    def is_full(self):
        return self._top == self._max_capacity - 1

    def is_empty(self):
        return self._top == -1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack Overflow: Cannot push to a full stack.")
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        value = self._data[self._top]
        self._data[self._top] = None  
        self._top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot peek into an empty stack.")
        return self._data[self._top]
    

# this type of stack should be static . so we cant resize it !
    # def resize(self, new_capacity):
    #     if new_capacity <= 0:
    #         raise ValueError("New capacity must be a positive integer.")
    #     if new_capacity < self._top + 1:
    #         raise ValueError("New capacity cannot be less than the number of elements in the stack.")

    #     self._data = self._data[:self._top + 1] + [None] * (new_capacity - (self._top + 1))
    #     self._max_capacity = new_capacity


if __name__ == "__main__" :
    stack = Stack(5)
    try:
        stack.push(5)
        stack.push(10)
        stack.push(3)
        print(stack)
        print(stack.peek())
        print(stack.pop())
        print(stack)

    except (OverflowError, IndexError, ValueError) as error:
        print(error)
    finally :
        print("Done!")

        