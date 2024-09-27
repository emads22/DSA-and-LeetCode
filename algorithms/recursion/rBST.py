from typing import Optional


class Node:
    """
    A class representing a node in a binary search tree.       
    """

    def __init__(self, value) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left: 'Node' = None
        self.right: 'Node' = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return f"Node({self.value})"


class rBST:
    """
    A recursive implementation of a binary search tree (rBST).
    """

    def __init__(self) -> None:
        """
        Initialize an empty binary search tree.
        """
        self.root: Node = None

    def __repr__(self) -> str:
        """
        Return a concise string representation of the Binary Search Tree (rBST).

        Returns:
            str: A string representation of the rBST.
        """
        return f"rBST(Root: {self.root})"

    def __str__(self) -> str:
        """
        Return a detailed formatted string representation of the Binary Search Tree (rBST).

        Returns:
            str: A formatted string representing the rBST.
        """
        # Convert the rBST to a list format and include the root node in the string
        return f"\n\t*  {self._to_list(self.root)}\t\t- Root: {self.root}\n"

    def _to_list(self, node: Node) -> list:
        """
        Convert the binary search tree (rBST) to a list representation recursively.

        Args:
            node (Node): The current node in the rBST.

        Returns:
            List: A list containing all the values in the rBST in pre-order traversal.
        """
        # Base case: if the current node is None, return an empty list
        if node is None:
            return []
        # Recursive case: add the current node's value, traverse the left subtree, then traverse the right subtree
        return [node.value] + self._to_list(node.left) + self._to_list(node.right)

    def display(self) -> None:
        """
        Print the string representation of the Binary Search Tree (rBST) using the __str__ method.
        """
        print(str(self))

    def clear(self) -> None:
        """
        Clears the binary search tree by setting the root to None.

        This method effectively removes all nodes from the tree and resets
        the tree to an empty state. It is useful when you need to reuse the
        same rBST object for different operations or tests without remnants
        of previous data.
        """
        # Set the root of the tree to None, effectively clearing the tree.
        self.root = None

    def r_lookup(self, value) -> Optional[Node]:
        """
        Recursively looks up a value in the binary search tree (rBST).

        Args:
            value: The value to search for in the rBST.

        Returns:
            Optional[Node]: The node containing the value if found, otherwise None.
        """

        def _r_lookup_(node: Optional[Node], value) -> Optional[Node]:
            """
            Helper function to perform the recursive lookup.

            Args:
                node (Optional[Node]): The current node in the traversal.
                value: The value to search for.

            Returns:
                Optional[Node]: The node containing the value if found, otherwise None.
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

    def r_contains(self, value) -> bool:
        """
        Public method to check if a value exists in the binary search tree using recursion.

        Args:
            value : The value to search for in the tree.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """

        def _r_contains_(current_node: Optional[Node], value) -> bool:
            """
            Recursively checks if a value exists in the binary search tree.

            Args:
                current_node (Optional[Node]): The current node being checked.
                value : The value to search for in the tree.

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

    def r_insert(self, value) -> None:
        """
        Public method to insert a value into the binary search tree using recursion.

        Args:
            value : The value to be inserted into the tree.
        """
        if self.root is None:
            # If the tree is empty, create a new root node with the given value
            self.root = Node(value)
            return

        def _r_insert_(current_node: Optional[Node], value) -> Node:
            """
            Recursively inserts a value into the binary search tree.

            Args:
                current_node (Optional[Node]): The current node being checked.
                value : The value to be inserted into the tree.

            Returns:
                Node: The updated node after insertion.
            """
            if current_node is None:
                # If the current node is None, create a new node with the given value
                return Node(value)
            if value < current_node.value:
                # If the value is less than the current node's value, insert into the left subtree
                current_node.left = _r_insert_(current_node.left, value)
            elif value > current_node.value:
                # If the value is greater than the current node's value, insert into the right subtree
                current_node.right = _r_insert_(current_node.right, value)
            # Return the current node after insertion
            return current_node

        # Recursively insert the value starting from the root node
        self.root = _r_insert_(self.root, value)
        # Alternatively: `_r_insert_(self.root, value)` directly
        # without assignement since the root does not change

    def _subtree_min_value(self, current_node: Node):
        """
        Finds the minimum value in a subtree.

        Args:
            current_node (Node): The root node of the subtree.

        Returns:
         The minimum value found in the subtree.
        """
        # Traverse to the leftmost node to find the minimum value
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def r_delete(self, value) -> None:
        """
        Public method to delete a value from the binary search tree using recursion.

        Args:
            value : The value to be deleted from the tree.
        """
        def _r_delete_(current_node: Optional[Node], value) -> Optional[Node]:
            """
            Recursively deletes a value from the binary search tree.

            Args:
                current_node (Optional[Node]): The current node being checked.
                value : The value to be deleted from the tree.

            Returns:
                Optional[Node]: The updated node after deletion.
            """
            if current_node is None:
                # If the current node is None, the value is not found in the tree
                return None
            if value < current_node.value:
                # If the value to be deleted is less than the current node's value,
                # continue searching in the left subtree
                current_node.left = _r_delete_(current_node.left, value)
            elif value > current_node.value:
                # If the value to be deleted is greater than the current node's value,
                # continue searching in the right subtree
                current_node.right = _r_delete_(current_node.right, value)
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
                    min_value_right = self._subtree_min_value(
                        current_node.right)
                    # Replace the value of the current node with the minimum value found
                    current_node.value = min_value_right
                    # Delete the duplicate node with the minimum value from the right subtree
                    current_node.right = _r_delete_(
                        current_node.right, min_value_right)
            # Return the updated current node after deletion
            return current_node

        # Start the recursive deletion process from the root node
        self.root = _r_delete_(self.root, value)

    def DFS_pre_order(self) -> list:
        """
        Perform a depth-first search (DFS) pre-order traversal of the binary search tree.

        In pre-order traversal, the current node is processed before its child nodes.

        Returns:
            list: A list containing all values in the tree in pre-order traversal order.
        """
        output = []

        def traverse(current_node: Node) -> None:
            """
            Recursive helper function to perform pre-order traversal.

            Args:
                current_node (Node): The current node being traversed.
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

    def DFS_in_order(self) -> list:
        """
        Perform a depth-first search (DFS) in-order traversal of the binary search tree.

        In in-order traversal, the left subtree is processed first, 
        followed by the current node, and then the right subtree.

        Returns:
            list: A list containing all values in the tree in in-order traversal order.
        """
        output = []

        def traverse(current_node: Node) -> None:
            """
            Recursive helper function to perform in-order traversal.

            Args:
                current_node (Node): The current node being traversed.
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

    def DFS_post_order(self) -> list:
        """
        Perform a depth-first search (DFS) post-order traversal of the binary search tree.

        In post-order traversal, the left and right subtrees are processed before the current node.

        Returns:
            list: A list containing all values in the tree in post-order traversal order.
        """
        output = []

        def traverse(current_node: Node) -> None:
            """
            Recursive helper function to perform post-order traversal.

            Args:
                current_node (Node): The current node being traversed.
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

    def BFS(self) -> list:
        """
        Perform a breadth-first search (BFS) traversal of the binary search tree.

        In BFS, nodes are processed level by level, starting from the root and moving 
        to each level's child nodes from left to right.

        Returns:
            list: A list containing all values in the tree in BFS order.
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
        is considered to have a height of -1.

        This implementation uses Depth-First Search (DFS) to recursively 
        determine the height of the left and right subtrees and computes the 
        maximum height between them. The final height is calculated by adding 1 
        to account for the edge between the root and its children.

        Returns:
            int: The height of the tree. Returns 0 for an empty tree.
        """
        def _height(node: Optional[Node]) -> int:
            """
            Helper function to compute the height of the subtree rooted at `node`.

            Args:
                node (Optional[Node]): The current node in the tree.

            Returns:
                int: The height of the subtree rooted at `node`. Returns 0 for an empty subtree.
            """
            if node is None:
                # Base case: Empty tree or end of recursion (leaf node's children)
                return -1
            # Recursively find the height of the left and right subtrees
            left_height = _height(node.left)
            right_height = _height(node.right)
            # The height of the current node is the maximum of the heights of its subtrees plus 1
            return max(left_height, right_height) + 1

        # Start the height calculation from the root of the tree
        return _height(self.root)

    def depth(self, value) -> int:
        """
        Find the depth of the node with the specified value in the binary search tree.

        Depth is defined as the number of edges from the root to the node with the given value.
        If the node with the specified value is not found, return -1.

        This method performs a Depth-First Search (DFS) to locate the node and calculate its depth.

        Args:
            value : The value of the node whose depth is to be found.

        Returns:
            int: The depth of the node with the specified value, or -1 if the node is not found.
        """
        def _depth(node: Optional[Node], value, current_depth: int) -> int:
            """
            Helper method to perform recursive DFS and find the depth of the node with the specified value.

            Args:
                node (Optional[Node]): The current node in the recursive search.
                value : The value of the node to find.
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


