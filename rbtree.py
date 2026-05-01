class RBNode:
    __slots__ = ['key', 'left', 'right', 'parent', 'color']
    def __init__(self, key, color=1): # 1=RED, 0=BLACK
        self.key, self.left, self.right, self.parent, self.color = key, None, None, None, color

class RBTree:
    def __init__(self):
        self.NIL = RBNode(0, color=0)
        self.root = self.NIL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y

    def insert(self, key):
        node = RBNode(key); node.left = node.right = self.NIL
        y, x = None, self.root
        while x != self.NIL:
            y = x
            x = x.left if node.key < x.key else x.right
        node.parent = y
        if not y: self.root = node
        elif node.key < y.key: y.left = node
        else: y.right = node
        if not node.parent: node.color = 0; return
        if not node.parent.parent: return
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = k.parent.color = 0; k.parent.parent.color = 1; k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent; self.rotate_right(k)
                    k.parent.color = 0; k.parent.parent.color = 1; self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = k.parent.color = 0; k.parent.parent.color = 1; k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent; self.rotate_left(k)
                    k.parent.color = 0; k.parent.parent.color = 1; self.rotate_right(k.parent.parent)
            if k == self.root: break
        self.root.color = 0

    def inorder(self):
        def _res(node):
            if node == self.NIL: return []
            color = "RED" if node.color == 1 else "BLACK"
            return _res(node.left) + [f"{node.key}({color})"] + _res(node.right)
        return _res(self.root)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None: node = self.root
        if node != self.NIL:
            c = "RED" if node.color == 1 else "BLACK"
            print(" " * (level * 4) + prefix + f"{node.key} ({c})")
            if node.left != self.NIL or node.right != self.NIL:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")
