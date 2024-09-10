from typing import Optional


class Solution:
    """
    A class containing solutions to various algorithmic problems. 

    This class includes methods to:
    - Remove all occurrences of a specific value from a list.
    - Find the maximum and minimum values in a list.
    - Find the longest string in a list of strings.
    - Remove duplicates from a sorted list of integers.
    - Calculate the maximum profit from buying and selling a single share of stock.
    - Rotate the elements of a list to the right by a specified number of steps.
    - Find the sum of the maximum contiguous subarray using Kadane's Algorithm.
    """

    def remove_element(self, nums: list[int], val: int) -> int:
        """
        Removes all occurrences of 'val' from the input list 'nums' in-place
        and returns the new length of the modified list.

        Parameters:
        nums (list[int]): List of integers from which occurrences of 'val' should be removed.
        val (int): The value to be removed from the list.

        Returns:
        int: The new length of the list after removing all occurrences of 'val'.
        """
        # Initialize index pointer to traverse through the list
        i = 0
        # Loop through the list
        while i < len(nums):
            # If the current element matches 'val', remove it
            if nums[i] == val:
                nums.pop(i)
            else:
                # If not, move to the next element
                i += 1
        # Return the new length of the modified list
        return len(nums)

    def find_max_min(self, myList: list[int]) -> Optional[tuple[int, int]]:
        """
        Finds the maximum and minimum values in a list of integers.

        This method provides two different approaches to find the max and min:
        - METHOD 1 uses Python's built-in max() and min() functions for each comparison.
        - METHOD 2 performs explicit comparisons using if-elif conditions.

        Args:
            myList (list[int]): A list of integers to find the max and min values.

        Returns:
            Optional[Tuple[int, int]]: A tuple containing the maximum and minimum
                                    values of the list. Returns None if the list is empty.
        """

        # # METHOD 1: Using built-in max() and min() functions
        # if len(myList) == 0:  # Handle empty list case
        #     return None
        # # Initialize both maximum and minimum with the first element
        # maximum = minimum = myList[0]
        # # Iterate through the list and update maximum and minimum using max() and min()
        # for num in myList:
        #     maximum = max(maximum, num)
        #     minimum = min(minimum, num)
        # # Return the maximum and minimum as a tuple
        # return maximum, minimum

        # METHOD 2: Using explicit if-elif comparisons
        if len(myList) == 0:  # Handle empty list case
            return None
        # Initialize both maximum and minimum with the first element
        maximum = minimum = myList[0]
        # Iterate through the list and update maximum and minimum based on comparisons
        for num in myList:
            if num > maximum:
                maximum = num  # Update maximum if current num is larger
            elif num < minimum:
                minimum = num  # Update minimum if current num is smaller
        # Return the maximum and minimum as a tuple
        return maximum, minimum

    def find_longest_string(self, string_list: list[str]) -> str:
        """
        Find the longest string in a list of strings.

        This method provides two implementations for finding the longest string.

        METHOD 1:
        - Handles the case where the list might be empty.
        - Iterates through the list, keeping track of the longest string by comparing lengths.

        METHOD 2:
        - Provides an alternative implementation using a simpler approach.
        - Directly iterates through the list and keeps track of the longest string.

        Args:
            string_list (list[str]): A list of strings to be evaluated.

        Returns:
            str: The longest string from the list. If the list is empty, returns an empty string.
        """

        # # METHOD 1
        # if len(string_list) == 0:  # Handle empty list case
        #     return ""
        # longest = string_list[0]  # Initialize the longest string with the first element
        # for i in range(1, len(string_list)):  # Iterate through the rest of the list
        #     if len(string_list[i]) > len(longest):  # Compare lengths
        #         longest = string_list[i]  # Update the longest string
        # return longest

        # METHOD 2
        # Initialize the longest string as an empty string
        longest = ""
        # Iterate through the list of strings
        for string in string_list:
            # Compare lengths and update the longest string if needed
            if len(string) > len(longest):
                longest = string
        return longest

    def remove_duplicates(self, nums: list[int]) -> int:
        """
        Removes duplicates from a sorted list of integers in-place and returns the new length of the list containing only unique elements.

        Parameters:
        nums (list[int]): A sorted list of integers with potential duplicates.

        Returns:
        int: The length of the list after duplicates have been removed.
        """

        # # METHOD 1: Two-pointer approach
        # if len(nums) == 0:
        #     return 0
        # i, j = 0, 1  # Initialize two pointers
        # while j < len(nums):
        #     if nums[j] == nums[i]:
        #         j += 1  # Move the second pointer forward if the current element is a duplicate
        #     else:
        #         i += 1  # Move the first pointer to the next unique element position
        #         # Swap the current element with the next unique position
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j += 1  # Move the second pointer forward
        # return i + 1  # Return the length of the list with unique elements

        # METHOD 2: Single-pass approach
        if len(nums) == 0:
            return 0
        write_pointer = 1  # Initialize a pointer for writing unique elements
        # Iterate over the list starting from the second element
        for read_pointer in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[read_pointer] != nums[read_pointer - 1]:
                # Write the unique element to the write_pointer position
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1  # Move the write_pointer forward
        return write_pointer  # Return the length of the list with unique elements

    def max_profit(self, prices: list[int]) -> int:
        """
        Calculate the maximum profit from buying and selling a single share of stock.

        This function implements two methods to find the maximum profit possible given a list of stock prices. It assumes 
        that you can only buy and sell once.

        Parameters:
        prices (list[int]): A list of integers where each element represents the stock price on a particular day.

        Returns:
        int: The maximum profit that can be achieved.

        Time Complexity:
        Both methods have a time complexity of O(n), where n is the number of elements in the `prices` list.
        """

        # METHOD 1: Iterates through the list and updates the buying price and profit
        max_profit = profit = 0
        # Initialize the buy price to the positive infinity (also will hande empty list case)
        buy_price = float('+inf')
        for price in prices:
            # Update the buy price if a lower price is found
            if price < buy_price:
                buy_price = price
            else:
                # Calculate profit if selling at the current price
                profit = price - buy_price
            # Update the maximum profit found so far
            max_profit = max(profit, max_profit)
        return max_profit

        # # METHOD 2: Tracks the minimum price seen so far and calculates profit in a single pass
        # # Initialize the buy price to the positive infinity (also will hande empty list case)
        # buy_price = float('+inf')
        # max_profit = 0
        # for price in prices:
        #     # Update the buy price to the minimum of the current price and the previous buy price
        #     buy_price = min(price, buy_price)
        #     # Calculate profit if selling at the current price
        #     profit = price - buy_price
        #     # Update the maximum profit found so far
        #     max_profit = max(profit, max_profit)
        # return max_profit

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate the elements of the list 'nums' to the right by 'k' steps.

        This function implements two methods to rotate the list:
        - Method 1: Repeatedly moves the last element to the front until 'k' rotations are done.
        - Method 2: Uses list slicing to perform the rotation in a single step.

        Args:
            nums (list[int]): The list of integers to be rotated.
            k (int): The number of steps to rotate the list to the right.

        Returns:
            None: The function modifies the list 'nums' in-place and does not return a value.
        """

        # # METHOD 1: Iterative Rotation with Slicing
        # # Rotate the list by repeatedly moving the last element to the front.
        # # Time Complexity: O(k * n), where n is the length of the list.
        # # Space Complexity: O(n), where n is the length of the list due to temporary lists created during each iteration.

        # if len(nums) < 2:
        #     # If the list has fewer than 2 elements, no rotation is needed.
        #     return
        # while k > 0:
        #     # Move the last element to the front.
        #     nums[:] = nums[-1:] + nums[:-1]
        #     k -= 1

        # METHOD 2: Optimized Rotation with Slicing
        # Rotate the list by slicing it into two parts and reassembling them.
        # Time Complexity: O(n), where n is the length of the list.
        # Space Complexity: O(n) due to the creation of temporary lists for slicing and concatenation.

        # Normalize k to be within the bounds of the list length.
        k = k % len(nums)
        # Reassemble the list by slicing and concatenation.
        nums[:] = nums[-k:] + nums[:-k]

    def max_subarray(self, nums: list[int]) -> int:
        """
        Finds the sum of the maximum contiguous subarray using Kadane’s Algorithm in two methods.

        METHOD 1:
        This method calculates the maximum subarray sum by iterating through the list and maintaining a running sum.
        It handles edge cases by initializing `max_sum` to negative infinity and checking if the list is empty.

        METHOD 2:
        This method calculates the maximum subarray sum using a similar approach but initializes both `max_sum` and `current_sum`
        with the first element of the list, assuming the list is non-empty.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The sum of the maximum contiguous subarray.
        """

        # # METHOD 1
        # if len(nums) == 0:
        #     return 0  # Edge case: return 0 for empty input
        # # Initialize max_sum to the smallest possible value
        # max_sum = float('-inf')
        # current_sum = 0  # Initialize current_sum to 0
        # for num in nums:
        #     current_sum += num  # Add the current number to the running sum
        #     # Start a new subarray if the current number alone is larger
        #     current_sum = max(current_sum, num)
        #     # Update the max_sum if the current_sum is greater
        #     max_sum = max(current_sum, max_sum)
        # return max_sum

        # # Time Complexity: O(n) - Single pass through the list
        # # Space Complexity: O(1) - Only a few variables used

        # METHOD 2
        if len(nums) == 0:
            return 0  # Edge case: return 0 for empty input
        # Initialize both max_sum and current_sum with the first element
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum += nums[i]  # Add the current number to the running sum
            # Start a new subarray if the current number alone is larger
            current_sum = max(current_sum, nums[i])
            # Update the max_sum if the current_sum is greater
            max_sum = max(current_sum, max_sum)
        return max_sum

        # Time Complexity: O(n) - Single pass through the list
        # Space Complexity: O(1) - Only a few variables used


def main():
    solution = Solution()

    # Test remove_element
    print("\n==> Test remove_element()\n")
    nums = [3, 2, 2, 3, 4, 5, 3]
    val = 3
    print(f"\t. Original list: {nums}, Value: {val}")
    new_length = solution.remove_element(nums, val)
    print(f"\t. Modified list: {
          nums[:new_length]}, New length: {new_length}\n")
    print("-" * 60)

    # Test find_max_min
    print("\n==> Test find_max_min()\n")
    myList = [10, 2, 5, 8, 1]
    max_min = solution.find_max_min(myList)
    print(f"\t. List: {myList}")
    print(f"\t. Max and Min: {max_min}\n")
    print("-" * 60)

    # Test find_longest_string
    print("\n==> Test find_longest_string()\n")
    string_list = ["apple", "banana", "cherry", "date"]
    longest_string = solution.find_longest_string(string_list)
    print(f"\t. String list: {string_list}")
    print(f"\t. Longest string: {longest_string}\n")
    print("-" * 60)

    # Test remove_duplicates
    print("\n==> Test remove_duplicates()\n")
    sorted_nums = [1, 1, 2, 3, 3, 4, 5, 5]
    print(f"\t. Original list: {sorted_nums}")
    new_length_no_duplicates = solution.remove_duplicates(sorted_nums)
    print(f"\t. List without duplicates: {
          sorted_nums[:new_length_no_duplicates]}, New length: {new_length_no_duplicates}\n")
    print("-" * 60)

    # Test max_profit
    print("\n==> Test max_profit()\n")
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = solution.max_profit(prices)
    print(f"\t. Prices: {prices}")
    print(f"\t. Maximum profit: {max_profit}\n")
    print("-" * 60)

    # Test rotate
    print("\n==> Test rotate()\n")
    nums_to_rotate = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"\t. Original list: {nums_to_rotate}, K: {k}")
    solution.rotate(nums_to_rotate, k)
    print(f"\t. Rotated list by '{k}' steps: {nums_to_rotate}\n")
    print("-" * 60)

    # Test max_subarray
    print("\n==> Test max_subarray()\n")
    subarray_nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    max_subarray_sum = solution.max_subarray(subarray_nums)
    print(f"\t. List: {subarray_nums}")
    print(f"\t. Maximum subarray sum: {max_subarray_sum}\n")
    print("-" * 60)


if __name__ == "__main__":
    main()
