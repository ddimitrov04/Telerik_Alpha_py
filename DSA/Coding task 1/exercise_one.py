class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None


n, k = map(int, input().split())
names = input().split()

nodes = {name: Node(name) for name in names}

for i in range(1, n):
    prev_node = nodes[names[i - 1]]
    curr_node = nodes[names[i]]
    prev_node.next = curr_node
    curr_node.prev = prev_node

head, tail = nodes[names[0]], nodes[names[-1]]


for _ in range(k):
    left_name, right_name = input().split()
    left_node, right_node = nodes[left_name], nodes[right_name]

    if left_node.prev:  # If it's not the head
        left_node.prev.next = left_node.next
    if left_node.next:  # If it's not the tail
        left_node.next.prev = left_node.prev

    if left_node is head:
        head = left_node.next
    if left_node is tail:
        tail = left_node.prev

    if right_node.prev:
        right_node.prev.next = left_node
    else:
        head = left_node

    left_node.prev = right_node.prev
    left_node.next = right_node
    right_node.prev = left_node

result = []
current = head
while current:
    result.append(current.name)
    current = current.next

print(' '.join(result))
