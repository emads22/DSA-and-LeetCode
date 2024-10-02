from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        """Initialize a tree node with a value and optional left and right children."""
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None

    def __str__(self) -> str:
        """Return a string representation of the tree."""
        return str(self._list) if hasattr(self, "_list") else "None"

    def build_from_list(self, values: List[Optional[int]]) -> None:
        """Build a binary tree from a list representation."""
        if not values:
            return
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


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        """Initialize a list node with a value and optional next element."""
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        return str(self._list) if hasattr(self, "_list") else "None"

        # # Alternatively
        # if self.head is None:
        #     return "None"
        # current = self.head
        # result = []
        # while current:
        #     result.append(str(current.val))
        #     current = current.next
        # return " -> ".join(result)

    def build_from_list(self, values: List[Optional[int]]) -> None:
        """Build a linked list from a list representation."""
        if not values:
            return
        # Save the list representation for display
        self._list = values
        # Create the root of the tree
        self.head = ListNode(values[0])  # Initialize head with the first value
        current = self.head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next

    def to_list(self) -> List[Optional[int]]:
        """Convert the linked list back to a Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.val)  # Append the value of the current node
            current = current.next      # Move to the next node
        return result

    def get_node(self, value: int) -> Optional[ListNode]:
        """
        Retrieve the node with the specified value.
        """
        current = self.head
        while current:
            if current.val == value:
                return current
            current = current.next  # Move to the next node
        return None
