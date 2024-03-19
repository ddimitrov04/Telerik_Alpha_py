from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.head = None
        self._count = 0

    @property
    def count(self):
        return self._count
    
    @property
    def is_empty(self):
        return self.count == 0
    
    def push(self, value):
        new_node = LinkedListNode(value)
        self.head = new_node
        self._count += 1
    
    def pop(self):
        if self.is_empty:
            raise ValueError("The stack is empty.")
        value = self.head.value
        self.head = self.head.next
        self._count -= 1
        return value

    def peek(self):
        if self.is_empty:
            raise ValueError("The stack is empty.")
        return self.head.value