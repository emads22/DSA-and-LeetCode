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

    def _to_list(self, node: Node_BST[ItemType]) -> list[ItemType]:
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
        return [node.value] + self._to_list(node.left) + self._to_list(node.right)

    def display(self) -> None:
        """
        Print the string representation of the binary search tree.
        """
        display = f"""

*  {self._to_list(self.root)}

    . Root: {self.root}
"""
        print(display)

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

    def r_contains(self, value: ItemType) -> bool:
        """
        Public method to check if a value exists in the binary search tree using recursion.

        Args:
            value (ItemType): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        # Start the recursive search from the root of the tree
        return self._r_contains_(self.root, value)

    def _r_contains_(self, current_node: Optional[Node_BST[ItemType]], value: ItemType) -> bool:
        """
        Recursively checks if a value exists in the binary search tree.

        Args:
            current_node (Optional[Node_BST[ItemType]]): The current node being checked.
            value (ItemType): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        if current_node is None:
            # If the current node is None, the value is not in the tree
            return False
        if value == current_node.value:
            # If the current node's value matches the target value, return True
            return True
        if value < current_node.value:
            # If the target value is less than the current node's value, search the left subtree
            return self._r_contains_(current_node.left, value)
        if value > current_node.value:
            # If the target value is greater than the current node's value, search the right subtree
            return self._r_contains_(current_node.right, value)

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

    def r_insert(self, value: ItemType) -> None:
        """
        Public method to insert a value into the binary search tree using recursion.

        Args:
            value (ItemType): The value to be inserted into the tree.
        """
        if self.root is None:
            # If the tree is empty, create a new root node with the given value
            self.root = Node_BST(value)
            return
        # Recursively insert the value starting from the root node
        self.root = self._r_insert_(self.root, value)
        # Alternatively: `self._r_insert_(self.root, value)` directly
        # without assignement since the root does not change

    def _r_insert_(self, current_node: Optional[Node_BST[ItemType]], value: ItemType) -> Node_BST[ItemType]:
        """
        Recursively inserts a value into the binary search tree.

        Args:
            current_node (Optional[Node_BST[ItemType]]): The current node being checked.
            value (ItemType): The value to be inserted into the tree.

        Returns:
            Node_BST[ItemType]: The updated node after insertion.
        """
        if current_node is None:
            # If the current node is None, create a new node with the given value
            return Node_BST(value)
        if value < current_node.value:
            # If the value is less than the current node's value, insert into the left subtree
            current_node.left = self._r_insert_(current_node.left, value)
        elif value > current_node.value:
            # If the value is greater than the current node's value, insert into the right subtree
            current_node.right = self._r_insert_(current_node.right, value)
        # Return the current node after insertion
        return current_node

    def delete(self, value: ItemType) -> Optional[Node_BST[ItemType]]:
        """
        Iteratively deletes a node with the specified value from the binary search tree.

        Args:
            value (ItemType): The value of the node to delete.

        Returns:
            Optional[Node_BST[ItemType]]: The deleted node if found, otherwise None.
        """
        if self.root is None:
            # If the tree is empty, there is nothing to delete
            return None

        current = self.root
        parent = None
        to_delete = None

        # Traverse the tree to find the node to delete
        while True:
            if value < current.value:
                # If the value is less than the current node's value, move left
                if current.left:
                    parent = current
                    current = current.left
                else:
                    # If there's no left child, the value isn't in the tree
                    return None
            elif value > current.value:
                # If the value is greater than the current node's value, move right
                if current.right:
                    parent = current
                    current = current.right
                else:
                    # If there's no right child, the value isn't in the tree
                    return None
            else:
                # Node with the matching value is found
                to_delete = current

                # Case 1: The node is a leaf node (no children)
                if current.left is None and current.right is None:
                    if parent:
                        # If the node has a parent, disconnect it from the parent
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        # If the node is the root, set the root to None
                        self.root = None

                # Case 2: The node has only one child (left child)
                elif current.right is None:
                    if parent:
                        # Connect the parent to the left child of the current node
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    else:
                        # If the root is being deleted, update the root
                        self.root = self.root.left

                # Case 3: The node has only one child (right child)
                elif current.left is None:
                    if parent:
                        # Connect the parent to the right child of the current node
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    else:
                        # If the root is being deleted, update the root
                        self.root = self.root.right

                # Case 4: The node has two children
                else:
                    # Find the minimum value in the right subtree (in-order successor)
                    temp_parent = current
                    temp = current.right
                    while temp.left:
                        temp_parent = temp
                        temp = temp.left

                    # Replace the value of the current node with the minimum value found
                    current.value = temp.value

                    # Remove the minimum node by linking the parent's left to the right child of temp
                    temp_parent.left = temp.right  # Works whether temp.right is None or not

                # Return the deleted node
                return to_delete

    def r_delete(self, value: ItemType) -> None:
        """
        Public method to delete a value from the binary search tree using recursion.

        Args:
            value (ItemType): The value to be deleted from the tree.
        """
        # Start the recursive deletion process from the root node
        self.root = self._r_delete_(self.root, value)

    def _r_delete_(self, current_node: Optional[Node_BST[ItemType]], value: ItemType) -> Optional[Node_BST[ItemType]]:
        """
        Recursively deletes a value from the binary search tree.

        Args:
            current_node (Optional[Node_BST[ItemType]]): The current node being checked.
            value (ItemType): The value to be deleted from the tree.

        Returns:
            Optional[Node_BST[ItemType]]: The updated node after deletion.
        """
        if current_node is None:
            # If the current node is None, the value is not found in the tree
            return None
        if value < current_node.value:
            # If the value to be deleted is less than the current node's value,
            # continue searching in the left subtree
            current_node.left = self._r_delete_(current_node.left, value)
        elif value > current_node.value:
            # If the value to be deleted is greater than the current node's value,
            # continue searching in the right subtree
            current_node.right = self._r_delete_(current_node.right, value)
        else:  # The value to be deleted is found
            # Case 1: The node is a leaf node (no children)
            if current_node.left is None and current_node.right is None:
                current_node = None  # Remove the node by setting it to None
            # Case 2: The node has only one child (left child)
            elif current_node.right is None:
                current_node = current_node.left  # Replace the node with its left child
            # Case 3: The node has only one child (right child)
            elif current_node.left is None:
                current_node = current_node.right  # Replace the node with its right child
            # Case 4: The node has two children
            else:
                # Find the minimum value in the right subtree
                min_value_right = self._subtree_min_value(current_node.right)
                # Replace the value of the current node with the minimum value found
                current_node.value = min_value_right
                # Delete the duplicate node with the minimum value from the right subtree
                current_node.right = self._r_delete_(
                    current_node.right, min_value_right)
        # Return the updated current node after deletion
        return current_node

    def _subtree_min_value(self, current_node: Node_BST[ItemType]) -> ItemType:
        """
        Finds the minimum value in a subtree.

        Args:
            current_node (Node_BST[ItemType]): The root node of the subtree.

        Returns:
            ItemType: The minimum value found in the subtree.
        """
        # Traverse to the leftmost node to find the minimum value
        while current_node.left:
            current_node = current_node.left
        return current_node.value

