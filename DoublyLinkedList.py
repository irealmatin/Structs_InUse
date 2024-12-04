# belong to EXR3_4

class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def split_list(self):
        even_list = DoublyLinkedList()
        odd_list = DoublyLinkedList()
        current = self.head
        while current:
            if current.data % 2 == 0:
                even_list.insert(current.data)
            else:
                odd_list.insert(current.data)
            current = current.next
        return even_list, odd_list

    def __str__(self):
        res = []
        current = self.head
        while current:
            res.append(current.data)
            current = current.next
        return str(res)

    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev is None:  # If it's the head node
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:  # Middle or last node
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return True  # Node deleted
            current = current.next
        return False  # Node not found

    def reverse(self):
        if not self.head: 
            return    
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def insert_at(self, index, value):
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        new_node = self.Node(value)
        if index == 0:  # Insert at the beginning
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            count += 1
            current = current.next

        raise IndexError("Index out of bounds")


#Test -----------------------------------------------------

if __name__ == "__main__" :
    obj_dll = DoublyLinkedList()

    # Insert values
    obj_dll.insert(10)
    obj_dll.insert(20)
    obj_dll.insert(30)
    obj_dll.insert(8)
    obj_dll.insert(5)
    obj_dll.insert(3)

    print("Length:", obj_dll.length())  

    obj_dll.delete(20)
    print("After deletion:", obj_dll)  

    print("Find 10:", obj_dll.find(10))  
    print("Find 20:", obj_dll.find(20))  

    obj_dll.insert_at(1, 25)
    print("After insert_at:", obj_dll)  

    obj_dll.reverse()
    print("Reversed List:", obj_dll)  