def main():
    # Create a new recursive binary search tree
    r_bst = rBST()

    # Test: Recursively insert nodes into the rBST
    print("\n==> Test: Insert nodes into the BST\n")
    values_to_insert = [15, 35, 55, 25, 45, 65, 85]
    print(f"\t. Inserting values {tuple(values_to_insert)}:\n")
    for value in values_to_insert:
        r_bst.r_insert(value)
    r_bst.display()
    print("-" * 60)

    search_values = [55, 45, 100]  # 100 is not in the tree

    # Test: Recursively check for existing and non-existing values
    print("\n==> Test: Recursively check existing and non-existing values\n")
    for value in search_values:
        result = r_bst.r_contains(value)
        print(f"\t. Recursively contains {value}: {result}")
    print()
    print("-" * 60)

    # Test: Recursively lookup for existing and non-existing values
    print("\n==> Test: Recursively lookup for existing and non-existing values\n")
    for value in search_values:
        result = r_bst.r_lookup(value)
        print(f"\t. Recursively lookup {value}: {result}")
    print()
    print("-" * 60)

    # Test: Recursive delete
    # Test: Delete leaf node 15 using recursive delete
    print("\n==> Test: Recursive delete of leaf node 15:")
    r_bst.r_delete(15)
    r_bst.display()
    print("-" * 60)

    # Test: Delete node with one child (25) using recursive delete
    print("\n==> Test: Recursive delete of node 25 (has one child):")
    r_bst.r_delete(25)
    r_bst.display()
    print("-" * 60)

    # Test: Delete node with two children (55) using recursive delete
    print("\n==> Test: Recursive delete of node 55 (has two children):")
    r_bst.r_delete(55)
    r_bst.display()
    print("-" * 60)

    # Test: Traversal methods
    print("\n==> Test: Traversal methods:")
    in_order = r_bst.DFS_in_order()
    # In-order traversal
    print(f"\n\t. In-order traversal:\t{in_order}\n")
    pre_order = r_bst.DFS_pre_order()
    # Pre-order traversal
    print(f"\t. Pre-order traversal:\t{pre_order}\n")
    # Post-order traversal
    post_order = r_bst.DFS_post_order()
    print(f"\t. Post-order traversal:\t{post_order}\n")
    print("-" * 60)

    # Test: Tree height
    print("\n==> Test: Tree height")
    height = r_bst.height()
    print(f"\n\t. Height of the tree: {height}\n")
    print("-" * 60)

    # Test: Depth of nodes
    print("\n==> Test: Depth of nodes\n")
    depth_values = [85, 45, 65, 100]  # 100 is not in the tree
    for value in depth_values:
        depth_result = r_bst.depth(value)
        print(f"\t. Depth of node {value}: {depth_result}")
    print()
    print("-" * 60)

    # Test: Clear the rBST
    print("\n==> Test: Clear the rBST")
    r_bst.clear()
    r_bst.display()
    print("-" * 60)


if __name__ == "__main__":
    main()
