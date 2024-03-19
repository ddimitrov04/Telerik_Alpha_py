from src.linked_list_node import LinkedListNode


class CustomQueue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.count

    @property
    def is_empty(self):
        return self.count == 0

    def enqueue(self, element):
        new = LinkedListNode(element, None)
        if self.is_empty:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.count += 1

    def dequeue(self):
        if self.is_empty:
            raise ValueError
        result = self.head.value
        self.head = self.head.next
        self.count -= 1
        if self.is_empty:
            self.tail = None
        return result

    def peek(self):
        if self.is_empty:
            raise ValueError
        return self.head.value
