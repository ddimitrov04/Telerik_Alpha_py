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

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail
    
    @tail.setter
    def tail(self, value):
        self._tail = value

    def add_first(self, value):
        new_node = LinkedListNode(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:  
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._count += 1


    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def insert_after(self, node, value):
        if node is None:
            raise ValueError('Node is empty!')
        
        new_node = LinkedListNode(value)
        if node == self.tail:
            self._insert_after_tail(value)
        else:
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            self._count += 1  

    def insert_before(self, node, value):
        if node is None:
            raise ValueError('Node is none!')

        new_node = LinkedListNode(value)

        if node == self.head:
            self._insert_before_head(value)
        else:
            new_node.prev = node.prev
            new_node.next = node
            new_node.prev.next = new_node
            node.prev = new_node

        self._count += 1


    def remove_first(self):
        if self.head is None:
            raise ValueError('Node is empty!')
        
        removed_el = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._count -= 1

        return removed_el

    def remove_last(self):
        if self.head is None:
            raise ValueError('Node is empty')
        removed_el = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._count -= 1
        return removed_el


    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def values(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return tuple(result)


    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._count += 1


    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        if self.tail is None:
            raise ValueError('Node is empty!')
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1
