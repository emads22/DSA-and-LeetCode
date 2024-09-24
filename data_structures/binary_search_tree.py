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

    def __repr__(self) -> str:
        """
        Return a concise string representation of the Binary Search Tree (BST).

        Returns:
            str: A string representation of the BST.
        """
        return f"BinarySearchTree(Root: {self.root})"

    def __str__(self) -> str:
        """
        Return a detailed formatted string representation of the Binary Search Tree (BST).

        Returns:
            str: A formatted string representing the BST.
        """
        # Convert the BST to a list format and include the root node in the string
        return f"""
*  {self._to_list(self.root)}

    . Root: {self.root}
"""

    def _to_list(self, node: Node_BST[ItemType]) -> list[ItemType]:
        """
        Convert the binary search tree (BST) to a list representation recursively.

        Args:
            node (Node_BST[ItemType]): The current node in the BST.

        Returns:
            List[ItemType]: A list containing all the values in the BST in pre-order traversal.
        """
        # Base case: if the current node is None, return an empty list
        if node is None:
            return []
        # Recursive case: add the current node's value, traverse the left subtree, then traverse the right subtree
        return [node.value] + self._to_list(node.left) + self._to_list(node.right)

    def display(self) -> None:
        """
        Print the string representation of the Binary Search Tree (BST) using the __str__ method.
        """
        print(str(self))

    def lookup(self, value: ItemType) -> Optional[Node_BST[ItemType]]:
        """
        Look up a specific value in the binary search tree and return the corresponding node.

        Args:
            value (ItemType): The value to search for in the tree.

        Returns:
            Optional[Node_BST[ItemType]]: The node containing the value if found, 
                                        or None if the value is not in the tree.
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
                # Return the node if the value is found
                return temp
        # Return None if the value is not found in the tree (also if the tree is empty)
        return None

    def r_lookup(self, value: ItemType) -> Optional[Node_BST[ItemType]]:
        """
        Recursively looks up a value in the binary search tree (BST).

        Args:
            value (ItemType): The value to search for in the BST.

        Returns:
            Optional[Node_BST[ItemType]]: The node containing the value if found, otherwise None.
        """

        def _r_lookup_(node: Optional[Node_BST[ItemType]], value: ItemType) -> Optional[Node_BST[ItemType]]:
            """
            Helper function to perform the recursive lookup.

            Args:
                node (Optional[Node_BST[ItemType]]): The current node in the traversal.
                value (ItemType): The value to search for.

            Returns:
                Optional[Node_BST[ItemType]]: The node containing the value if found, otherwise None.
            """
            # Base case: if the current node is None, the value is not found
            if node is None:
                return None
            # If the current node's value matches the search value, return the current node
            if value == node.value:
                return node
            # If the search value is less than the current node's value, search the left subtree
            if value < node.value:
                return _r_lookup_(node.left, value)
            # If the search value is greater than the current node's value, search the right subtree
            if value > node.value:
                return _r_lookup_(node.right, value)
        # Start the recursive lookup from the root node
        return _r_lookup_(self.root, value)

    def contains(self, value: ItemType) -> bool:
        """
        Check if the binary search tree contains a specific value.

        Args:
            value (ItemType): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        # Call the lookup method to check for the existence of the value
        exists = True if self.lookup(value) else False
        return exists

    def r_contains(self, value: ItemType) -> bool:
        """
        Public method to check if a value exists in the binary search tree using recursion.

        Args:
            value (ItemType): The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """

        def _r_contains_(current_node: Optional[Node_BST[ItemType]], value: ItemType) -> bool:
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
                return _r_contains_(current_node.left, value)
            if value > current_node.value:
                # If the target value is greater than the current node's value, search the right subtree
                return _r_contains_(current_node.right, value)

        # Start the recursive search from the root of the tree
        return _r_contains_(self.root, value)

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

    def DFS_pre_order(self) -> list[ItemType]:
        """
        Perform a depth-first search (DFS) pre-order traversal of the binary search tree.

        In pre-order traversal, the current node is processed before its child nodes.

        Returns:
            list[ItemType]: A list containing all values in the tree in pre-order traversal order.
        """
        output = []

        def traverse(current_node: Node_BST[ItemType]) -> None:
            """
            Recursive helper function to perform pre-order traversal.

            Args:
                current_node (Node_BST[ItemType]): The current node being traversed.
            """
            if current_node is None:
                return  # Base case: if current_node is None, do nothing
            # Process the current node's value
            output.append(current_node.value)
            # Traverse the left subtree if it exists
            if current_node.left is not None:
                traverse(current_node.left)
            # Traverse the right subtree if it exists
            if current_node.right is not None:
                traverse(current_node.right)

        # Start the traversal from the root node
        traverse(self.root)
        return output

    def DFS_in_order(self) -> list[ItemType]:
        """
        Perform a depth-first search (DFS) in-order traversal of the binary search tree.

        In in-order traversal, the left subtree is processed first, 
        followed by the current node, and then the right subtree.

        Returns:
            list[ItemType]: A list containing all values in the tree in in-order traversal order.
        """
        output = []

        def traverse(current_node: Node_BST[ItemType]) -> None:
            """
            Recursive helper function to perform in-order traversal.

            Args:
                current_node (Node_BST[ItemType]): The current node being traversed.
            """
            if current_node is None:
                return  # Base case: if current_node is None, do nothing
            # Traverse the left subtree if it exists
            if current_node.left is not None:
                traverse(current_node.left)
            # Process the current node's value
            output.append(current_node.value)
            # Traverse the right subtree if it exists
            if current_node.right is not None:
                traverse(current_node.right)

        # Start the traversal from the root node
        traverse(self.root)
        return output

    def DFS_post_order(self) -> list[ItemType]:
        """
        Perform a depth-first search (DFS) post-order traversal of the binary search tree.

        In post-order traversal, the left and right subtrees are processed before the current node.

        Returns:
            list[ItemType]: A list containing all values in the tree in post-order traversal order.
        """
        output = []

        def traverse(current_node: Node_BST[ItemType]) -> None:
            """
            Recursive helper function to perform post-order traversal.

            Args:
                current_node (Node_BST[ItemType]): The current node being traversed.
            """
            if current_node is None:
                return  # Base case: if current_node is None, do nothing
            # Traverse the left subtree if it exists
            if current_node.left is not None:
                traverse(current_node.left)
            # Traverse the right subtree if it exists
            if current_node.right is not None:
                traverse(current_node.right)
            # Process the current node's value
            output.append(current_node.value)

        # Start the traversal from the root node
        traverse(self.root)
        return output

    def BFS(self) -> list[ItemType]:
        """
        Perform a breadth-first search (BFS) traversal of the binary search tree.

        In BFS, nodes are processed level by level, starting from the root and moving 
        to each level's child nodes from left to right.

        Returns:
            list[ItemType]: A list containing all values in the tree in BFS order.
        """
        # Initialize an empty queue to hold nodes to be processed and an output list to store the values.
        queue = []
        output = []
        # Start the traversal from the root node.
        current_node = self.root
        # Add the root node to the queue if it exists.
        queue.append(current_node)
        # Continue until there are no more nodes to process in the queue.
        while len(queue) > 0:
            # Dequeue the first node from the queue.
            current_node = queue.pop(0)
            # Add the current node's value to the output list.
            output.append(current_node.value)
            # Enqueue the left child node if it exists.
            if current_node.left is not None:
                queue.append(current_node.left)
            # Enqueue the right child node if it exists.
            if current_node.right is not None:
                queue.append(current_node.right)
        # Return the list of values obtained from the BFS traversal.
        return output

    def height(self) -> int:
        """
        Calculate the height of the binary search tree.

        The height of a binary search tree is defined as the number of edges
        on the longest path from the root node to a leaf node. An empty tree 
        is considered to have a height of 0.

        This implementation uses Depth-First Search (DFS) to recursively 
        determine the height of the left and right subtrees and computes the 
        maximum height between them. The final height is calculated by adding 1 
        to account for the edge between the root and its children.

        Returns:
            int: The height of the tree. Returns 0 for an empty tree.
        """
        def _height(node: Optional[Node_BST[ItemType]]) -> int:
            """
            Helper function to compute the height of the subtree rooted at `node`.

            Args:
                node (Optional[Node_BST[ItemType]]): The current node in the tree.

            Returns:
                int: The height of the subtree rooted at `node`. Returns 0 for an empty subtree.
            """
            if node is None:
                return 0  # Base case: the height of an empty subtree is 0
            # Recursively find the height of the left and right subtrees
            left_height = _height(node.left)
            right_height = _height(node.right)
            # The height of the current node is the maximum of the heights of its subtrees plus 1
            return max(left_height, right_height) + 1

        # Start the height calculation from the root of the tree
        return _height(self.root)

        # if node is None:
        #     return -1  # Empty tree or end of recursion (leaf node's children)

        # # Recursively calculate the height of the left and right subtrees
        # left_height = self.height(node.left)
        # right_height = self.height(node.right)

        # # Return the greater of the two heights plus 1 for the current node
        # return max(left_height, right_height) + 1

    def depth(self, value: ItemType) -> int:
        """
        Find the depth of the node with the specified value in the binary search tree.

        Depth is defined as the number of edges from the root to the node with the given value.
        If the node with the specified value is not found, return -1.

        This method performs a Depth-First Search (DFS) to locate the node and calculate its depth.

        Args:
            value (ItemType): The value of the node whose depth is to be found.

        Returns:
            int: The depth of the node with the specified value, or -1 if the node is not found.
        """
        def _depth(node: Optional[Node_BST[ItemType]], value: ItemType, current_depth: int) -> int:
            """
            Helper method to perform recursive DFS and find the depth of the node with the specified value.

            Args:
                node (Optional[Node_BST[ItemType]]): The current node in the recursive search.
                value (ItemType): The value of the node to find.
                current_depth (int): The current depth level in the tree.

            Returns:
                int: The depth of the node with the specified value, or -1 if the node is not found.
            """
            # Base case: If the current node is None, the value is not found in this subtree.
            if node is None:
                return -1
            # If the current node contains the value, return the current depth.
            if node.value == value:
                return current_depth
            # Recursively search in the left subtree.
            left_depth = _depth(node.left, value, current_depth + 1)
            # If the value is found in the left subtree, return the depth.
            if left_depth != -1:
                return left_depth
            # Recursively search in the right subtree.
            right_depth = _depth(node.right, value, current_depth + 1)
            return right_depth

        # Start the search from the root of the tree with an initial depth of 0.
        return _depth(self.root, value, 0)

    def clear(self) -> None:
        """
        Clears the binary search tree by setting the root to None.

        This method effectively removes all nodes from the tree and resets
        the tree to an empty state. It is useful when you need to reuse the
        same BST object for different operations or tests without remnants
        of previous data.

        Example:
        >>> bst = BST()
        >>> bst.insert(5)
        >>> bst.clear()
        >>> bst.root
        None
        """
        # Set the root of the tree to None, effectively clearing the tree.
        self.root = None


