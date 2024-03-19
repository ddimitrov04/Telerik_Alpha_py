from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode | None = None
        self._tail: LinkedListNode | None = None
        self._count = 0

    @property
    def is_empty(self):
        if self._count == 0:
            return True
        elif self._count >= 1:
            return False

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
        self._insert_before_head(value)

    def add_last(self, value):
        self._insert_after_tail(value)

    def insert_after(self, node, value):
        if node is None:
            raise ValueError("Cannot insert after a None node!")

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
        if node is None:
            raise ValueError("Cannot insert before a None node")

        new_node = LinkedListNode(value)
        new_node.next = node
        new_node.prev = node.prev

        if node.prev is None:
            self._head = new_node
        else:
            node.prev.next = new_node

        node.prev = new_node
        self._count += 1

    def remove_first(self):
        if self.is_empty:
            raise ValueError("Cannot remove items from an empty list!")
        else:
            if self._head is not None:
                node_for_removal = self._head.value
                self._head = self._head.next
                self._count -= 1
                return node_for_removal

    def remove_last(self):
        if self.is_empty:
            raise ValueError("Cannot remove items from an empty list!")
        else:
            if self._tail is not None:
                node_for_removal = self._tail.value
                self._tail = self._tail.prev
                self._count -= 1
                return node_for_removal

    def find(self, value):
        if self.is_empty:
            return None
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return current
                current = current.next
            return None

    def values(self):
        values_tuple = ()
        if not self.is_empty:
            current = self._head
            while current is not None:
                values_tuple += (current.value,)
                current = current.next

        return values_tuple

    def _insert_before_head(self, value):
        node = LinkedListNode(value)
        if self.is_empty:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

        self._count += 1

    def _insert_after_tail(self, value):
        node = LinkedListNode(value)
        if self.is_empty:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node

        self._count += 1

