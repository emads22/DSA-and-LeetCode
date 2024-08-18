import sys
from pathlib import Path
from typing import TypeVar, Generic, Optional


# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Define a generic type variable to represent any type for use in the stack class
ItemType = TypeVar('ItemType')


class Stack(Generic[ItemType]):
    """
    A class representing a stack implemented as a list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.stack_list: list = []

    def __repr__(self) -> str:
        """
        Return a string representation of the stack.
        """
        display = "\n\n*         <-- IN\n          --> OUT"
        runner = ""
        for element in self.stack_list:
            runner = f"\n  | {element} |" + runner
        else:
            if runner == "":
                runner += f"\n  |   |"
        display += runner + f"""
  |___|

  . Top: {self.peak()}
  . Height: {self.size()}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the stack.
        """
        print(self)

    def size(self):
        return len(self.stack_list)

    def peak(self):
        """
        Return the top element of the stack without removing it.
        """
        if self.size() > 0:
            return self.stack_list[-1]
        return None

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return self.size() == 0

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        """
        self.stack_list.clear()

    def push(self, value: ItemType) -> None:
        """
        Push an element onto the stack.
        """
        self.stack_list.append(value)

    def pop(self) -> Optional[ItemType]:
        """
        Remove and return the top element of the stack.
        """
        if self.empty():
            return None
        return self.stack_list.pop()


class Solution:
    """
    A class that provides solutions for operations on a stack.

    Attributes:
        stack (LinkedList): The linked list to perform operations on.
    """

    def stack_as_list(self) -> Stack:
        """
        Return a new stack instance implemented as a list.
        """
        return Stack()

    def is_balanced_parentheses(self, parentheses: str) -> bool:
        """
        Check if the parentheses string is balanced.

        Args:
            parentheses (str): The string to check.

        Returns:
            bool: True if balanced, False otherwise.
        """
        stack = Stack()

        for char in parentheses:
            if char == "(":
                stack.push(char)  # Push open parenthesis
            elif char == ")":
                if stack.pop() is None:  # Pop for close parenthesis
                    return False
            else:
                return False  # Invalid character

        return stack.empty()  # Check if all open parentheses were matched

    def reverse_string(self, string: str) -> str:
        """
        Reverse the given string using a stack.

        Args:
            string (str): The string to reverse.

        Returns:
            str: The reversed string.
        """
        stack = Stack()  # Initialize stack
        reverse = ""  # Store reversed string
        for char in string:
            stack.push(char)  # Push each character onto the stack
        while stack.peak():
            reverse += stack.pop()  # Pop characters to form the reversed string
        return reverse  # Return the reversed string
