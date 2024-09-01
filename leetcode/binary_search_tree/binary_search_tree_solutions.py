import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data_structures import Node_BST, BinarySearchTree
from typing import Optional


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

    def find_kth_smallest(self, k: int) -> Optional[int]:
        """
        Find the k-th smallest element in the binary search tree (BST).

        This method provides two approaches to find the k-th smallest element:
        1. **Iterative Method**: Uses an in-order traversal with a stack to find the k-th smallest element.
        2. **Recursive Method**: Uses a recursive in-order traversal to track the k-th smallest element.

        Args:
            k (int): The k-th position to find in the sorted order of the BST values.

        Returns:
            Optional[int]: The value of the k-th smallest element if it exists, 
                        otherwise None if k is out of bounds.
        """
        # METHOD 1: ITERATIVE APPROACH
        stack = []
        left_side_leftmost = self.bst.root
        # Traverse to the leftmost node starting from the root, pushing nodes onto the stack.
        while left_side_leftmost:
            stack.append(left_side_leftmost)
            left_side_leftmost = left_side_leftmost.left
        # Process nodes in in-order sequence.
        while len(stack) > 0:
            popped = stack.pop()  # Pop the top node from the stack.
            k -= 1  # Decrement the kth smallest counter
            if k == 0:
                # Return the value if the k-th smallest node is found.
                return popped.value
            # If the popped node has a right child, traverse its leftmost path.
            if popped.right is not None:
                right_side_leftmost = popped.right
                while right_side_leftmost:
                    stack.append(right_side_leftmost)
                    right_side_leftmost = right_side_leftmost.left
        # If k is still greater than zero, the k-th element does not exist.
        if k > 0:
            return None

        # # METHOD 2: RECURSIVE APPROACH
        # nodes_visited = 0  # Counter to keep track of nodes visited during in-order traversal.

        # def __find_kth_smallest(current_node: Node_BST[int], k: int) -> Optional[Node_BST[int]]:
        #     """
        #     Recursive helper function to find the k-th smallest element using in-order traversal.

        #     Args:
        #         current_node (Node_BST[int]): The current node being traversed.
        #         k (int): The target k-th position to find.

        #     Returns:
        #         Optional[Node_BST[int]]: The k-th smallest node if found, otherwise None.
        #     """
        #     # Use nonlocal to modify the `nodes_visited` variable from the outer `find_kth_smallest` function,
        #     # allowing us to update the count of visited nodes.
        #     # This refers specifically to the nearest parent scope where `nodes_visited` is defined,
        #     # not to a global scope variable, ensuring it affects the intended variable in the outer function.
        #     nonlocal nodes_visited
        #     # Base case: if the current node is None, return None to stop recursion in this path.
        #     if current_node is None:
        #         return None
        #     # Recursively search the left subtree.
        #     result = __find_kth_smallest(current_node.left, k)
        #     if result is not None:
        #         # If the left subtree found the k-th node, propagate it up without further traversal.
        #         return result
        #     # Increment the visited nodes count.
        #     nodes_visited += 1
        #     # If the k-th node is the current node, return it.
        #     if nodes_visited == k:
        #         return current_node
        #     # Recursively search the right subtree.
        #     result = __find_kth_smallest(current_node.right, k)
        #     if result is not None:
        #         # If the right subtree found the k-th node, propagate it up.
        #         return result
        #     # Return None if the k-th node is not found in this path, ensuring recursion handles
        #     # cases where traversal ends without finding the k-th element.
        #     return None
        # # Call the recursive helper function starting from the root.
        # kth_smallest_node = __find_kth_smallest(self.bst.root, k)
        # # Return the value of the k-th smallest node if found. This serves as a safeguard to ensure that
        # # if the node was found during traversal, its value is returned correctly; otherwise, it returns None.
        # if kth_smallest_node:
        #     return kth_smallest_node.value
        # # Return None if the k-th smallest element does not exist.
        # # This serves as a safeguard ensuring that if the loop or recursion completes
        # # without finding the k-th element—such as when `k` is larger than the total number
        # # of nodes—the function returns a clear indication that the element is not present,
        # # rather than failing silently or causing unexpected behavior.
        # return None
