from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.count = 0
        self.head = None

    def __len__(self):
        return self.count

    @property
    def is_empty(self):
        return self.count == 0

    def push(self, element):
        self.head = LinkedListNode(element, self.head)
        self.count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError
        else:
            result = self.head.value
            self.head = self.head.next
            self.count -= 1
            return result

    def peek(self):
        if self.is_empty:
            raise ValueError
        else:
            return self.head.value
