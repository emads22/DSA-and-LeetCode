import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data_structures import LinkedList, Node_LL


class Solution:
    """
    A class that provides solutions for merge sort operations on a linked list.

    Attributes:
        linked_list (LinkedList[int]): The linked list to perform operations on.
    """

    def __init__(self) -> None:
        """
        Initialize the Solution with a new linked list instance for integers.
        """
        self.linked_list: LinkedList[int] = LinkedList(
        )  # Initialize as a LinkedList of int type.

    def merge(self, other_list: LinkedList[int]) -> None:
        """
        Merge the current linked list with another sorted linked list in ascending order.

        Parameters:
            other_list (LinkedList[int]): Another linked list to be merged with the current linked list.

        Returns:
            None: Modifies the current linked list in place to include the merged result.
        """

        # Create a dummy node to start the merged list and a "current" pointer to track its progress.
        current = dummy = Node_LL(0)

        # Pointers to the heads of both linked lists.
        head = self.linked_list.head
        other_head = other_list.head

        # Traverse both lists and merge them based on the smallest node values.
        while head is not None and other_head is not None:
            if head.value < other_head.value:
                # Attach the smaller node to the merged list and move the pointer in the current list.
                current.next = head
                head = head.next
            else:
                # Attach the smaller node from the other list and move the other list's pointer.
                current.next = other_head
                other_head = other_head.next
            # Move the "current" pointer forward.
            current = current.next

        # If any nodes remain in the current list, attach them to the merged list.
        if head is not None:
            current.next = head

        # If any nodes remain in the other list, attach them to the merged list.
        elif other_head is not None:
            current.next = other_head
            # Update the tail pointer to reflect the tail of the other list.
            self.linked_list.tail = other_list.tail

        # Update the head of the current list to point to the start of the merged list.
        self.linked_list.head = dummy.next
        # Update the length of the current list to account for the nodes from both lists.
        self.linked_list.length += other_list.length


def main():
    """
    Test the merge functionality of the Solution class with various cases.
    """

    # Test Case 1: Merging two non-empty linked lists of equal length
    print("\n==> Test Case 1: Merging two non-empty linked lists of equal length:\n")
    l1 = LinkedList()
    l1.from_list([1, 3, 5])

    l2 = LinkedList()
    l2.from_list([2, 4, 6])

    solution1 = Solution()
    solution1.linked_list = l1
    print("\t\t- List 1:", l1.to_list())
    print("\t\t- List 2:", l2.to_list(), "\n")

    solution1.merge(l2)
    solution1.linked_list.display()
    print("-" * 80)

    # Test Case 2: Merging a non-empty list with an empty list
    print("\n==> Test Case 2: Merging a non-empty list with an empty list\n")
    l3 = LinkedList()
    l3.from_list([10, 20])

    l4 = LinkedList()  # Empty list

    solution2 = Solution()
    solution2.linked_list = l3

    print("\t\t- List 1:", l3.to_list())
    print("\t\t- List 2:", l4.to_list(), "\n")

    solution2.merge(l4)
    solution2.linked_list.display()
    print("-" * 80)

    # Test Case 3: Merging two empty lists
    print("\n==> Test Case 3: Merging two empty lists\n")
    l5 = LinkedList()  # Empty list
    l6 = LinkedList()  # Empty list

    solution3 = Solution()
    solution3.linked_list = l5
    print("\t\t- List 1:", l5.to_list())
    print("\t\t- List 2:", l6.to_list())

    solution3.merge(l6)
    solution3.linked_list.display()
    print("-" * 80)

    # Test Case 4: Merging lists where one list has more elements than the other
    print("\n==> Test Case 4: Merging lists where one list has more elements than the other\n")
    l7 = LinkedList()
    l7.from_list([1, 4, 7])

    l8 = LinkedList()
    l8.from_list([2])

    solution4 = Solution()
    solution4.linked_list = l7
    print("\t\t- List 1:", l7.to_list())
    print("\t\t- List 2:", l8.to_list())

    solution4.merge(l8)
    solution4.linked_list.display()
    print("-" * 80)


if __name__ == "__main__":
    main()
