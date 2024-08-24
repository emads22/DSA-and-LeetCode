## 1. Item In Common (**Interview Question**)  

### Write a function `item_in_common(list1, list2)` that takes two lists as input and returns `True` if there is at least one common item between the two lists, `False` otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.

-----------------------------------------------------------------------------------------



## 2. Find Duplicates (**Interview Question**)

### Given an array of integers `nums`, implement a function `find_duplicates()` to find all the duplicates in the array using a hash table (dictionary).

**Input:**  
A list of integers `nums`.

**Output:**  
A list of integers representing the numbers in the input array `nums` that appear more than once. If no duplicates are found in the input array, return an empty list `[]`.

**Examples:**

- Input: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`  
  Output: `[2, 3]`  
  Explanation: The numbers 2 and 3 appear more than once in the input array.
  
- Input: `nums = [1, 2, 3, 4, 5]`  
  Output: `[]`  
  Explanation: There are no duplicates in the input array, so the function returns an empty list `[]`.
  
- Input: `nums = [3, 3, 3, 3, 3]`  
  Output: `[3]`  
  Explanation: The number 3 appears more than once in the input array.
  
- Input: `nums = [-1, 0, 1, 0, -1, -1, 2, 2]`  
  Output: `[-1, 0, 2]`  
  Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
  
- Input: `nums = []`  
  Output: `[]`  
  Explanation: There are no numbers in the input array, so the function returns an empty list `[]`.

-----------------------------------------------------------------------------------------



## 3. First Non-Repeating Character (**Interview Question**)

### Given a string of lowercase letters, write a function called `first_non_repeating_char(string)` that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return `None`.

**Examples:**

- If the input string is `"leetcode"`, the function should return `"l"` because `"l"` is the first character that appears only once in the string.
- If the input string is `"hello"`, the function should return `"h"` because `"h"` is the first non-repeating character in the string.

-----------------------------------------------------------------------------------------



## 4. Group Anagrams (**Interview Question**)

### Given an array of strings, where each string may contain only lowercase English letters. Write a function `group_anagrams(strings)` that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

**Example:**

- If the input array is `["eat", "tea", "tan", "ate", "nat", "bat"]`, the function should return `[["eat","tea","ate"],["tan","nat"],["bat"]]` because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the `group_anagrams(strings)` function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.

-----------------------------------------------------------------------------------------



## 5. Two Sum (**Interview Question**)

### Given an array of integers `nums` and a target integer `target`, implement the function `two_sum()` that finds the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in `nums`.

**Input:**

- A list of integers `nums`.
- A target integer `target`.

**Output:**

- A list of two integers representing the indices of the two numbers in the input array `nums` that add up to the target. If no two numbers in the input array add up to the target, return an empty list `[]`.

**Examples:**

- Input: `nums = [5, 1, 7, 2, 9, 3]`, `target = 10`  
  Output: `[1, 4]`  
  Explanation: The numbers at indices 1 and 4 in the array add up to the target 10.
  
- Input: `nums = [3, 2, 4]`, `target = 6`  
  Output: `[1, 2]`  
  Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.
  
- Input: `nums = [3, 3]`, `target = 6`  
  Output: `[0, 1]`  
  Explanation: The numbers at indices 0 and 1 in the array add up to the target 6.
  
- Input: `nums = [2, 1, 2, 7, 11, 15]`, `target = 9`  
  Output: `[2, 3]`  
  Explanation: Notice there are two 2s in the array. The second one will be used.
  
- Input: `nums = [1, 2, 3, 4, 5]`, `target = 10`  
  Output: `[]`  
  Explanation: There are no two numbers in the array that add up to the target 10.
  
- Input: `nums = []`, `target = 0`  
  Output: `[]`  
  Explanation: There are no numbers in the input array, so the function returns an empty list `[]`.

-----------------------------------------------------------------------------------------



## 6. Subarray Sum (**Interview Question**)  

### Given an array of integers `nums` and a target integer `target`, write a Python function called `subarray_sum` that finds the indices of a contiguous subarray in `nums` that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

- `nums`: a list of integers representing the input array.
- `target`: an integer representing the target sum.

Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

**Example:**

- `nums = [1, 2, 3, 4, 5]`  
  `target = 9`  
  `print(subarray_sum(nums, target))`  # should print `[1, 3]`

Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.

-----------------------------------------------------------------------------------------



## 7. Set: Remove Duplicates (**Interview Question**) 

### Given a list `my_list` with some duplicate values. Implement a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function `remove_duplicates(my_list)` that takes in the input list `my_list` as a parameter and returns a new list with no duplicates.

Your function should not modify the original list; instead, it should create a new list with unique values and return it.

**Example:**

- Input:  
  `my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]`
  
- Output:  
  `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

