import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data_structures import Node_LL, LinkedList
from typing import Optional


class Solution:
    """
    A class that provides solutions for operations on a linked list.

    Attributes:
        linked_list (LinkedList[int]): The linked list to perform operations on.
    """

    def __init__(self) -> None:
        """
        Initialize the Solution with a new linked list instance for integers.
        """
        self.linked_list: LinkedList[int] = LinkedList(
        )  # Initialize as a LinkedList of int type.

    def bubble_sort(self) -> None:
        """
        Sorts the linked list using the bubble sort algorithm.

        The method iteratively compares adjacent nodes and swaps their values 
        if they are in the wrong order. It continues until the entire list 
        is sorted. Two different methods are shown, each achieving the same 
        sorting effect.
        """
        # # METHOD 1: Using runner and end pointers to sort the list
        # # Check if the list has fewer than two elements, in which case it is already sorted
        # if self.linked_list.length < 2:
        #     return
        # # Initialize pointers
        # runner = self.linked_list.head
        # end = self.linked_list.tail
        # # Outer loop to progressively move the sorted boundary
        # while end != self.linked_list.head:
        #     # Inner loop to compare adjacent nodes up to the sorted boundary
        #     while runner.next != end:
        #         temp = runner.next
        #         # Swap values if they are out of order
        #         if runner.value > temp.value:
        #             runner.value, temp.value = temp.value, runner.value
        #         runner = runner.next
        #     # Final swap if the last node is greater than the end node
        #     if runner.value > end.value:
        #         runner.value, end.value = end.value, runner.value
        #     # Move the sorted boundary back
        #     end = runner
        #     # Reset the runner to the start of the list for the next pass
        #     runner = self.linked_list.head

        # METHOD 2: Using a sorted boundary pointer to sort the list
        # Check if the list has fewer than two elements, in which case it is already sorted
        if self.linked_list.length < 2:
            return
        # Initialize the sorted boundary pointer
        sorted_until = None
        # Outer loop to progressively move the sorted boundary
        while sorted_until != self.linked_list.head:
            current = self.linked_list.head
            # Inner loop to compare adjacent nodes up to the sorted boundary
            while current.next != sorted_until:
                temp = current.next
                # Swap values if they are out of order
                if current.value > temp.value:
                    current.value, temp.value = temp.value, current.value
                current = current.next
            # Move the sorted boundary back
            sorted_until = current

    def selection_sort(self) -> None:
        """
        Sorts the linked list using the selection sort algorithm.

        The method iteratively selects the minimum element from the unsorted portion 
        of the list and swaps it with the first unsorted element. This process is 
        repeated until the entire list is sorted.
        """
        # Check if the list has fewer than two elements; if so, it is already sorted
        if self.linked_list.length < 2:
            return
        # Start with the first node in the linked list
        current = self.linked_list.head
        # Outer loop to iterate over each node as the starting point for finding the minimum
        while current:
            # Assume the current node is the minimum
            min_pointer = current
            # Runner pointer to traverse the remaining unsorted part of the list
            runner = current.next
            # Inner loop to find the minimum value node in the unsorted portion
            while runner:
                # Update the min_pointer if a smaller value is found
                if runner.value < min_pointer.value:
                    min_pointer = runner
                runner = runner.next
            # Swap the values of the current node and the found minimum node
            if min_pointer != current:
                min_pointer.value, current.value = current.value, min_pointer.value
            # Move to the next node in the list
            current = current.next
