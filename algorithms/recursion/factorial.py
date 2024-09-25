def factorial(n: int) -> int:
    """
    Recursive function to compute the factorial of a given number.

    Args:
        n (int): The number to calculate its factorial. Should be a non-negative integer.

    Returns:
        int: The factorial of the number n.
    """
    # Input validation
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: compute n * factorial(n - 1)
    return n * factorial(n - 1)

    # Time Complexity: O(n) - The function makes n recursive calls, resulting in linear time complexity.
    # Space Complexity: O(n) - Each recursive call adds to the stack, leading to linear space usage due to maximum call depth.


def main():

    # Test cases for both functions
    test_cases = [3, 4, 5, -6]

    # Test the recursive Factorial function
    print("\n\n==> Test the recursive Factorial function\n")
    for n in test_cases:
        print(f"\n\t* Testing factorial({n}):")
        try:
            result = factorial(n)
            print(f"\t\t. Result: {result}")
        except ValueError as error:
            print(f"\t\t. Result:\t{error}")
        print("\n   ", "-" * 40)


if __name__ == "__main__":
    main()
