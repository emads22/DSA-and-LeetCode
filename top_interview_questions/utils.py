import random
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """Initialize a tree node with a value and optional left and right children."""
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None

    def __str__(self) -> str:
        """Return a string representation of the tree."""
        return str(self._list) if hasattr(self, "_list") else "None"

    def build_from_list(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Build a binary tree from a list representation."""
        if not values:
            return None
        # Save the list representation for display
        self._list = values
        # Create the root of the tree
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while i < len(values):
            # Get the next node from the queue
            current = queue.pop(0)
            # Insert the left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Insert the right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

