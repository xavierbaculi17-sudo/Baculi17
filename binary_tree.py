r"""Assessment 3.3 - Binary Tree for the last name BACULI.

The letters are inserted level by level, from left to right:

Level 0:          B
                /   \
Level 1:       A     C
              / \   /
Level 2:     U   L I
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(letters):
    """Build a binary tree by filling each level from left to right."""
    if not letters:
        return None
    root = Node(letters[0])
    queue = deque([root])
    i = 1
    while i < len(letters):
        parent = queue.popleft()
        parent.left = Node(letters[i])
        queue.append(parent.left)
        i += 1
        if i < len(letters):
            parent.right = Node(letters[i])
            queue.append(parent.right)
            i += 1
    return root


def bfs(root):
    """Breadth-First Search: visit the tree level by level using a queue."""
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs(node, order=None):
    """Depth-First Search (pre-order): node, then left subtree, then right subtree."""
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.value)
    dfs(node.left, order)
    dfs(node.right, order)
    return order


if __name__ == "__main__":
    last_name = "BACULI"
    root = build_tree(list(last_name))
    print("Binary Tree for:", last_name)
    print("BFS:", " - ".join(bfs(root)))
    print("DFS:", " - ".join(dfs(root)))
