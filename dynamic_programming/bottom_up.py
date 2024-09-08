def fibonacci_bot_up(n: int) -> int:
    """
    Bottom-up Fibonacci function using iteration.
    
    This function computes the nth Fibonacci number using an iterative approach,
    building up the solution from the base cases.
    
    Time Complexity: O(n)
    - Each Fibonacci number up to n is computed exactly once.

    Space Complexity: O(n)
    - An array of size n+1 is used to store Fibonacci numbers.

    Args:
        n (int): The Fibonacci number to calculate.
    
    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer, as Fibonacci numbers are not defined for negative indices.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    fib_list = [0, 1]
    
    for i in range(2, n + 1):
        next_val = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_val)
    
    return fib_list[n]


def main():
    """
    Main function to test and compare the performance of the Fibonacci functions.
    
    This function resets the number of function calls, runs the bottom-up Fibonacci function, 
    and prints the result.
    """
       
    # Test cases for all functions
    test_cases = [10, 20, 30]
    
    # Test the bottom-up Fibonacci function
    print("\n\n==> Test the bottom-up Fibonacci function\n")
    for n in test_cases:
        print(f"\t* Testing fibonacci_bot_up({n})...")
        result = fibonacci_bot_up(n)
        print(f"\t\t. Result: {result}")
        print("   ", "-" * 40)

if __name__ == "__main__":
    main()