class Queue:
    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Maximum capacity must be greater than 0")
        
        self._max_capacity = max_capacity
        self._data = [None] * max_capacity
        self._front = 0
        self._rear = 0

    def __str__(self):
        return str(self._data[self._front:self._rear])

    def is_empty(self):
        return self._front == self._rear

    def is_full(self):
        return self._rear == self._max_capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        self._data[self._rear] = value
        self._rear += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        self._front+=1
        return self._data[self._front -1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")

        return self._data[self._front]

    @property
    def size(self):
        return self._rear - self._front

    @property
    def capacity(self):
        return self._max_capacity
    

# ------------------------------------------------------------------------------
#practical version of Queue 

class CircularQueue:
    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Maximum capacity must be greater than 0")

        self._max_capacity = max_capacity
        self._data = [None] * max_capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def __str__(self):
        if self.is_empty():
            return "[]"

        elements = []
        for i in range(self._size):
            elements.append(self._data[(self._front + i) % self._max_capacity])
        return str(elements)

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        value = self._data[self._front]
        self._data[self._front] = None  # Optional: clear the dequeued spot
        self._front = (self._front + 1) % self._max_capacity
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")

        return self._data[self._front]

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._max_capacity
    

if __name__ == "__main__":
    Q1 = CircularQueue(5)
    Q1.enqueue(3)
    Q1.enqueue(2)
    Q1.enqueue(10)
    print(Q1) # [3, 2, 10]
    print(Q1.capacity)
    print(Q1.is_full()) # Flase
    Q1.dequeue()
    print(Q1) # [2, 10]

