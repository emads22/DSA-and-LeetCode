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
        display = "\n*         <-- IN\n          --> OUT"
        runner = ""
        for element in self.stack_list:
            runner = f"\n  | {element} |" + runner
        else:
            if runner == "":
                runner += f"\n  |   |"
        display += runner + f"""
  |___|

  . Top: {self.peek()}
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

    def peek(self):
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
        while stack.peek():
            reverse += stack.pop()  # Pop characters to form the reversed string
        return reverse  # Return the reversed string


def main() -> None:
    """
    Test each method of the Solution class with various cases.
    """
    solution = Solution()

    # Test stack_as_list method
    print("\n==> Test: stack_as_list method:")
    stack_list = solution.stack_as_list()
    stack_list.push(1)
    stack_list.push(2)
    stack_list.push(3)
    print("\n______ Stack after pushing 1, 2, 3 ______")
    stack_list.display()
    print("-" * 80)

    # Pop from the stack
    print("\n==> Test: Pop from the stack\n")
    while not stack_list.empty():
        print(f"\t\t. Popped value: {stack_list.pop()}")
    print(f"\n\t. Is stack empty? {stack_list.empty()}\n")
    print("-" * 80)

    # Test is_balanced_parentheses method
    print("\n==> Test: is_balanced_parentheses method\n")
    test_cases = [
        ("()", True),
        ("(())", True),
        ("(()", False),
        ("())", False),
        ("", True),
        ("()()", True)
    ]
    for parentheses, expected in test_cases:
        result = solution.is_balanced_parentheses(parentheses)
        parentheses = parentheses if parentheses else "\t"
        print(f"\t\t. Parentheses: {parentheses}\t|\tExpected: {
              expected}\t|\tResult: {result}")
    print("\n", "-" * 80)

    # Test reverse_string method
    print("\n==> Test: reverse_string method\n")
    strings_to_reverse = [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("", ""),
        ("abcd", "dcba"),
        ("racecar", "racecar")  # Palindrome
    ]
    for string, expected in strings_to_reverse:
        result = solution.reverse_string(string)
        string = string if string else "\t"
        expected = expected if expected else "\t"
        print(f"\t\t. Original:\t{string}\t|\tExpected:\t{
              expected}\t|\tReversed:\t{result}")
    print("\n", "-" * 80)


if __name__ == "__main__":
    main()
