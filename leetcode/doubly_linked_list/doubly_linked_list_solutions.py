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
