import sys
from pathlib import Path


# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))


from data_structures import StackList


class Solution:
    """
    A class that provides solutions for operations on a stack.
    """

    def stack_as_list(self) -> StackList:
        """
        Return a new stack instance implemented as a list.
        """
        return StackList()

    def is_balanced_parentheses(self, parentheses: str) -> bool:
        """
        Check if the parentheses string is balanced.

        Args:
            parentheses (str): The string to check.

        Returns:
            bool: True if balanced, False otherwise.
        """
        stack = StackList()

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
        stack = StackList()  # Initialize stack
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
