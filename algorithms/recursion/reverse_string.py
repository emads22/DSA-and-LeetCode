def reverse_string(string: str) -> str:
    """
    Recursive function to reverse a string.

    Args:
        string (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    # Base case: if the string is empty, return an empty string
    if len(string) == 0:
        return ""

    # Recursive case: concatenate the last character with the reverse of the rest of the string
    return string[-1] + reverse_string(string[:-1])
    # Alternatively:
    # return  reverse_string(string[1:]) + string[0]

    # Time Complexity: O(n) - Each character is processed once
    # Space Complexity: O(n) - Recursive call stack and string concatenation


def main():
    # Test cases for the reverse_string function
    test_cases = ["Python", "hello", "world", ""]

    # Test the recursive reverse string function
    print("\n\n==> Test the recursive reverse string function\n")
    for n in test_cases:
        print(f"\n\t* Testing reverse_string({n}):")
        result = reverse_string(n)
        print(f"\t\t. Result: {result}")
        print("\n   ", "-" * 40)


if __name__ == "__main__":
    main()
