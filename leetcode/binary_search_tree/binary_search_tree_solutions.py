import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import Optional
from data_structures import Node_BST, BinarySearchTree


class Solution:
    """
    A class that provides solutions for operations on a binary search tree.

    Attributes:
        bst (BinarySearchTree[int]): The binary search tree to perform operations on.
    """

    def __init__(self) -> None:
        """
        Initialize the Solution with a new binary search tree instance.
        """
        # Specifying int as the type for the BST
        self.bst = BinarySearchTree[int]()

    def sorted_list_to_bst(self, sorted_nums: list[int]) -> None:
        """
        Convert a sorted list of integers into a balanced binary search tree (BST).

        Args:
            sorted_nums (list[int]): A sorted list of integers to be converted into a BST.
        """
        # Convert the sorted list to a BST and set it as the root of the binary search tree
        self.bst.root = self.__sorted_list_to_bst(
            sorted_nums, 0, len(sorted_nums) - 1)

    def __sorted_list_to_bst(self, sorted_nums: list[int], left: int, right: int) -> Optional[Node_BST[int]]:
        """
        Recursively converts a sorted list into a balanced binary search tree (BST).

        Args:
            sorted_nums (list[int]): A sorted list of integers to be converted into a BST.
            left (int): The left boundary of the current sublist.
            right (int): The right boundary of the current sublist.

        Returns:
            Optional[Node_BST[int]]: The root node of the subtree created from the sorted list.
        """
        if left > right:
            return None  # Base case: If the left index exceeds the right, return None
        # Find the middle index to make the current root
        middle_idx = (left + right) // 2
        # Create a new node with the middle value
        current_node = Node_BST(sorted_nums[middle_idx])
        # Recursively construct the left and right subtrees
        current_node.left = self.__sorted_list_to_bst(
            sorted_nums, left, middle_idx - 1)
        current_node.right = self.__sorted_list_to_bst(
            sorted_nums, middle_idx + 1, right)
        # Return the current node as the root of this subtree.
        return current_node

    def invert(self) -> None:
        """
        Public method to invert the binary search tree.

        Inverts the binary search tree such that all left children are swapped with right children, effectively mirroring the tree.
        """
        # METHOD 1 (returning value):
        # Start the recursive inversion from the root of the tree and update the root reference
        self.bst.root = self.__invert_tree(self.bst.root)

        # # METHOD 2 (in place):
        # # Start the recursive inversion from the root of the tree directly
        # without assignement since the root does not change
        # but the explicit assignment makes it clearer
        # self.__invert_tree(self.bst.root)

    def __invert_tree(self, node: Optional[Node_BST[int]]) -> Optional[Node_BST[int]]:
        """
        Recursively inverts the binary search tree.

        Args:
            node (Optional[Node_BST[int]]): The current node to be inverted.

        Returns:
            Optional[Node_BST[int]]: The root node of the inverted subtree or None if the node is None.
        """
        # METHOD 1 (returning value):
        if node is None:
            # Base case: if the current node is None, return None
            return None
        # Swap the left and right children of the current node
        temp_node = node.left
        node.left = node.right
        node.right = temp_node
        # Recursively invert the left and right subtrees
        node.left = self.__invert_tree(node.left)
        node.right = self.__invert_tree(node.right)
        # Return the current node as the new root of this inverted subtree
        return node

        # # METHOD 2 (in place):
        # if node is None:
        #     # Base case: if the current node is None, there is nothing to invert
        #     return
        # # Swap the left and right children of the current node
        # temp_node = node.left
        # node.left = node.right
        # node.right = temp_node
        # # Recursively invert the left and right subtrees
        # self.__invert_tree(node.left)
        # self.__invert_tree(node.right)

    def is_valid_bst(self) -> bool:
        """
        Check if the binary search tree (BST) is valid.

        A valid BST is defined as a tree where for every node, 
        all values in its left subtree are less than the node's value, 
        and all values in its right subtree are greater.

        This function provides two methods to verify if the tree is a valid BST:
        - **Method 1**: Compares the in-order traversal of the BST with its sorted version.
        - **Method 2**: Checks each adjacent element in the in-order traversal to ensure 
        that the current value is less than the next value.

        Returns:
            bool: True if the BST is valid, False otherwise.
        """
        # # METHOD 1: Check if the in-order traversal is sorted.
        # # An in-order traversal of a BST should produce a sorted list.
        # bst_list = self.bst.DFS_in_order()  # O(n) time complexity for the in-order traversal.
        # # Check if the BST list matches its sorted version.
        # # This comparison takes O(n), but the sorting operation takes O(n log n),
        # # making this method less efficient overall.
        # if bst_list == sorted(bst_list):  # Sorting takes O(n log n) time.
        #     return True

        # METHOD 2: Check if each element is less than the next in the in-order traversal.
        # O(n) time complexity for the in-order traversal.
        bst_list = self.bst.DFS_in_order()
        # Iterate through the list and check if each value is less than the next.
        # O(n) time complexity for the loop.
        for i in range(len(bst_list) - 1):
            if bst_list[i] >= bst_list[i + 1]:
                # Return False if any element is not less than the next, indicating an invalid BST.
                return False
        # Return True if all checks pass, confirming a valid BST.
        return True

    def find_kth_smallest_iterative(self, k: int) -> Optional[int]:
        """
        Find the k-th smallest element in the binary search tree (BST).

        Args:
            k (int): The k-th position to find in the sorted order of the BST values.

        Returns:
            Optional[int]: The value of the k-th smallest element if it exists, 
                        otherwise None if k is out of bounds.
        """
        # METHOD 1: Iterative In-Order Traversal
        stack = []
        left_side_leftmost = self.bst.root
        # Traverse to the leftmost node, pushing nodes onto the stack.
        while left_side_leftmost:
            stack.append(left_side_leftmost)
            left_side_leftmost = left_side_leftmost.left
        # Process nodes in in-order sequence.
        while stack:
            popped = stack.pop()  # Pop the next node in order.
            k -= 1  # Decrement k, moving closer to the k-th smallest.
            if k == 0:
                return popped.value  # Return the k-th smallest element.
            # Traverse the leftmost path of the right subtree if it exists.
            if popped.right:
                right_side_leftmost = popped.right
                while right_side_leftmost:
                    stack.append(right_side_leftmost)
                    right_side_leftmost = right_side_leftmost.left
        # Return None if k is out of bounds.
        if k > 0:
            return None

        # # METHOD 2: Integrated Iterative In-Order Traversal
        # stack = []
        # current_node = self.root
        # # Traverse the tree using in-order traversal.
        # while stack or current_node:
        #     # Push left nodes onto the stack.
        #     while current_node:
        #         stack.append(current_node)
        #         current_node = current_node.left
        #     popped_node = stack.pop()  # Pop the next node in order.
        #     k -= 1
        #     if k == 0:
        #         return popped_node.value  # Return the k-th smallest element.
        #     current_node = popped_node.right  # Move to the right subtree.
        # # Return None if the k-th element does not exist.
        # return None

    def find_kth_smallest_recursive(self, k: int) -> Optional[int]:
        """
        Find the k-th smallest element in the binary search tree (BST).

        Args:
            k (int): The k-th position to find in the sorted order of the BST values.

        Returns:
            Optional[int]: The value of the k-th smallest element if it exists, 
                        otherwise None if k is out of bounds.
        """

        # Counter to keep track of the number of nodes visited during the in-order traversal.
        n_visited_nodes = 0

        def _kth_smallest_element(current_node: Node_BST[int], k: int) -> Optional[int]:
            """
            Recursive helper function to find the k-th smallest element using in-order traversal.

            This function performs an in-order traversal (left, root, right) of the BST, 
            counting the nodes visited to identify the k-th smallest node.

            Args:
                current_node (Node_BST[int]): The current node being traversed in the BST.
                k (int): The target k-th position to find in the sorted order of BST nodes.

            Returns:
                Optional[int]: The value of the k-th smallest node if found, otherwise None.
            """
            # Use nonlocal to modify the `n_visited_nodes` variable from the outer scope,
            # allowing the recursive function to update the count of nodes visited.
            # `nonlocal` refers specifically to the nearest parent scope where `n_visited_nodes`
            # is defined, ensuring it updates the correct variable and not a global or local one.
            nonlocal n_visited_nodes

            # Base case: if the current node is None, return None to indicate the end of this path.
            if current_node is None:
                return None

            # Recursively search the left subtree to process nodes in ascending order.
            result = _kth_smallest_element(current_node.left, k)
            if result is not None:
                # If the left subtree returns a result, propagate it up as the k-th element has been found.
                return result

            # Increment the count of visited nodes since we're now processing the current node.
            n_visited_nodes += 1
            # Check if the current node is the k-th node by comparing the count to k.
            if n_visited_nodes == k:
                # Return the value of the current node if it matches the k-th position.
                return current_node.value

            # Recursively search the right subtree if the k-th node hasn't been found yet.
            result = _kth_smallest_element(current_node.right, k)
            if result is not None:
                # If the right subtree returns a result, propagate it up as the k-th element has been found.
                return result

            # Return None if the k-th node is not found in this path, ensuring all branches handle
            # the case where traversal completes without identifying the k-th smallest element.
            return None

        # Call the recursive helper function starting from the root node of the BST.
        return _kth_smallest_element(self.bst.root, k)


