from typing import TypeVar, Optional


# Define a generic type variable to represent any type for use in the stack class
ItemType = TypeVar('ItemType')


class Solution:
    """
    A class that provides solutions for various operations using dynamic programming.
    """

    def max_money_robbed(self, nums: list[int]) -> int:
        """
        Calculate the maximum amount of money that can be robbed without triggering alarms.

        This function determines the maximum amount of money that can be robbed from a list of houses,
        where each house has a certain amount of money, and adjacent houses cannot be robbed on the same night.

        Parameters:
        nums (list[int]): A list of integers where each element represents the amount of money in a house.

        Returns:
        int: The maximum amount of money that can be robbed without alerting the police.
        """
        # # METHOD 1
        # if len(nums) == 0:  # If there are no houses, return 0
        #     return 0
        # if len(nums) == 1:  # If there's only one house, return its money
        #     return nums[0]
        # max_money1 = money1 = 0  # Initialize variables for even-indexed houses
        # max_money2 = money2 = 0  # Initialize variables for odd-indexed houses
        # # Loop through all houses
        # for i in range(len(nums)):
        #     if i % 2 == 0:  # If the index is even
        #         money1 += nums[i]  # Add money from the even-indexed house
        #         # Update the maximum for even-indexed houses
        #         max_money1 = max(max_money1, money1)
        #     else:  # If the index is odd
        #         money2 += nums[i]  # Add money from the odd-indexed house
        #         # Update the maximum for odd-indexed houses
        #         max_money2 = max(max_money2, money2)
        # # Return the maximum money robbed from either the even or odd indexed houses
        # return max(max_money1, max_money2)

        # Time Complexity: O(n) - Each house is examined once, making the function efficient.
        # Space Complexity: O(1) - The function uses a constant amount of space for variables.

        # METHOD 2: Bottom-Up Dynamic Programming
        # Variables to store the maximum money robbed up to two previous houses
        till_before_previous = 0  # Maximum money robbed up to the house before the previous one
        till_previous = 0         # Maximum money robbed up to the last house
        # Loop through the list of house values
        for current in nums:
            # Calculate the maximum money that can be robbed if we rob the current house or not
            temp = max(till_before_previous + current, till_previous)
            # Update the previous values for the next iteration
            till_before_previous = till_previous
            till_previous = temp
        return till_previous  # The maximum money robbed will be in till_previous

        # Time Complexity: O(n) - Each house is examined once, where n is the number of houses.
        # Space Complexity: O(1) - Only a fixed amount of space is used (variables).

    def max_profit(self, prices: list[int]) -> int:
        """
        Calculate the maximum profit from buying and selling a single share of stock.

        This function implements two methods to find the maximum profit possible given a list of stock prices. 
        Method 1 uses a greedy algorithm, while Method 2 employs a dynamic programming approach. 
        It assumes that you can only buy and sell once.

        Parameters:
        prices (list[int]): A list of integers where each element represents the stock price on a particular day.

        Returns:
        int: The maximum profit that can be achieved.
        """

        # # METHOD 1: Greedy Algorithm
        # if len(prices) == 0:  # Check for empty price list
        #     return 0
        # max_profit = profit = 0  # Initialize max profit and current profit
        # buy = prices[0]  # Set the initial buy price to the first day's price
        # # Loop through the prices starting from the second day
        # for i in range(1, len(prices)):
        #     # If current price is lower than the buy price, update buy price
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     else:
        #         # Calculate profit if selling at the current price
        #         profit = prices[i] - buy
        #         # Update the maximum profit found so far
        #         max_profit = max(profit, max_profit)
        # # Return the maximum profit found using the greedy method
        # return max_profit

        # Time Complexity: O(n) - Each price is examined once.
        # Space Complexity: O(1) - Only a fixed amount of space is used (variables).

        # METHOD 2: Dynamic Programming Algorithm
        if len(prices) == 0:  # Check for empty price list
            return 0
        buy = prices[0]  # Initialize the buy price to the first day's price
        # Initialize the dp array to store maximum profit values for each day
        dp = [0] * len(prices)
        # Loop through the prices starting from the second day
        for i in range(1, len(prices)):
            # Update buy price to the minimum price seen so far
            buy = min(buy, prices[i])
            # Calculate the maximum profit up to the current day
            dp[i] = max(dp[i-1], prices[i] - buy)
        # Return the maximum profit found using the dynamic programming method
        # The last element in dp array contains the maximum profit
        return dp[-1]

        # Time Complexity: O(n) - Each price is examined once.
        # Space Complexity: O(n) - The dp array stores profit values for each day.

    def climb_stairs(self, n: int) -> int:
        """
        Given the number of steps 'n', this function returns the number of distinct ways
        to reach the top of the staircase.
        The problem can be thought of as a Fibonacci sequence, where the number of ways to reach
        step n is the sum of ways to reach steps n-1 and n-2.

        Parameters:
        n (int): The number of steps to reach the top.

        Returns:
        int: The number of distinct ways to climb to the top of the staircase.
        """
        # # METHOD 1: Recursive approach similar to Fibonacci (inefficient without memoization)
        # # Base cases: If there are 1 or 2 steps, the answer is n itself.
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # # Recursive case: sum of ways to get to the previous step and the step before that
        # return self.climb_stairs(n-1) + self.climb_stairs(n-2)

        # Time Complexity - O(2^n) (without memoization)
        # Space Complexity - O(n) (due to recursion stack)

        # METHOD 2: Iterative dynamic programming approach (efficient)
        # Base case: If there are 1 or 2 steps, return 'n' directly.
        # There is only 1 way to climb 1 step, and 2 ways to climb 2 steps.
        if n <= 2:
            return n

        # Initialization:
        # - 'ways_till_before_previous' is the number of ways to reach the step two steps before (n-2).
        # - 'ways_till_previous' is the number of ways to reach the previous step (n-1).
        ways_till_before_previous = 1  # There is 1 way to reach step 1.
        ways_till_previous = 2  # There are 2 ways to reach step 2.
        total_ways = 0

        # Iterate from step 3 to step 'n' to calculate the number of ways to reach each step.
        for i in range(3, n + 1):
            # The number of ways to reach the current step is the sum of the ways
            # to reach the previous step and the step two steps back.
            total_ways = ways_till_previous + ways_till_before_previous

            # Update the values for the next iteration:
            # - 'ways_till_before_previous' becomes the old 'ways_till_previous'
            # - 'ways_till_previous' becomes the current 'total_ways'
            ways_till_before_previous = ways_till_previous
            ways_till_previous = total_ways

        # After the loop, 'total_ways' holds the number of ways to reach step 'n'.
        return total_ways

        # Time Complexity: O(n), where 'n' is the number of steps. The loop runs from 3 to n.
        # Space Complexity: O(1), as only a constant amount of extra space is used (three variables).