def main():
    # Create a new binary search tree
    bst = BinarySearchTree[int]()

    # Test: Insert nodes into the BST
    print("\n==> Test: Insert nodes into the BST\n")
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print("\t. Inserting values:", values_to_insert)
    for value in values_to_insert:
        bst.insert(value)
    bst.display()
    print("-" * 80)

    # Test: Check for existing and non-existing values
    print("\n==> Test: Check for existing and non-existing values\n")
    search_values = [70, 40, 100]  # 100 is not in the tree
    for value in search_values:
        result = bst.contains(value)
        print(f"\t. Contains {value}: {result}")
    print()
    print("-" * 80)

    # Test: Recursively check for existing and non-existing values
    print("\n==> Test: Recursively check existing and non-existing values\n")
    for value in search_values:
        result = bst.r_contains(value)
        print(f"\t. Recursively contains {value}: {result}")
    print()
    print("-" * 80)

    # Test: Lookup for existing and non-existing values
    print("\n==> Test: Lookup for existing and non-existing values\n")
    search_values = [70, 40, 100]  # 100 is not in the tree
    for value in search_values:
        result = bst.lookup(value)
        print(f"\t. Lookup {value}: {result}")
    print()
    print("-" * 80)

    # Test: Recursively lookup for existing and non-existing values
    print("\n==> Test: Recursively lookup for existing and non-existing values\n")
    for value in search_values:
        result = bst.r_lookup(value)
        print(f"\t. Recursively lookup {value}: {result}")
    print()
    print("-" * 80)

    # Test: Delete nodes with no children (leaf nodes)
    print("\n==> Test: Delete leaf node 20:")
    bst.delete(20)
    bst.display()
    print("-" * 80)

    # Test: Delete nodes with one child
    print("\n==> Test: Delete node 30 (has one child):")
    bst.delete(30)
    bst.display()
    print("-" * 80)

    # Test: Delete nodes with two children
    print("\n==> Test: Delete node 50 (has two children):")
    bst.delete(50)
    bst.display()
    print("-" * 80)

    # Test: Insert recursively
    print("\n==> Test: Insert 25 recursively:")
    bst.r_insert(25)
    bst.display()
    print("-" * 80)

    # Test: Recursive delete
    # Re-insert nodes to prepare for recursive delete tests
    values_to_reinsert = [50, 30, 70, 20, 40, 60, 80]
    print(
        f"\n==> Re-insert node values {values_to_reinsert} for recursive delete tests")
    for value in values_to_reinsert:
        bst.r_insert(value)
    bst.display()
    print("-" * 80)

    # Test: Delete leaf node 20 using recursive delete
    print("\n==> Test: Recursive delete of leaf node 20:")
    bst.r_delete(20)
    bst.display()
    print("-" * 80)

    # Test: Delete node with one child (30) using recursive delete
    print("\n==> Test: Recursive delete of node 30 (has one child):")
    bst.r_delete(30)
    bst.display()
    print("-" * 80)

    # Test: Delete node with two children (50) using recursive delete
    print("\n==> Test: Recursive delete of node 50 (has two children):")
    bst.r_delete(50)
    bst.display()
    print("-" * 80)

    # Test: Traversal methods
    print("\n==> Test: Traversal methods:")
    in_order = bst.DFS_in_order()
    # In-order traversal
    print(f"\n\t. In-order traversal:\t{in_order}\n")
    pre_order = bst.DFS_pre_order()
    # Pre-order traversal
    print(f"\t. Pre-order traversal:\t{pre_order}\n")
    # Post-order traversal
    post_order = bst.DFS_post_order()
    print(f"\t. Post-order traversal:\t{post_order}\n")
    print("-" * 80)

    # Test: Tree height
    print("\n==> Test: Tree height")
    height = bst.height()
    print(f"\n\t. Height of the tree: {height}\n")
    print("-" * 80)

    # Test: Depth of nodes
    print("\n==> Test: Depth of nodes\n")
    depth_values = [25, 40, 60, 100]  # 100 is not in the tree
    for value in depth_values:
        depth_result = bst.depth(value)
        print(f"\t. Depth of node {value}: {depth_result}")
    print()
    print("-" * 80)

    # Test: Clear the BST
    print("\n==> Test: Clear the BST")
    bst.clear()
    bst.display()
    print("-" * 80)


if __name__ == "__main__":
    main()
