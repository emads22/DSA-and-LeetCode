from typing import Optional

# import sys
# from pathlib import Path

# # Get the absolute path of the main_project directory
# main_project_path = Path(__file__).resolve().parent.parent.parent

# # Add the main_project directory to sys.path
# sys.path.append(str(main_project_path))

# # Alternatively: sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# from data_structures import LinkedList, Node_LL


class Solution:
    """
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

        # METHOD 1: Two-pointer approach
        if len(nums) == 0:
            return 0
        i, j = 0, 1  # Initialize two pointers
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1  # Move the second pointer forward if the current element is a duplicate
            else:
                i += 1  # Move the first pointer to the next unique element position
                # Swap the current element with the next unique position
                nums[i], nums[j] = nums[j], nums[i]
                j += 1  # Move the second pointer forward
        return i + 1  # Return the length of the list with unique elements

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
