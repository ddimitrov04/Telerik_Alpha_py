from src.linked_list_node import LinkedListNode


class CustomQueue:
    def __init__(self):
        self.head = None
        self.tail = None

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


    def enqueue(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next



    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        else:
            make_first = self.head.next
            removed_from_front = self.head
            self.head = make_first

        return removed_from_front.value

    def peek(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        else:
            return self.head.value
