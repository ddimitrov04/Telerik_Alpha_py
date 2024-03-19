class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next: LinkedListNode | None = None
        self.prev: LinkedListNode | None = None
