class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if not self.key:
            self.key = key
        elif key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
        return self

    def inorder(self):
        ret = []
        cast = {
            int: ret.append,
            list: ret.extend,
        }

        if self.left:
            cast[type(l := self.left.inorder())](l)

        ret.append(self.key)

        if self.right:
            cast[type(r := self.right.inorder())](r)

        return ret


def tree_sort(arr):
    tree_root = TreeNode()
    for i in arr:
        tree_root.insert(i)

    return tree_root.inorder()
