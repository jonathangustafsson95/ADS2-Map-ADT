class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = 0

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
                    self.right.parent = self.parent
                else:
                    self.parent.right = self.left
                    self.left.parent = self.parent
            else:
                if self.parent and self.parent.left == self:
                    self.parent.left = self.right
                    self.right.parent = self.parent
                else:
                    self.parent.right = self.right
                    self.right.parent = self.parent


class BalancedBSTMap:
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
                self._update_balance(current.left)
        else:
            if current.right:
                self._put(key, value, current.right)
            else:
                current.right = Node(key, value, parent=current)
                self._update_balance(current.right)

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

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def _update_after_delete(self, node):
        node.balance = self.height(node.left) - self.height(node.right)
        if abs(node.balance) == 2:
            self.rebalance(node)

    def _delete(self, node):
        if not node.left and not node.right:
            if node.parent and node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            self._update_after_delete(node.parent)
        elif node.left and node.right:
            successor = node.find_successor()
            successor.delete_successor()
            node.key, node.value = successor.key, successor.value
            self._update_after_delete(successor.parent)
        elif node.left or node.right:
            if node.left:
                if node.parent and node.parent.left == node:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                    self._update_after_delete(node.parent)
                elif node.parent and node.parent.right == node:
                    node.left.parent = node.parent
                    node.parent.right = node.left
                    self._update_after_delete(node.parent)
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
                    self._update_after_delete(node.parent)
                elif node.parent and node.parent.right == node:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                    self._update_after_delete(node.parent)
                else:
                    node.key, node.value = node.right.key, node.right.value
                    node.left, node.right = node.right.left, node.right.right
                    if node.left:
                        node.left.parent = node
                    if node.right:
                        node.right.parent = node

    def _update_balance(self, node):
        if abs(node.balance) > 1:
            self.rebalance(node)
            return

        if node.parent:
            if node.parent.left == node:
                node.parent.balance += 1
            elif node.parent.right == node:
                node.parent.balance -= 1

            if node.parent.balance != 0:
                self._update_balance(node.parent)

    def rebalance(self, node):
        if node.balance < 0:
            if node.right.balance > 0:
                self._rotate_right(node.right)
                self._rotate_left(node)
            else:
                self._rotate_left(node)
        elif node.balance > 0:
            if node.left.balance < 0:
                self._rotate_left(node.left)
                self._rotate_right(node)
            else:
                self._rotate_right(node)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left

        if new_root.left:
            new_root.left.parent = node
        new_root.parent = node.parent
        if self.root == node:
            self.root = new_root
        else:
            if node.parent and node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        node.balance = self.height(node.left) - self.height(node.right)
        new_root.balance = self.height(node.left) - self.height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right

        if new_root.right:
            new_root.right.parent = node
        new_root.parent = node.parent
        if self.root == node:
            self.root = new_root
        else:
            if node.parent and node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        new_root.right = node
        node.parent = new_root
        node.balance = self.height(node.left) - self.height(node.right)
        new_root.balance = self.height(node.left) - self.height(node.right)

