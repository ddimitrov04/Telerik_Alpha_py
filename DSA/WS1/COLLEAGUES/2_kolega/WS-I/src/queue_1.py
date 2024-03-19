from src.linked_list_node import LinkedListNode


class CustomQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    @property
    def count(self):
        return self._count
    
    @property
    def is_empty(self):
        return self.count == 0
    
    def enqueue(self, value):
        new_node = LinkedListNode(value)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1
    
    def dequeue(self):
        if self.is_empty:
            raise ValueError("The queue is empty.")
        value = self.head.value
        self.head = self.head.next
        self._count -= 1
        return value

    def peek(self):
        if self.is_empty:
            raise ValueError("The queue is empty.")
        return self.head.value