class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_successor(self):
        successor = None
        if self.right:
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.parent.left == self:
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def find_min(self):
        successor = self
        while successor.left:
            successor = successor.left
        return successor

    def delete_successor(self):
        if not (self.right or self.left):
            if self.parent and self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.left or self.right:
            if self.left:
                if self.parent and self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.parent and self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, value='a value'):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.left:
                self._put(key, value, current.left)
            else:
                current.left = Node(key, value, parent=current)
        else:
            if current.right:
                self._put(key, value, current.right)
            else:
                current.right = Node(key, value, parent=current)

    def contains(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return True
            else:
                return False
        else:
            return False

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self._delete(node)
                self.size = self.size - 1
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

    def _delete(self, node):
        if not node.left and not node.right:
            if node.parent and node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left and node.right:
            successor = node.find_successor()
            successor.delete_successor()
            node.key, node.value = successor.key, successor.value
        else:
            if node.left:
                if node.parent and node.parent.left == node:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.parent and node.parent.right == node:
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.key, node.value = node.left.key, node.left.value
                    node.left, node.right = node.left.left, node.left.right
                    if node.left:
                        node.left.parent = node
                    if node.right:
                        node.right.parent = node
            else:
                if node.parent and node.parent.left == node:
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.parent and node.parent.right == node:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.key, node.value = node.right.key, node.right.value
                    node.left, node.right = node.right.left, node.right.right
                    if node.left:
                        node.left.parent = node
                    if node.right:
                        node.right.parent = node


