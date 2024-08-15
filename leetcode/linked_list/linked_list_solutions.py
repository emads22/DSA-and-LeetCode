import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data_structures import Node, LinkedList
from typing import Optional

class Solution:
    """
    A class that provides solutions for operations on a linked list.

    Attributes:
        linked_list (LinkedList): The linked list to perform operations on.
    """

    def __init__(self, linked_list: LinkedList):
        """
        Initialize the Solution with a linked list.

        Args:
            linked_list (LinkedList): The linked list to be manipulated.
        """
        self.linked_list = linked_list

    def find_middle_node(self) -> Optional[Node]:
        """
        Finds the middle node of the linked list.

        This method uses a two-pointer technique to find the middle node in a linked list. 
        The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
        When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

        Returns:
            Optional[Node]: The middle node of the linked list, or the first node of the second half 
                            if the list has an even number of nodes.
        """
        slow = fast = self.linked_list.head  # Initialize both pointers to the head of the list
        while fast and fast.next:       # Loop until fast reaches the end or has no next node
            slow = slow.next            # Move slow pointer one step
            fast = fast.next.next       # Move fast pointer two steps
        # slow now points to the middle node or the first node of the second half
        return slow

    def has_loop(self) -> bool:
        """
        Detects if there is a loop (cycle) in the linked list.

        This method uses Floyd's cycle-finding algorithm (the "tortoise and hare" algorithm) 
        to detect the presence of a loop in the linked list. If the slow and fast pointers 
        meet at some point, it indicates a loop.

        Returns:
            bool: True if a loop is detected, otherwise False.
        """
        slow = fast = self.linked_list.head  # Initialize both pointers to the head of the list

        while fast and fast.next:       # Loop until fast reaches the end or has no next node
            slow = slow.next            # Move slow pointer one step
            fast = fast.next.next       # Move fast pointer two steps

            if fast == slow:
                return True

        return False

    @staticmethod
    def find_kth_from_end(linked_list: LinkedList, k: int) -> Optional[Node]:
        """
        Finds the k-th node from the end of the linked list.

        This function uses a two-pointer technique to locate the k-th node from the end without
        calculating the length of the list. The fast pointer moves k steps ahead, and then both 
        slow and fast pointers move together until the fast pointer reaches the end of the list.

        Args:
            linked_list (LinkedList): The linked list to search within.
            k (int): The position from the end to find the node.

        Returns:
            Optional[Node]: The k-th node from the end of the list, or None if the position is out of bounds.
        """
        slow = fast = linked_list.head

        if k <= 0:                     # Handle the case where k is 0 or negative
            return None

        for _ in range(k):
            # Also triggers if linked_list is empty (head is None)
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

    def partition_list(self, x: int) -> None:
        """
        Partition the linked list such that all nodes with values less than x come before nodes 
        with values greater than or equal to x. The relative order of nodes in each partition is preserved.

        Args:
            x (int): The partitioning value.

        Returns:
            None: This function modifies the linked list in place and does not return a value.
        """
        if self.linked_list.head is None:
            # If the linked list is empty, there's nothing to partition.
            return
        # Initialize two dummy nodes to start the less and greater partitions to simplify the process of adding nodes to each partition.
        less = dummy1 = Node(0)
        greater = dummy2 = Node(0)
        # Start with the head of the original linked list.
        current = self.linked_list.head
        # Traverse the linked list, partitioning the nodes into less and greater lists.
        while current:
            if current.value < x:
                # If the current node's value is less than x, add it to the less partition.
                less.next = current
                less = less.next
            else:
                # If the current node's value is greater than or equal to x, add it to the greater partition.
                greater.next = current
                greater = greater.next
            # Move to the next node in the original list.
            current = current.next
        # Terminate the greater list to avoid circular references or dangling pointers.
        greater.next = None
        # Connect the less list to the greater list.
        less.next = dummy2.next
        # Update the head of the linked list to the start of the less list.
        self.linked_list.head = dummy1.next

    def remove_duplicates(self) -> None:
        """
        Removes all duplicate values from the linked list.

        This method modifies the linked list in-place to remove any duplicate values, preserving 
        the relative order of the nodes. The implementation provides two methods: one using a set 
        (with O(n) time complexity) and another without any additional data structures 
        (with O(n^2) time complexity).

        The first method uses a set to track seen values, ensuring that duplicates are removed 
        efficiently in O(n) time. The second method (commented out) uses nested loops to remove 
        duplicates without extra space, but at the cost of O(n^2) time complexity.

        Args:
            None

        Returns:
            None
        """

        # METHOD 1: Using a set for O(n) time complexity and O(n) space complexity
        values = set()  # Set to track unique values seen in the list
        before = None  # Pointer to the previous node
        current = self.linked_list.head  # Pointer to the current node

        while current:
            if current.value in values:
                # If the current value is already in the set, it's a duplicate.
                # Remove the current node by skipping it.
                before.next = current.next
                # Adjust the length of the linked list if length tracking is implemented
                self.linked_list.length -= 1
            else:
                # If the current value is not in the set, add it and move the 'before' pointer.
                values.add(current.value)
                before = current
            current = current.next  # Move to the next node

        # # METHOD 2: Without using a set, with O(n^2) time complexity and O(1) space complexity
        # current = self.linked_list.head
        # while current:
        #     before = current
        #     temp = current.next
        #     while temp:
        #         if temp.value == current.value:
        #             # If a duplicate is found, remove it by skipping the node.
        #             before.next = temp.next
        #             self.linked_list.length -= 1  # Adjust the length of the linked list
        #         else:
        #             # If no duplicate, move the 'before' pointer to the temp node.
        #             before = temp
        #         temp = temp.next  # Move to the next node in the inner loop
        #     current = current.next  # Move to the next node in the outer loop

    def binary_to_decimal(self) -> Optional[int]:
        """
        Converts a binary number represented as a linked list to its decimal equivalent.

        This method traverses the linked list from the head to the end, calculating the decimal 
        value of the binary number by multiplying each digit by 2 raised to the power of its 
        position (starting from the right, which is the least significant bit).

        Returns:
            Optional[int]: The decimal equivalent of the binary number or None if the linked list is empty.
        """

        # METHOD 1
        if self.linked_list.empty():  # Check if the linked list is empty
            return None

        current = self.linked_list.head  # Start from the head of the linked list
        decimal_value = 0  # Initialize the decimal value

        # Traverse the list and calculate the decimal value
        for idx in range(self.linked_list.length - 1, -1, -1):
            decimal_value += current.value * \
                (2 ** idx)  # Convert binary to decimal
            current = current.next  # Move to the next node

        return decimal_value  # Return the calculated decimal value

        # # METHOD 2
        # if self.linked_list.empty():  # Check if the linked list is empty
        #     return None

        # current = self.linked_list.head  # Start from the head of the linked list
        # decimal_value = 0  # Initialize the decimal value

        # # Traverse the list and calculate the decimal value
        # while current:
        #     #  shift the current accumulated value left by one bit (equivalent to multiplying by 2) and then add the current bit(node)'s value (either 0 or 1).
        #     decimal_value = decimal_value * 2 + current.value  # Convert binary to decimal
        #     current = current.next  # Move to the next node

        # return decimal_value  # Return the calculated decimal value

    def reverse_between(self, start_index: int, end_index: int) -> None:
        """
        Reverse the nodes of the linked list from start_index to end_index in one pass and in-place.

        This method modifies the linked list in-place by reversing the nodes between the specified indices.
        If the linked list is empty or has only one node, no changes are made.

        Args:
            start_index (int): The starting index (inclusive) of the sublist to reverse.
            end_index (int): The ending index (inclusive) of the sublist to reverse.

        Returns:
            None: The linked list is modified in place.
        """
        # If the linked list is empty or has only one node, nothing to reverse.
        if self.linked_list.length < 2:
            return
        # Dummy node to simplify the reversal process.
        dummy = Node(0)
        # Pointer to the node before the start_index.
        previous = None
        # Start from the head of the linked list.
        current = self.linked_list.head
        for idx in range(end_index + 1):
            if idx < start_index:
                # Traverse to the start_index while keeping track of the previous node.
                previous = current
                current = current.next
            else:
                if idx == start_index:
                    # Mark the node at start_index, it will connect to the node after end_index.
                    first = current
                # Reverse the current node's link to point to the previous reversed node.
                after = current.next
                current.next = dummy.next
                dummy.next = current
                current = after
        # Connect the node at start_index to the node after end_index.
        if current:
            first.next = current
        # Connect the reversed sublist to the rest of the linked list.
        if previous:
            previous.next = dummy.next
        else:
            # If start_index is 0, update the head of the list.
            self.linked_list.head = dummy.next
