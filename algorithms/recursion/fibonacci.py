def fibonacci(n: int) -> int:
    """
    Recursive function to compute the nth Fibonacci number.

    Args:
        n (int): The Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    # Input validation
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    # Base case: if n is 0 or 1, return n
    if n == 0 or n == 1:
        return n

    # Recursive case: compute fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():

    # Test cases for both functions
    test_cases = [10, 20, 30, -40]

    # Test the recursive Fibonacci function
    print("\n\n==> Test the recursive Fibonacci function\n")
    for n in test_cases:
        print(f"\n\t* Testing fibonacci({n}):")
        try:
            result = fibonacci(n)
            print(f"\t\t. Result: {result}")
        except ValueError as error:
            print(f"\t\t. Result:\t{error}")
        print("\n   ", "-" * 40)

    # Time Complexity: O(2^n) - The function makes two calls for each n, leading to exponential time complexity.
    # Space Complexity: O(n) - Each recursive call adds to the stack, leading to linear space usage due to maximum call depth.


if __name__ == "__main__":
    main()