**Note:**

The order of the elements in the updated list may be different from the original list, as sets are unordered.

-----------------------------------------------------------------------------------------



## 8. Set: Has Unique Chars (**Interview Question**) 

### Write a function called `has_unique_chars` that takes a string as input and returns `True` if all the characters in the string are unique, and `False` otherwise.

**Example:**

- `has_unique_chars('abcdefg')` should return `True`.
- `has_unique_chars('hello')` should return `False`.

-----------------------------------------------------------------------------------------



## 9. Set: Find Pairs (**Interview Question**)  

### Write a function called `find_pairs` that takes in three arguments: `arr1`, `arr2`, and `target` (two lists of integers, and a target integer value), and returns a list of all pairs of numbers (one from `arr1` and one from `arr2`) whose sum equals the target. Assume that each array does not contain duplicate values.

**Input:**

Your function should take in the following inputs:

- `arr1`: a list of integers
- `arr2`: a list of integers
- `target`: an integer

**Output:**

Your function should return a list of tuples, where each tuple contains two integers from `arr1` and `arr2` that add up to the target.

**Examples:**

- Example 1:
  - `arr1 = [1, 2, 3]`
  - `arr2 = [4, 5, 6]`
  - `target = 9`
  - `pairs = find_pairs(arr1, arr2, target)`
  - Expected output: `[(3, 6)]`
  - Explanation: There's only one pair that adds up to 9: 3 from `arr1` and 6 from `arr2`.

- Example 2:
  - `arr1 = [0, 1, 2]`
  - `arr2 = [7, 8, 9]`
  - `target = 10`
  - `pairs = find_pairs(arr1, arr2, target)`
  - Expected output: `[(1, 9), (2, 8)]`
  - Explanation: The pairs that add up to 10 are (1, 9) and (2, 8).

- Example 3:
  - `arr1 = [1, 2, 3, 5]`
  - `arr2 = [1, 3, 4, 5]`
  - `target = 6`
  - `pairs = find_pairs(arr1, arr2, target)`
  - Expected output: `[(5, 1), (3, 3), (2, 4), (1, 5)]`
  - Explanation: The pairs that add up to 6 are (5, 1), (3, 3), (2, 4), and (1, 5). Each pair consists of one element from `arr1` and one element from `arr2` that together sum to the target value.

- Example 4:
  - `arr1 = [1, 2, 3, 5]`
  - `arr2 = [1, 3, 4, 5]`
  - `target = 11`
  - `pairs = find_pairs(arr1, arr2, target)`
  - Expected output: `[]`
  - Explanation: There are no pairs in `arr1` and `arr2` that add up to 11.

-----------------------------------------------------------------------------------------



## 10. Set: Longest Consecutive Sequence (**Interview Question**)

### Given an unsorted array of integers, write a function that finds the length of the `longest_consecutive_sequence` (i.e., a sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

**Input:**  
An unsorted array of integers, `nums`.

**Output:**  
An integer representing the length of the longest consecutive sequence in `nums`.

**Example:**

- Input: `nums = [100, 4, 200, 1, 3, 2]`
- Output: `4`
- Explanation: The longest consecutive sequence in the input array is `[4, 3, 2, 1]`, and its length is 4.

-----------------------------------------------------------------------------------------
