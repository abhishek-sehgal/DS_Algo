#%%
import random

#%%
# Basic Node Class
class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.data)


# Basic Tree Class
class Tree:
    root = Node(None)

    def insert(self, data):
        if self.root.data is None:
            self.root = Node(data=data)
            return

        current = self.root
        while current:
            if data < current.data:
                if not current.left:
                    current.left = Node(data)
                    return
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(data)
                    return
                else:
                    current = current.right


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node, end=", ")
        in_order(node.right)


def post_order(node):
    if node is not None:
        in_order(node.left)
        in_order(node.right)
        print(node, end=", ")


def pre_order(node):
    if node is not None:
        print(node, end=", ")
        in_order(node.left)
        in_order(node.right)


#%%
print("Randomly Initialized Vector")
vec = [random.randint(0, 100) for _ in range(20)]
print(vec)

tree = Tree()

for v in vec:
    tree.insert(v)

print("In order traversal and how tree sort is done")
in_order(tree.root)
print("\nPre order traversal")
pre_order(tree.root)
print("\nPost Order Traversal")
post_order(tree.root)
# %%
