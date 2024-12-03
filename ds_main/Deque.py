# belong to exr3_3 
class Deque:
    def __init__(self , size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def __str__(self):
        if self.is_empty():
            return "[]"

        elements = []
        i = self.front
        while True:
            elements.append(self.deque[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return str(elements)

    
    def push_front(self , value):
        if self.is_full():
            raise OverflowError("Deque is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value


    def push_rear(self , value):
        if self.is_full():
            raise OverflowError("Deque is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = value


    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.deque[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value
    

    def pop_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.deque[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        return value

if __name__ == "__main__":   
    dq = Deque(5)

    dq.push_front(10)  # Deque: [10]
    dq.push_rear(20)   # Deque: [10, 20]
    dq.push_front(5)   # Deque: [5, 10, 20]
    dq.push_rear(25)   # Deque: [5, 10, 20, 25]
    dq.push_front(1)   # Deque: [1, 5, 10, 20, 25]

    print(dq)  # Output: [1, 5, 10, 20, 25]

    print(dq.pop_front())  # Output: 1
    print(dq.pop_rear())   # Output: 25

    print(dq)  # Output: [5, 10, 20]

    dq.push_rear(30)       # Deque: [5, 10, 20, 30]
    print(dq)  # Output: [5, 10, 20, 30]