def main():
    # Instantiate the Solution class
    solution = Solution()

    # Test cases for sorted_list_to_bst
    print("\n==> Testing sorted_list_to_bst:\n")
    sorted_lists = {
        "Edge case: empty list": [],                   # Edge case: empty list
        # Edge case: single element
        "Edge case: single element": [1],
        # Simple case: three elements
        "Simple case: three elements": [1, 2, 3],
        # Simple case: five elements
        "Simple case: five elements": [1, 2, 3, 4, 5],
        # Case with seven elements
        "Case with seven elements": [1, 2, 3, 4, 5, 6, 7]
    }

    for case, sorted_list in sorted_lists.items():
        solution.bst.clear()
        solution.sorted_list_to_bst(sorted_list)
        print(f"\t. {case} {sorted_list} --> {solution.bst.DFS_in_order()}")
    print()
    print("-" * 80)

    print("\n==> Testing invert:\n")
    # Reuse some test cases for inverting the BST
    for case, sorted_list in sorted_lists.items():
        solution.bst.clear()
        print(f"\t. {case} {sorted_list}:")
        solution.sorted_list_to_bst(sorted_list)
        print(
            f"\t\t. Original BST In-order traversal: {solution.bst.DFS_in_order()}")
        solution.invert()
        print(
            f"\t\t. Inverted BST In-order traversal: {solution.bst.DFS_in_order()}\n")
    print("-" * 80)

    print("\n==> Testing is_valid_bst:\n")
    valid_bsts = {
        "Edge case: empty tree": [],                   # Edge case: empty tree
        # Edge case: single element
        "Edge case: single element": [1],
        # Simple case: three elements forming a valid BST
        "Simple case: three elements forming a valid BST": [1, 2, 3],
        # Simple case: three elements forming a valid BST after inversion
        "Simple case: three elements forming a valid BST after inversion": [3, 2, 1]
    }

    for case, valid_bst in valid_bsts.items():
        solution.bst.clear()
        print(f"\t. {case} {valid_bst}:")
        solution.sorted_list_to_bst(valid_bst)
        print(f"\t\t. BST In-order traversal: {solution.bst.DFS_in_order()}")
        print(f"\t\t. Is valid BST: {solution.is_valid_bst()}\n")
    print("-" * 80)

    print("\n==> Testing find_kth_smallest_iterative:")
    ks = [1, 2, 3, 4]  # Various k values to test
    for case, sorted_list in sorted_lists.items():
        solution.bst.clear()
        print(f"\n\t. {case} {sorted_list}:")
        solution.sorted_list_to_bst(sorted_list)
        for k in ks:
            print(f"\t\t. K={k}, Kth smallest element is: {
                  solution.find_kth_smallest_iterative(k)}")
    print()
    print("-" * 80)

    print("\n==> Testing find_kth_smallest_recursive:")
    for case, sorted_list in sorted_lists.items():
        solution.bst.clear()
        print(f"\n\t. {case} {sorted_list}:")
        solution.sorted_list_to_bst(sorted_list)
        for k in ks:
            print(f"\t\t. K={k}, Kth smallest element is: {
                  solution.find_kth_smallest_recursive(k)}")
    print()
    print("-" * 80)


if __name__ == "__main__":
    main()
