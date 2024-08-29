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
