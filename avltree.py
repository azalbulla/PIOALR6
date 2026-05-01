class AVLNode:
    __slots__ = ['key', 'left', 'right', 'height']

    def __init__(self, key):
        self.key, self.left, self.right, self.height = key, None, None, 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        if node: node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y);
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update_height(x);
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root: return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)
        balance = self.get_balance(root)
        if balance > 1:
            if key > root.left.key: root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1:
            if key < root.right.key: root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def delete(self, root, key):
        if not root: return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        self.update_height(root)
        balance = self.get_balance(root)
        if balance > 1:
            if self.get_balance(root.left) < 0: root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1:
            if self.get_balance(root.right) > 0: root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def _min_node(self, node):
        while node.left: node = node.left
        return node

    def search(self, root, key):
        if not root or root.key == key: return root
        return self.search(root.left, key) if key < root.key else self.search(root.right, key)

    def inorder(self, root):
        res = []
        if root:
            res.extend(self.inorder(root.left))
            res.append(root.key)
            res.extend(self.inorder(root.right))
        return res

    def print_tree(self, root, level=0, prefix="Root: "):
        if root:
            print(" " * (level * 4) + prefix + f"{root.key} (H={root.height})")
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ") if root.left else print(
                    " " * ((level + 1) * 4) + "L--- None")
                self.print_tree(root.right, level + 1, "R--- ") if root.right else print(
                    " " * ((level + 1) * 4) + "R--- None")
