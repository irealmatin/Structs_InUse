class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_tail(self , data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_head(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        lst_result = []
        current = self.head
        while current:
            lst_result.append(current.data)
            current = current.next
        return "->".join(map(str,lst_result))
    

    def delete(self,value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next

    def find(self , value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return "No match found!"
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def remove_duplicate(self):
        "belong to Exr3_7"
        current = self.head
        prev = None
        lst_unique = []
        while current:
            if current.data in lst_unique:
                prev.next = current.next
            else:
                lst_unique.append(current.data)
                prev = current
            current = current.next
        

if __name__ == "__main__":
    obj_ll = LinkedList()
    obj_ll.insert_at_tail(23)
    obj_ll.insert_at_tail(12)
    obj_ll.insert_at_tail(2)
    obj_ll.insert_at_tail(5)
    print(obj_ll)
    obj_ll.insert_at_head(8)
    print(obj_ll)
    obj_ll.delete(5)
    obj_ll.reverse()
    print(obj_ll)
    obj_ll.insert_at_head(2)
    print(obj_ll)
    obj_ll.remove_duplicate()
    print(obj_ll)


        