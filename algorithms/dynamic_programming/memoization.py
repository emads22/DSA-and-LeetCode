# Global variable to count the number of function calls
n_calls = 0


def fibonacci(n: int) -> int:
    """
    Recursive Fibonacci function without memoization.

    This function computes the nth Fibonacci number using a simple recursive approach.

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

    # Time Complexity: O(2^n) - Each call results in two additional recursive calls, leading to exponential time complexity.
    # Space Complexity: O(n) - The depth of the recursion tree is proportional to 'n'.


def fibonacci_memoization(n: int) -> int:
    """
    Recursive Fibonacci function with memoization.

    This function computes the nth Fibonacci number using a recursive approach,
    while storing previously computed values in a memoization dictionary to avoid
    redundant calculations.    

    Args:
        n (int): The Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    # Initialize memoization dictionary to store previously calculated Fibonacci numbers
    memo = {}

    def _fib_memo(n: int) -> int:
        # Comment the following lines when demonstration is not needed
        global n_calls  # Used to track the number of function calls
        n_calls += 1    # Increment the function call count

        # If the value is already computed, return it from the memo dictionary
        if n in memo:
            return memo[n]

        # Base case: if n is 0 or 1, return n
        if n == 0 or n == 1:
            return n

        # Recursive case: compute fibonacci(n - 1) + fibonacci(n - 2) and store in memo
        memo[n] = _fib_memo(n - 1) + _fib_memo(n - 2)

        return memo[n]

    return _fib_memo(n)

    # Time Complexity: O(n) - Each Fibonacci number is computed once and then stored in the memo dictionary.
    # Space Complexity: O(n) - Storing the memoization dictionary and the recursion stack both take linear space.


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
        # Reset memoization dict for fresh calculation
        global memo
        memo = {}
        print(f"\n\t* Testing fibonacci_memoization({n})...")
        result = fibonacci_memoization(n)
        print(f"\t\t. Result: {result}")
        print(f"\t\t. Function Calls: {n_calls}\n")
        print("   ", "-" * 40)


if __name__ == "__main__":
    main()