def main():

    solution = Solution()

    # Test max_money_robbed
    print("\n==> Test max_money_robbed()\n")
    nums1 = [1, 2, 3, 1]
    max_money1 = solution.max_money_robbed(nums1)  # Output: 4
    print(f"\t. Nums: {nums1}")
    print(f"\t. Maximum money robbed: {max_money1}\n")

    nums2 = [2, 7, 9, 3, 1]
    max_money2 = solution.max_money_robbed(nums2)  # Output: 12
    print(f"\t. Nums: {nums2}")
    print(f"\t. Maximum money robbed: {max_money2}\n")

    nums3 = [1, 9, 3]
    max_money3 = solution.max_money_robbed(nums3)  # Output: 9
    print(f"\t. Nums: {nums3}")
    print(f"\t. Maximum money robbed: {max_money3}\n")

    nums4 = [2, 3]
    max_money4 = solution.max_money_robbed(nums4)  # Output: 3
    print(f"\t. Nums: {nums4}")
    print(f"\t. Maximum money robbed: {max_money4}\n")
    print("-" * 60)

    # Test max_profit
    print("\n==> Test max_profit()\n")
    prices1 = [7, 1, 5, 3, 6, 4]
    max_profit1 = solution.max_profit(prices1)  # Output: 5
    print(f"\t. Prices: {prices1}")
    print(f"\t. Maximum profit: {max_profit1}\n")

    prices2 = [7, 6, 4, 3, 1]
    max_profit2 = solution.max_profit(prices2)  # Output: 0
    print(f"\t. Prices: {prices2}")
    print(f"\t. Maximum profit: {max_profit2}\n")

    prices3 = [1, 2, 3, 4, 5]    # Output: 4 (buy at 1, sell at 5)
    max_profit3 = solution.max_profit(prices3)
    print(f"\t. Prices: {prices3}")
    print(f"\t. Maximum profit: {max_profit3}\n")

    prices4 = [5, 3, 6, 1, 4]    # Output: 3 (buy at 3, sell at 6)
    max_profit4 = solution.max_profit(prices4)
    print(f"\t. Prices: {prices4}")
    print(f"\t. Maximum profit: {max_profit4}\n")
    print("-" * 60)

    # Test climb_stairs
    print("\n==> Test climb_stairs()\n")
    n1 = 2
    climb_stairs1 = solution.climb_stairs(n1)  # Output: 2
    print(f"\t. Total number of stairs: {n1}")
    print(f"\t. Total distinct ways to climb to the top: {
          climb_stairs1}\n")

    n2 = 3
    climb_stairs2 = solution.climb_stairs(n2)  # Output: 3
    print(f"\t. Total number of stairs: {n2}")
    print(f"\t. Total distinct ways to climb to the top: {
          climb_stairs2}\n")

    n3 = 4
    climb_stairs3 = solution.climb_stairs(n3)  # Output: 5
    print(f"\t. Total number of stairs: {n3}")
    print(f"\t. Total distinct ways to climb to the top: {
          climb_stairs3}\n")

    n4 = 5
    climb_stairs4 = solution.climb_stairs(n4)  # Output: 8
    print(f"\t. Total number of stairs: {n4}")
    print(f"\t. Total distinct ways to climb to the top: {
          climb_stairs4}\n")
    print("-" * 60)


if __name__ == "__main__":
    main()
