import sys
from pathlib import Path


# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))


from typing import TypeVar, Optional
from data_structures import QueueTwoStacks


# Define a generic type variable to represent any type for use in the stack class
ItemType = TypeVar('ItemType')


class Solution:
    """
    A class that provides an interface for queue operations using a QueueTwoStacks instance.
    """

    def __init__(self) -> None:
        """
        Initialize the Solution with a new QueueTwoStacks instance.

        This constructor creates a new QueueTwoStacks object and assigns it to the Solution instance.
        """
        self.queue = QueueTwoStacks()

    def enqueue_method(self, value: ItemType) -> None:
        """
        Add an element to the queue.

        Args:
            value (ItemType): The element to add to the queue.
        """
        self.queue.enqueue(value)

    def dequeue_method(self) -> Optional[ItemType]:
        """        
        Remove and return the front element of the queue.
        """
        return self.queue.dequeue()


def main():
    # Create a Solution instance
    solution = Solution()
    print("\n==> New Queue created")
    solution.queue.display()
    print("-" * 80)

    # Test: Enqueue Integers
    print("\n==> Test: Enqueue Integers\n")
    for n in [1, 2, 3]:
        print(f"\n______ Enqueue element {n} ______")
        solution.enqueue_method(n)
        solution.queue.display()
    print("-" * 80)

    # Test: Dequeue Integers
    print("\n==> Test: Dequeue Integers\n")
    while not solution.queue.is_empty():
        print(f"\n______ Dequeued value: {solution.dequeue_method()} ______")
        solution.queue.display()
    print("-" * 80)


if __name__ == "__main__":
    main()
