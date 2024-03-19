from src.bst_node import BSTNode


class BinarySearchTree:
    def __init__(self):
        self._root: BSTNode = None

    @property
    def root(self):
        return self._root

    @property
    def height(self):
        raise NotImplementedError()

    def dfs_inorder(self):

        def _inorder_(node, list):
            if node is None:
                return

            _inorder_(node.left, list)
            list.append(node.value)
            _inorder_(node.right, list)

        list = []
        _inorder_(self._root, list)
        return list

    def dfs_preorder(self):
        def _preorder_(node, list):
            if node is None:
                return

            list.append(node.value)
            _preorder_(node.left, list)
            _preorder_(node.right, list)

        list = []
        _preorder_(self._root, list)
        return list

    def dfs_postorder(self):
        def _postorder_(node, list):
            if node is None:
                return

            _postorder_(node.left, list)
            _postorder_(node.right, list)
            list.append(node.value)

        list = []
        _postorder_(self._root, list)
        return list

    def bfs(self):
        raise NotImplementedError()

    def search(self, value):
        raise NotImplementedError()

    def insert(self, value):
        def _insert_recursive(node, new_value):
            if node is None:
                return BSTNode(new_value)

            if new_value < node.value:
                node.left = _insert_recursive(node.left, new_value)
            else:
                node.right = _insert_recursive(node.right, new_value)

            return node

        self._root = _insert_recursive(self._root, value)
    def remove(self, value):
        raise NotImplementedError()


tree = BinarySearchTree()
tree.insert(7)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(8)
tree.insert(9)
print(tree.dfs_inorder())
print(tree.dfs_postorder())