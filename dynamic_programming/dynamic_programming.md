# I. Dynamic Programming

Dynamic Programming (DP) is a powerful technique used in computer science to solve complex problems by breaking them down into simpler subproblems. It is particularly useful in optimization problems where the solution can be constructed incrementally. DP avoids redundant computations by storing the results of subproblems, which can be reused in the final solution.

DP is defined by two main properties:

## 1. Overlapping Subproblems
In many problems, the same subproblems are solved multiple times. DP addresses this by solving each subproblem once, storing its solution in a table (or memoization), and reusing the result whenever the same subproblem is encountered again. This eliminates the need to recompute solutions, thus improving efficiency.

### Example: Fibonacci Sequence
To calculate the Fibonacci number `Fib(n)`, we need `Fib(n-1)` and `Fib(n-2)`. Without DP, we would end up recalculating many Fibonacci numbers multiple times, leading to exponential time complexity. With DP, we store each Fibonacci number once and reuse it, reducing the complexity to linear time.

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

## 2. Optimal Substructure
A problem exhibits an optimal substructure when the optimal solution to the entire problem can be built from the optimal solutions to its subproblems. DP exploits this property by solving each subproblem optimally and combining those results to solve the larger problem. This allows for efficient construction of the final solution.

### Example: Shortest Path (Bellman-Ford Algorithm)
In the shortest path problem, the optimal solution (shortest path) from a starting node to any destination node can be determined by considering the shortest path to neighboring nodes and adding the edge weight. DP stores the shortest paths to each node, ensuring that each path is built optimally based on smaller subproblems.

```python
def bellman_ford(graph, V, E, src):
    dist = [float('inf')] * V
    dist[src] = 0
    
    for _ in range(V - 1):
        for u, v, w in E:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    return dist
```

## When is Dynamic Programming Used?
Dynamic Programming is used in problems where there are overlapping subproblems and where the solution can be built from subproblem solutions. Some common examples include:

- **Fibonacci Sequence**: DP optimizes the recursive calculation of Fibonacci numbers by storing previously computed values.
- **Knapsack Problem**: DP is used to determine the maximum value that can be obtained by selecting a combination of items with given weights and values.
- **Shortest Path in Graphs**: Algorithms like Bellman-Ford and Floyd-Warshall use DP to find the shortest paths between nodes in a weighted graph.
- **Matrix Chain Multiplication**: DP minimizes the number of scalar multiplications needed to multiply a sequence of matrices.
- **Longest Common Subsequence**: DP efficiently finds the longest subsequence that is common between two sequences.

These are just a few examples, but DP is widely applied in various optimization problems in fields like algorithms, artificial intelligence, and operations research.

### Conclusion
Dynamic Programming optimizes problem-solving by using overlapping subproblems and optimal substructure properties. By storing and reusing subproblem solutions, DP transforms problems that would otherwise have high time complexity into more manageable solutions.


# II. Memoization and Bottom-Up Approach in Dynamic Programming

## Memoization

### Definition
Memoization is a technique in dynamic programming used to optimize recursive algorithms by storing the results of expensive function calls and reusing these results when the same inputs occur again. This technique prevents redundant calculations and improves computational efficiency.

### Benefits
- **Reduces Redundant Computations**: Memoization stores previously computed results, thus preventing the recalculation of values for the same inputs.
- **Improves Efficiency**: For problems with overlapping subproblems, memoization reduces the time complexity from exponential to linear or polynomial.
- **Easy to Implement**: Memoization can often be implemented with minimal modifications to a basic recursive solution.

### Uses
Memoization is particularly effective in scenarios where:
- The same subproblems are solved multiple times, such as in recursive algorithms for sequences or combinatorial problems.
- Optimal substructure exists, meaning the problem can be decomposed into overlapping subproblems that can be solved independently.

### Big O Complexity
- **Time Complexity**: O(n), where `n` is the number of unique subproblems. Each subproblem is solved once and stored.
- **Space Complexity**: O(n) for the space required to store results in a memoization table.

### Example
Consider the Fibonacci sequence calculation:

```python
memo = [None] * 100

def fibonacci_memo(n: int) -> int:
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]
```

- In this example, `fibonacci_memo` uses memoization to store previously computed Fibonacci numbers, thus avoiding redundant calculations.

## Bottom-Up Approach

### Definition
The bottom-up approach, also known as tabulation, is a technique in dynamic programming where the solution is built iteratively from the simplest cases up to the final problem. This approach constructs a table of solutions to subproblems in a systematic manner.

### Benefits
- **Avoids Recursive Overhead**: By using iteration rather than recursion, the bottom-up approach eliminates the overhead associated with recursive function calls.
- **Optimal Space Usage**: Often uses less space compared to memoization because it generally only maintains a table of intermediate results.
- **Improved Performance**: Particularly efficient for problems where subproblems can be solved in a sequential order and the solution can be constructed iteratively.

### Uses
The bottom-up approach is well-suited for problems where:
- There is a clear ordering of subproblems, with each subproblem depending on the results of previously solved subproblems.
- An iterative solution is preferable, and the problem can be effectively solved by building up from base cases.

### Big O Complexity
- **Time Complexity**: O(n), where `n` is the number of subproblems to solve. Each subproblem is solved exactly once.
- **Space Complexity**: O(n) for the space needed to store intermediate results in a table.

### Example
Consider the Fibonacci sequence calculation with the bottom-up approach:

```python
def fibonacci_bot_up(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    fib_list = [0, 1]
    for i in range(2, n + 1):
        next_val = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_val)
    return fib_list[n]
```

- In this example, `fibonacci_bot_up` builds up the solution iteratively, storing results in a list to avoid redundant calculations.

## Summary
- **Memoization** is ideal for problems with overlapping subproblems and is implemented through recursive solutions enhanced with result caching.
- **Bottom-Up Approach** is appropriate for problems that can be solved iteratively by building solutions from the ground up.

Both techniques are fundamental in dynamic programming, offering different methods for optimizing and managing complexity in problem-solving.
