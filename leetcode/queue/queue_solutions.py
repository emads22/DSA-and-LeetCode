import sys
from pathlib import Path
from typing import TypeVar, Generic, Optional


# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Define a generic type variable to represent any type for use in the stack class
ItemType = TypeVar('ItemType')


class Queue(Generic[ItemType]):
    """
    A class representing a queue implemented using two stacks, where each stack is implemented as a list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty queue with two stacks.
        `Stack1` primarily represents the queue, where elements are stored in the correct order.
        `Stack2` is used temporarily during operations to maintain the queue order.
        """
        self.stack1 = []
        self.stack2 = []

    def __repr__(self) -> str:
        """
        Return a string representation of the queue.
        """
        display = "\n\n*         <-- IN               <-- IN\n          --> OUT              --> OUT"
        runner = ""
        for element in self.stack1:
            runner = f"\n  | {element} |                |   |" + runner
        else:
            if runner == "":
                runner += f"\n  |   |"
        display += runner + f"""
  |___|                |___|

  STACK_1              STACK_2


  . Top: {self.peak()}
  . Height: {self.size()}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the queue.
        """
        print(self)

    def size(self):
        """
        Return the number of elements in the queue.
        """
        return len(self.stack1)

    def peak(self):
        """
        Return the first element of the queue (top element of stack1) without removing it.
        """
        if self.size() > 0:
            return self.stack1[-1]
        return None

    def empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return self.size() == 0

    def clear(self) -> None:
        """
        Remove all elements from the queue.
        """
        self.stack1.clear()

    def enqueue(self, value: ItemType) -> None:
        """
        Add an element to the back of the queue.
        """
        # Move all elements from stack1 to stack2 to access the bottom.
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        # Add the new value to the bottom of stack1.
        self.stack1.append(value)
        # Move all elements back from stack2 to stack1 to restore order.
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self) -> Optional[ItemType]:
        """        
        Remove and return the front element of the queue.
        """
        if self.empty():
            return None
        return self.stack1.pop()


class Solution:
    """
    A class that provides an interface for queue operations using a Queue instance.
    """

    def __init__(self):
        """
        Initialize the Solution with a new queue instance.

        This constructor creates a new Queue object and assigns it to the Solution instance.
        """
        self.queue = Queue()

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
