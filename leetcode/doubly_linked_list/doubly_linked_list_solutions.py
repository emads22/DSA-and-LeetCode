import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))


from typing import Optional
from data_structures import Node, DoublyLinkedList


class Solution:
    """
    A class that provides solutions for operations on a doubly linked list.

    Attributes:
        doubly_linked_list (DoublyLinkedList): The doubly linked list to perform operations on.
    """

    def __init__(self, doubly_linked_list: DoublyLinkedList):
        """
        Initialize the Solution with a doubly linked list.

        Args:
            doubly_linked_list (DoublyLinkedList): The doubly linked list to be manipulated.
        """
        self.doubly_linked_list = doubly_linked_list

    def swap_first_last(self) -> None:
        """
        Swap the values of the first and last nodes in the doubly linked list.

        Note:
            This method assumes the list contains at least two nodes. If the list has only one node,
            the method does nothing.
        """
        if self.doubly_linked_list.length > 1:
            # Temporarily store the value of the head node
            temp = self.doubly_linked_list.head.value
            # Assign the value of the tail node to the head node
            self.doubly_linked_list.head.value = self.doubly_linked_list.tail.value
            # Assign the stored head value to the tail node
            self.doubly_linked_list.tail.value = temp

    def reverse(self) -> None:
        """
        Reverse the order of the nodes in the doubly linked list.

        The method offers three different approaches to reverse the list:
        1. Using a dummy node.
        2. Without a dummy node.
        3. A concise version of the reversal algorithm.
        """

        # # METHOD 1: using a dummy node
        # dummy = Node(0)
        # dummy.next = runner = self.doubly_linked_list.head
        # while runner:
        #     # Temporarily store the next node
        #     temp = runner.next
        #     # Update the head node if the next node is None (i.e., at the end of the list)
        #     if temp is None:
        #         self.doubly_linked_list.head = runner
        #     # Reverse the next and prev pointers of the current node
        #     runner.next = runner.prev
        #     runner.prev = temp
        #     runner = temp
        # # Set the tail to the original head node (now the last node)
        # self.doubly_linked_list.tail = dummy.next
        # dummy.next = None

        # METHOD 2: without dummy node
        runner = self.doubly_linked_list.head
        while runner:
            # Temporarily store the next node
            temp = runner.next
            # Swap the next and prev pointers of the current node
            runner.next, runner.prev = runner.prev, runner.next
            runner = temp
        # Swap the head and tail references
        self.doubly_linked_list.head, self.doubly_linked_list.tail = self.doubly_linked_list.tail, self.doubly_linked_list.head

        # # METHOD 3: concise version
        # runner = self.doubly_linked_list.head
        # while runner:
        #     # Swap the next and prev pointers of the current node
        #     runner.next, runner.prev = runner.prev, runner.next
        #     # Move to the previous node (which is now the next node due to reversal)
        #     runner = runner.prev
        # # Swap the head and tail references
        # self.doubly_linked_list.head, self.doubly_linked_list.tail = self.doubly_linked_list.tail, self.doubly_linked_list.head

    def is_palindrome(self) -> bool:
        """
        Checks if the elements in the doubly linked list form a palindrome.

        A palindrome is a sequence that reads the same backward as forward. This method
        includes two approaches to determine if the list is a palindrome. Only the first
        approach is executed in the current implementation.

        Returns:
            bool: True if the doubly linked list is a palindrome, False otherwise.
        """

        # METHOD 1:
        # A single element or an empty list is considered a palindrome.
        if self.doubly_linked_list.length <= 1:
            return True
        # Initialize two pointers: one starting from head (beginning) and one from tail (end)
        forward = self.doubly_linked_list.head
        backward = self.doubly_linked_list.tail
        # Iterate through the list comparing values from the front and the back.
        while forward.value == backward.value:
            # If pointers meet or are adjacent, it indicates a palindrome.
            if forward == backward or forward.prev == backward:
                return True
            # Move forward pointer to the next node and backward pointer to the previous node.
            forward = forward.next
            backward = backward.prev
        # If a mismatch is found, the list is not a palindrome.
        return False

        # # METHOD 2:
        # if self.doubly_linked_list.length <= 1:
        #     # If the list has 0 or 1 element, it is trivially a palindrome.
        #     return True
        # # Initialize two pointers: one at the head (start) of the list and one at the tail (end).
        # forward = self.doubly_linked_list.head
        # backward = self.doubly_linked_list.tail
        # # Iterate through the first half of the list.
        # for _ in range(self.doubly_linked_list.length // 2):
        #     # Compare the value at the forward pointer with the value at the backward pointer.
        #     if forward.value != backward.value:
        #         # If the values do not match, the list is not a palindrome.
        #         return False

        #     # Move forward pointer to the next node and backward pointer to the previous node.
        #     forward = forward.next
        #     backward = backward.prev
        # # If all compared values match, the list is a palindrome.
        # return True

    def swap_pairs(self) -> None:
        """
        Swap every two adjacent nodes in the doubly linked list. If the list has an odd number of nodes,
        the last node remains in place. This method modifies the linked list in place.

        Returns:
            None: The linked list is modified in place.
        """
        # If the list has fewer than 2 nodes, there's nothing to swap.
        if self.doubly_linked_list.length < 2:
            return
        # Start with the first node in the list.
        first = self.doubly_linked_list.head
        # Update the head to be the second node since the first pair will be swapped.
        self.doubly_linked_list.head = first.next
        while first and first.next:
            # `second` is the node next to `first` that will be swapped with `first`.
            second = first.next
            # Update `first`'s next to skip over `second`.
            first.next = second.next
            if second.next:
                # Update the previous pointer of the node after `second` to point back to `first`.
                second.next.prev = first
            # Link `second` back to the node before `first`.
            second.prev = first.prev
            if first.prev:
                # Link the previous node of `first` to `second`.
                first.prev.next = second
            # Link `first` as the next node after `second`.
            first.prev = second
            second.next = first
            # Move `first` to the next pair.
            first = first.next
