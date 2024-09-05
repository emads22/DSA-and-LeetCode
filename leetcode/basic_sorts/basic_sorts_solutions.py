import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data_structures import LinkedList  


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

    def insertion_sort(self) -> None:
        """
        Sorts the linked list using the insertion sort algorithm.

        The method builds a sorted portion of the list by inserting each element 
        from the unsorted portion into its correct position in the sorted portion.
        Two different methods are provided for accomplishing this.
        """
        # METHOD 1: Sorting by inserting elements from the unsorted part into the sorted part
        if self.linked_list.length < 2:
            return
        # The first node is considered sorted initially
        sorted = self.linked_list.head
        unsorted = sorted.next
        sorted.next = None  # The sorted list starts with a single element
        # Loop over the unsorted portion
        while unsorted:
            before = None
            current = unsorted
            unsorted = unsorted.next  # Move the unsorted pointer forward
            # Find the correct insertion position in the sorted portion
            while sorted and sorted.value < current.value:
                before = sorted
                sorted = sorted.next
            # Insert the current node in the correct position
            if before:
                before.next = current
            else:
                # Insert at the beginning if it's the smallest element
                self.linked_list.head = current
            current.next = sorted  # Link the current node with the sorted part
            # Reset the sorted pointer back to the head for the next pass
            sorted = self.linked_list.head
        # After sorting, update the tail pointer of the list
        while sorted.next:
            sorted = sorted.next
        # Update the tail to point to the last element of the sorted list
        self.linked_list.tail = sorted

        # # METHOD 2: Another approach to inserting elements in the correct sorted order
        # if self.linked_list.length < 2:
        #     return
        # # Start with the first node being the sorted part
        # sorted = self.linked_list.head
        # unsorted = sorted.next
        # sorted.next = None  # Sorted list initially contains only one element
        # # Loop through each node in the unsorted list
        # while unsorted:
        #     current = unsorted
        #     unsorted = unsorted.next  # Advance the unsorted pointer
        #     # Insert the current node at the correct position in the sorted portion
        #     if current.value < sorted.value:
        #         # If the current value is smaller than the head of the sorted list, insert at the head
        #         current.next = sorted
        #         self.linked_list.head = current
        #     else:
        #         # Find the correct position in the sorted portion
        #         while sorted.next and current.value > sorted.next.value:
        #             sorted = sorted.next
        #         # Insert the current node at the correct position
        #         current.next = sorted.next
        #         sorted.next = current
        #     # Reset the sorted pointer back to the head for the next pass
        #     sorted = self.linked_list.head
        # # After sorting, update the tail pointer
        # while sorted.next:
        #     sorted = sorted.next
        # self.linked_list.tail = sorted  # Update the tail pointer to the last element of the sorted list


def main() -> None:
    test_cases = [
        [4, 3, 5, 1, 2],
        [10, 5, 2, 8, 7],
        [5, 5, 5, 5, 5],
        [1],
        [],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]

    sol = Solution()

    # Test bubble sort
    print("\n\n=========={ Testing bubble_sort on LinkedList }==========\n\n")
    for case in test_cases:
        sol.linked_list = LinkedList()
        sol.linked_list.from_list(case)
        print(f". Original: {sol.linked_list.to_list()}")
        sol.bubble_sort()
        print(f". Sorted: {sol.linked_list.to_list()}")
        print("-" * 40)

    # Test selection sort
    print("\n\n=========={ Testing selection_sort on LinkedList }==========\n\n")
    for case in test_cases:
        sol.linked_list = LinkedList()
        sol.linked_list.from_list(case)
        print(f". Original: {sol.linked_list.to_list()}")
        sol.selection_sort()
        print(f". Sorted: {sol.linked_list.to_list()}")
        print("-" * 40)

    # Test insertion sort
    print("\n\n=========={ Testing insertion_sort on LinkedList }==========\n\n")
    for case in test_cases:
        sol.linked_list = LinkedList()
        sol.linked_list.from_list(case)
        print(f". Original: {sol.linked_list.to_list()}")
        sol.insertion_sort()
        print(f". Sorted: {sol.linked_list.to_list()}")
        print("-" * 40)


if __name__ == "__main__":
    main()
