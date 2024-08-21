from typing import TypeVar, Generic, Optional


# Type variable to represent the type of the item in the BST nodes
ItemType = TypeVar('ItemType')


class Node_BST(Generic[ItemType]):
    """
    A class representing a node in a binary search tree.

    Attributes:
        value (ItemType): The value stored in the node.
        left (Optional[Node_BST[ItemType]]): The left child node.
        right (Optional[Node_BST[ItemType]]): The right child node.        
    """

    def __init__(self, value: ItemType) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (ItemType): The value to be stored in the node.
        """
        self.value = value
        self.left: Optional[Node_BST[ItemType]] = None
        self.right: Optional[Node_BST[ItemType]] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return f"Node({self.value})"


class BinarySearchTree(Generic[ItemType]):
    """
    A class representing a binary search tree.

    Attributes:
        root (Optional[Node_BST[ItemType]]): The root node of the binary search tree.
    """

    def __init__(self) -> None:
        """
        Initialize an empty binary search tree.
        """
        self.root: Optional[Node_BST[ItemType]] = None

    def _list_repr_(self, node):
        """
        Convert the binary search tree (BST) to a list representation recursively.

        Args:
            node (Node_BST[ItemType]): The current node in the BST.

        Returns:
            List[ItemType]: A list containing all the values in the BST in in-order traversal.
        """
        # Base case: if the current node is None, return an empty list
        if node is None:
            return []
        # Recursive case: add the current node's value, traverse the left subtree, then traverse the right subtree
        return [node.value] + self._list_repr_(node.left) + self._list_repr_(node.right)

    def display(self) -> None:
        """
        Print the string representation of the binary search tree.
        """
        display = f"""

*  {self._list_repr_(self.root)}

    . Root: {self.root}
"""
        print(display)

    def insert(self, value: ItemType) -> bool:
        """
        Insert a value into the binary search tree.

        Args:
            value (ItemType): The value to be inserted into the tree.

        Returns:
            bool: True if the value was inserted successfully, False if the value already exists in the tree.
        """
        new_node = Node_BST(value)
        if self.root is None:
            # If the tree is empty, set the new node as the root
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value < temp.value:
                # Traverse to left subtree if the value is less than the current node's value
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif value > temp.value:
                # Traverse to right subtree if the value is greater than the current node's value
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                # Return False if the value already exists in the tree
                return False

    def contains(self, value: ItemType) -> bool:
        """
        Check if the binary search tree contains a specific value.

        Args:
            value (ItemType): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        temp = self.root
        while temp:
            if value < temp.value:
                # Traverse to left subtree if the value is less than the current node's value
                temp = temp.left
            elif value > temp.value:
                # Traverse to right subtree if the value is greater than the current node's value
                temp = temp.right
            else:
                # Return True if the value is found
                return True
        # Return False if the value is not found in the tree (also if the tree is empty)
        return False
