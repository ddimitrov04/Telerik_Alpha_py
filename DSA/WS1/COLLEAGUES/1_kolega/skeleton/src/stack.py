
from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.head = None


    @property
    def count(self):
        num = 0
        cur = self.head
        while cur:
            num += 1
            cur = cur.next
        return num

    @property
    def is_empty(self):
        return self.head is None


    def push(self, value):
        new_node = LinkedListNode(value)
        if self. head is None:
            self.head = new_node
        else:
            current = self.head
            self.head = new_node
            self.head.next = current

    def peek(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        else:
            return self.head.value

    def pop(self):
        if self.head is None:
            raise ValueError("Stack is empty")
        else:
            current = self.head
            self.head = current.next
        return current.value
