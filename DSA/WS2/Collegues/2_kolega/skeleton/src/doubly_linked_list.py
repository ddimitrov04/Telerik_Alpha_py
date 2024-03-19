from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
         return self._count

    @property
    def head(self):
        return self._head


    @property
    def tail(self):
        return self._tail
    

    def add_first(self, value):
        new_node = LinkedListNode(value)
        if self._count == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_before_head(new_node)
        self._count += 1

        

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self._count == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_after_tail(new_node)
        self._count += 1
    
    
    def insert_after(self, node, value):
        if not node:
            raise ValueError("Parameter node is None")
        new_node = LinkedListNode(value)
        new_node.prev = node
        new_node.next = node.next
        if node.next is None:
            self._tail = new_node
        else:
            node.next.prev = new_node
        node.next = new_node
        self._count += 1

           

    def insert_before(self, node, value):
        if not node:
            raise ValueError("Parameter node is None")
        new_node = LinkedListNode(value)
        new_node.prev = node.prev
        new_node.next = node
        if node.prev is None:
            self._head = new_node
        else:
            node.prev.next = new_node
        node.prev = new_node
        self._count += 1


    def remove_first(self):
        if self._count == 0:
            raise ValueError("List is empty")
        value = self._head.value
        if self._count == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._count -= 1
        return value
               

    def remove_last(self):
        if self._count == 0:
            raise ValueError("List is empty")
        value = self._tail.value
        if self._count == 1:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._count -= 1
        return value
        

    def find(self, value):
        current = self._head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
        
        

    def values(self):
        values_list = []
        current = self._head
        while current is not None:
            values_list.append(current.value)
            current = current.next
        return tuple(values_list)
 
        

    def _insert_before_head(self, value: LinkedListNode):
        value.next = self._head
        self._head.prev = value
        self._head = value
        

    def _insert_after_tail(self, value: LinkedListNode):
        value.prev = self._tail
        self._tail.next = value
        self._tail = value
       






    



 

   

    
    