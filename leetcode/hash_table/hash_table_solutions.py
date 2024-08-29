import sys
from pathlib import Path
from typing import TypeVar, Optional


# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))

# Define a generic type variable to represent any type for use in the stack class
ItemType = TypeVar('ItemType')


class Solution:
    """
    A class that provides solutions for various operations using a hash table.
    """

    def item_in_common(self, list1: list[ItemType], list2: list[ItemType]) -> bool:
        """
        Determines if there is any item in common between two lists.

        Args:
            list1 (list[ItemType]): The first list of items.
            list2 (list[ItemType]): The second list of items.

        Returns:
            bool: True if there is at least one common item between the lists, otherwise False.
        """
        ht = {}  # Hash table to store items from list1
        for item in list1:
            # Mark item as present in list1, O(n) where n is the length of list1
            ht[item] = True
        for item in list2:
            # Check if item from list2 is in the hash table, O(n) where n is the length of list2
            if item in ht:
                return True  # Common item found
        return False  # No common items found

    def find_duplicates(self, nums: list[ItemType]) -> list[ItemType]:
        """
        Finds and returns all duplicate items in a list.

        Args:
            nums (list[ItemType]): The list of items to check for duplicates.

        Returns:
            list[ItemType]: A list of duplicate items.
        """
        # Method 1: Using a hash table to count occurrences
        # Hash table to count occurrences of each item, O(n) where n is the length of nums
        ht = {}
        duplicates = []  # List to store duplicates
        for num in nums:
            # Increment count for each item, O(1) per item
            ht[num] = ht.get(num, 0) + 1
        for num, count in ht.items():
            # If an item appears more than once, it's a duplicate, O(n) where n is the number of unique items
            if count > 1:
                duplicates.append(num)
        return duplicates

        # # Method 2: Using a set to track duplicates (alternative approach)
        # ht = set()  # Set to track seen items, O(n) where n is the length of nums
        # duplicates = set()  # Set to store duplicates
        # for num in nums:
        #     # If the item has been seen before, it's a duplicate, O(1) per item
        #     if num in ht:
        #         duplicates.add(num)
        #     else:
        #         # Add item to set if it's seen for the first time, O(1) per item
        #         ht.add(num)
        # # Convert set of duplicates back to a list, O(n)
        # return list(duplicates)

    def first_non_repeating_char(self, string: str) -> Optional[str]:
        """
        Finds the first non-repeating character in a string.

        Args:
            string (str): The input string.

        Returns:
            Optional[str]: The first non-repeating character, or None if all characters repeat.
        """
        # Method 1: Using a hash table to count character occurrences
        # Hash table to count occurrences of each character, O(n) where n is the length of the string
        ht = {}
        for char in string:
            # Increment count for each character, O(1) per character
            ht[char] = ht.get(char, 0) + 1
        for char, count in ht.items():
            # Return the first character that occurs only once, O(n) where n is the number of unique characters
            if count == 1:
                return char
        return None  # All characters repeat

        # # Method 2: Check for non-repeating character in a second pass through the string
        # # Hash table to count occurrences of each character, O(n) where n is the length of the string
        # ht = {}
        # for char in string:
        #     # Increment count for each character, O(1) per character
        #     ht[char] = ht.get(char, 0) + 1
        # # Second pass to find the first non-repeating character, O(n)
        # for char in string:
        #     if ht[char] == 1:
        #         return char  # Return the first non-repeating character
        # return None  # All characters repeat

    def group_anagrams(self, strings: list[str]) -> list:
        """
        Groups a list of strings into anagrams.

        Args:
            strings (list[str]): The list of strings to group.

        Returns:
            list: A list of groups, where each group contains anagrams.
        """
        # Method 1: Group by frequency of characters
        # Hash table to group anagrams by frequency, O(n * m) where n is the number of strings and m is the length of each string
        ht = {}

        def frequency(word: str) -> str:
            """
            Creates a frequency representation of the given word.
            """
            alphabet_frequency = [
                '0'] * 26  # Initialize frequency array for 26 letters, O(1)
            for char in word.lower():
                # Find index of the character in the alphabet, O(1)
                idx = ord(char) - ord('a')
                # Mark the character as present, O(1)
                alphabet_frequency[idx] = '1'
            f = "".join(alphabet_frequency)  # Convert list to string, O(1)
            return f

        for word in strings:
            # Get frequency representation of the word, O(m) where m is the length of the word
            f = frequency(word)
            if f in ht:
                # Add the word to the existing group of anagrams, O(1)
                ht[f].append(word)
            else:
                ht[f] = [word]  # Create a new group for this anagram, O(1)
        # Return the grouped anagrams as a list of lists, O(n)
        return list(ht.values())

        # # Method 2: Group by sorted string
        # # Hash table to group anagrams by sorted string, O(n * m log m) where n is the number of strings and m is the length of each string
        # ht = {}
        # for word in strings:
        #     # Sort each word to find its anagram group, O(m log m) where m is the length of the word
        #     sorting = "".join(sorted(word))
        #     if sorting in ht:
        #         # Add the word to the existing group of anagrams, O(1)
        #         ht[sorting].append(word)
        #     else:
        #         # Create a new group for this anagram, O(1)
        #         ht[sorting] = [word]
        # # Return the grouped anagrams as a list of lists, O(n)
        # return list(ht.values())

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in the list that add up to the target and returns their indices.

        Args:
            nums (list[int]): The list of integers.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the indices of the two numbers that add up to the target.
        """
        num_idx = {}  # Hash table to store the indices of numbers
        for idx, num in enumerate(nums):
            # Check if the complement that would sum to the target is already in the hash table
            if (target - num) in num_idx:
                # Return indices of the two numbers
                return [num_idx[target - num], idx]
            # Store the index of the current number in the hash table
            num_idx[num] = idx
        return []  # Return an empty list if no solution is found

    def subarray_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds a continuous subarray that sums to the target and returns the start and end indices.

        Args:
            nums (list[int]): The list of integers.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the start and end indices of the subarray that sums to the target.
        """
        sum_idx = {0: -1}  # Hash table to store cumulative sums and their indices
        sum = 0  # Initialize cumulative sum
        for idx, num in enumerate(nums):
            sum += num  # Update cumulative sum
            # Check if the difference needed for the target sum has been seen before
            if (sum - target) in sum_idx:
                # Calculate the start index of the subarray
                start_idx = sum_idx[sum - target] + 1
                return [start_idx, idx]  # Return start and end indices
            # Store the current cumulative sum and its index
            sum_idx[sum] = idx
        return []  # Return an empty list if no subarray is found

    def remove_duplicates(self, my_list: list[int]) -> list[int]:
        """
        Removes duplicate elements from a list and returns a list of unique elements.

        Args:
            my_list (list[int]): The list of integers with potential duplicates.

        Returns:
            list[int]: A list of unique integers.
        """
        # # METHOD 1: Using a set to keep track of unique elements
        # uniques = set()  # Initialize an empty set to store unique elements
        # for num in my_list:
        #     # Add each element to the set, duplicates are automatically handled
        #     uniques.add(num)
        # return list(uniques)  # Convert the set back to a list and return

        # METHOD 2: Directly converting the list to a set and back to a list
        # Convert list to a set to remove duplicates and back to a list
        return list(set(my_list))

    def has_unique_chars(self, string: str) -> bool:
        """
        Determines if a string has all unique characters.

        Args:
            string (str): The input string to check.

        Returns:
            bool: True if all characters in the string are unique, otherwise False.
        """
        # METHOD 1: Compare the length of the string with the length of the set of characters
        return len(string) == len(set(string))

        # # METHOD 2: Use a set to track characters and check for duplicates
        # uniques = set()  # Initialize an empty set to store unique characters
        # for char in string:
        #     if char in uniques:  # If the character is already in the set, return False
        #         return False
        #     uniques.add(char)  # Add the character to the set
        # return True  # If no duplicates are found, return True

    def find_pairs(self, arr1: list[int], arr2: list[int], target: int) -> list[tuple[int, int]]:
        """
        Finds all pairs of numbers, one from each of the two lists, that add up to the target.

        Args:
            arr1 (list[int]): The first list of integers.
            arr2 (list[int]): The second list of integers.
            target (int): The target sum.

        Returns:
            list[tuple[int, int]]: A list of tuples, each containing a pair of integers that add up to the target.
        """
        arr1 = set(arr1)  # Convert the first list to a set
        pairs = []  # List to store the pairs that sum to the target
        for num in arr2:
            # Calculate the complement that would sum with num to reach the target
            complement = target - num
            if complement in arr1:  # Check if the complement exists in the set
                # If so, add the pair to the list
                pairs.append((complement, num))
        return pairs  # Return the list of pairs

    def longest_consecutive_sequence(self, nums: list[int]) -> int:
        """
        Finds the length of the longest consecutive sequence in a list of integers.

        Args:
            nums (list[int]): The list of integers.

        Returns:
            int: The length of the longest consecutive sequence.
        """

        # METHOD 1: O(n^2)
        # nums_set = set(nums)  # Convert the list to a set for O(1) lookups
        # max_count = 0  # Variable to store the maximum length of consecutive sequences
        # for num in nums_set:
        #     temp = num - 1  # Start checking from the previous number
        #     count = 1  # Initialize the count for the current sequence
        #     # Continue checking for consecutive smaller numbers
        #     while temp in nums_set:
        #         count += 1
        #         temp -= 1  # Move to the next previous number
        #     max_count = max(max_count, count)  # Update max_count if the current sequence is longer
        # # This method has O(n^2) complexity due to potential redundant processing of elements
        # return max_count

        # Time Complexity Explanation for Method 1:
        # - The outer loop runs O(n) times for each element in the set.
        # - The while loop can run O(n) times in the worst case if a sequence spans all elements.
        # - This leads to a total time complexity of O(n^2) due to redundant counting in overlapping sequences.

        # METHOD 2: O(n)
        nums_set = set(nums)  # Convert the list to a set for O(1) lookups
        max_count = 0  # Variable to store the maximum length of consecutive sequences
        for num in nums_set:
            # Only start counting if `num` is the start of a sequence
            if (num - 1) not in nums_set:
                temp = num + 1  # Start checking from the next number
                count = 1  # Initialize the count for the current sequence
                # Continue checking for consecutive larger numbers
                while temp in nums_set:
                    count += 1
                    temp += 1  # Move to the next following number
                # Update max_count if the current sequence is longer
                max_count = max(max_count, count)
        # This method has O(n) complexity because each number is processed only once
        return max_count

        # Time Complexity Explanation for Method 2:
        # - The outer loop runs O(n) times, once for each element.
        # - The if-condition ensures the while loop only runs for the start of sequences, preventing redundant work.
        # - This results in an overall time complexity of O(n), as each element is processed only once.
