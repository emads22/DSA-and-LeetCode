# Global variable to count the number of function calls
n_calls = 0


def fibonacci(n: int) -> int:
    """
    Recursive Fibonacci function without memoization.

    This function computes the nth Fibonacci number using a simple recursive approach.

    Time Complexity: O(2^n)
    - Each call results in two additional recursive calls, leading to exponential time complexity.

    Space Complexity: O(n)
    - The depth of the recursion tree is proportional to 'n'.

    Args:
        n (int): The Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    # Comment the following lines when demonstration is not needed
    global n_calls  # Used to track the number of function calls
    n_calls += 1    # Increment the function call count

    # Base case: if n is 0 or 1, return n
    if n == 0 or n == 1:
        return n

    # Recursive case: compute fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Initialize memoization array to store previously calculated Fibonacci numbers
memo = [None] * 100


def fibonacci_memoization(n: int) -> int:
    """
    Recursive Fibonacci function with memoization.

    This function computes the nth Fibonacci number using a recursive approach
    but stores previously computed values to avoid redundant calculations.

    Time Complexity: O(n)
    - Each Fibonacci number is computed once and then stored in the memo array.

    Space Complexity: O(n)
    - Storing the memoization array and the recursion stack both take linear space.

    Args:
        n (int): The Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    # Comment the following lines when demonstration is not needed
    global n_calls  # Used to track the number of function calls
    n_calls += 1    # Increment the function call count

    # If the value is already computed, return it from memo array
    if memo[n] is not None:
        return memo[n]

    # Base case: if n is 0 or 1, return n
    if n == 0 or n == 1:
        return n

    # Recursive case: compute fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)

    return memo[n]


def main():
    """
    Main function to test and compare the performance of both Fibonacci functions.

    This function resets the number of function calls, runs both the simple
    recursive Fibonacci and the memoized version, and prints the results.
    """
    global n_calls

    # Test cases for both functions
    test_cases = [10, 20, 30]

    # Test the recursive Fibonacci function
    print("\n\n==> Test the recursive Fibonacci function\n")
    for n in test_cases:
        n_calls = 0  # Reset function call counter
        print(f"\n\t* Testing fibonacci({n})...")
        result = fibonacci(n)
        print(f"\t\t. Result: {result}")
        print(f"\t\t. Function Calls: {n_calls}\n")
        print("   ", "-" * 40)

    # Test the memoized Fibonacci function
    print("\n\n==> Test the memoized Fibonacci function\n")
    for n in test_cases:
        n_calls = 0  # Reset function call counter
        # Reset memoization array for fresh calculation
        global memo
        memo = [None] * 100
        print(f"\n\t* Testing fibonacci_memoization({n})...")
        result = fibonacci_memoization(n)
        print(f"\t\t. Result: {result}")
        print(f"\t\t. Function Calls: {n_calls}\n")
        print("   ", "-" * 40)


if __name__ == "__main__":
    main()
