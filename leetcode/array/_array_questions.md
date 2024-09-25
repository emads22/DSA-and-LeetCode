## 1. Reverse a String (**Interview Question**)

### Implement the `reverse_string` function in Python that takes a string as input and returns the string reversed. 

**Note**: You should not use Python's built-in string reversal methods like `[::-1]`.

#### Requirements:
- The function should iterate through the input string, reversing it without using Python's built-in string slicing.
- The function should handle edge cases like empty strings or strings with a single character.

#### Examples:
```python
def reverse_string(string: str) -> str:
    pass

# Example 1:
input_string = "hello"
print(reverse_string(input_string))  # Output: "olleh"

# Example 2:
input_string = "Python"
print(reverse_string(input_string))  # Output: "nohtyP"

# Example 3:
input_string = "a"
print(reverse_string(input_string))  # Output: "a"

# Example 4:
input_string = ""
print(reverse_string(input_string))  # Output: ""
```
-----------------------------------------------------------------------------------------



## 2. Merge Two Sorted Arrays (**Interview Question**)

### Implement the `merge_sorted_arrays` function in Python that takes two sorted arrays as input and returns a new array that contains all the elements from both arrays, merged in sorted order.

#### Requirements:
- The function should merge the arrays without using Python’s built-in sorting functions.
- The function should handle arrays of different lengths.
- The merged array should be sorted in non-decreasing order.

#### Examples:
```python
def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    pass

# Example 1:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

# Example 2:
arr1 = [1, 2, 7]
arr2 = [3, 4, 5]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 7]

# Example 3:
arr1 = [5, 10]
arr2 = [2, 8, 12]
print(merge_sorted_arrays(arr1, arr2))  # Output: [2, 5, 8, 10, 12]

# Example 4:
arr1 = []
arr2 = [1, 2, 3]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3]
```

-----------------------------------------------------------------------------------------



## 3. Max Sub Array (**Interview Question**)

### Given an array of integers `nums`, write a function `max_subarray(nums)` that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

**Remember to also account for an array with 0 items.**

#### Input:
- A list of integers nums.

#### Output:
- An integer representing the sum of the contiguous subarray with the largest sum.

#### Examples:
```python
def max_subarray(nums):
    pass

#Example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  #Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#Example 2:
nums = [1]
print(max_subarray(nums))  #Output: 1
# Explanation: The subarray [1] has the largest sum 1.

#Example 3:
nums = [5,4,-1,7,8]
print(max_subarray(nums))  #Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

-----------------------------------------------------------------------------------------



## 4. Rotate (**Interview Question**)

### Given a list of `n` integers and a non-negative integer `k`. Write a function called `rotate` that takes the list of integers and an integer `k` as input and rotates the list to the right by `k` steps.

The function should modify the input list in-place, and you should not return anything.

### Constraints:

- Each element of the input list is an integer.
- The integer `k` is non-negative.

### Example:

```python
def rotate(nums, k):
    # Implementation goes here
    pass

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
# Explanation: The list has been rotated to the right by 3 steps:

# 1. [7, 1, 2, 3, 4, 5, 6]
# 2. [6, 7, 1, 2, 3, 4, 5]
# 3. [5, 6, 7, 1, 2, 3, 4]
```

-----------------------------------------------------------------------------------------



## 5. Move Zeros (**Interview Question**)

### Given an integer array `nums`, implement the `move_zeros` function in Python to move all 0's to the end of the array while maintaining the relative order of the non-zero elements. 

**Note**: you must do this in-place without making a copy of the array.

#### Requirements:
- The function should modify the array in-place.
- The order of non-zero elements should be preserved.
- The function should not use extra space for a new array.

#### Examples:

```python
def move_zeros(nums: list[int]) -> None:
    pass

# Example 1:
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Example 2:
nums = [0]
move_zeros(nums)
print(nums)  # Output: [0]

# Example 3:
nums = [0, 0, 1, 2, 3]
move_zeros(nums)
print(nums)  # Output: [1, 2, 3, 0, 0]

# Example 4:
nums = [4, 5, 0, 0, 6]
move_zeros(nums)
print(nums)  # Output: [4, 5, 6, 0, 0]

```

-----------------------------------------------------------------------------------------



## 6. Longest Word (**Interview Question**)

### Write a Python function called `longest_word(sentence)` that takes a string parameter `sentence` and returns the longest word in the string. 


### Constraints
- If there are two or more words of the same length, return the first word from the string with that length.
- Ignore punctuation and assume `sentence` will not be empty. 
- Words may also contain numbers.

### Examples:

```python
import re

def longest_word(sentence: str) -> str:
    pass

# Example 1:
sentence = "fun&!! time"
print(longest_word(sentence))  # expected output: 'time'

# Example 2:
sentence = "I love dogs"
print(longest_word(sentence))  # expected output: 'love'
```

-----------------------------------------------------------------------------------------



## 7. Pattern Matching (**Interview Question**)

### Given a string `text` and a pattern `pattern`, implement a function `pattern_matching()` to find all occurrences of the pattern in the string.

**Input:**  
A string `text` and a string `pattern`.

**Output:**  
A list of indices where the pattern is found in the text. If the pattern is not found, return an empty list `[]`.

**Examples:**

- Input: `text = "THIS IS A TEST TEXT"`, `pattern = "TEST"`  
  Output: `[10]`  
  Explanation: The pattern "TEST" is found starting at index 10.

- Input: `text = "AABAACAADAABAABA"`, `pattern = "AABA"`  
  Output: `[0, 9, 12]`  
  Explanation: The pattern "AABA" is found starting at indices 0, 9, and 12.

-----------------------------------------------------------------------------------------



## 8. Remove Element (**Interview Question**)

### Given a list of integers `nums` and an integer `val`, write a function `remove_element()` that removes all occurrences of `val` in the list in-place and returns the new length of the modified list.

The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.

### Input:

- A list of integers `nums`.
- An integer `val` representing the value to be removed from the list.

### Output:

- An integer representing the new length of the modified list after removing all occurrences of `val`.

### Constraints:

- Do not use any built-in list methods, except for `pop()` to remove elements.
- It is okay to have extra space at the end of the modified list after removing elements.

----------------------------------------------------------------------------------------- 



## 9. Find Max Min (**Interview Question**)

### Write a Python function `find_max_min()` that takes a list of integers `myList` as input and returns a tuple containing the maximum and minimum values in the list.

The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

### Example:
- For the input list [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.

----------------------------------------------------------------------------------------- 



## 10. Find Longest String (**Interview Question**)

### Write a Python function called `find_longest_string` that takes a list of strings as input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.

### Example:

```python
def find_longest_string(string_list):
    # Implementation goes here
    pass

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'
```

-----------------------------------------------------------------------------------------



## 11. Remove Duplicates (**Interview Question**)

### Given a sorted list of integers `nums`, write a funvtion `remove_duplicates()` to rearrange the list in-place such that all unique elements appear at the beginning of the list.

Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any additional data structures to solve this problem. The original list should be modified in-place.

### Constraints:

- The input list is sorted in non-decreasing order.
- The input list may contain duplicates.
- The function should have a time complexity of O(n), where n is the length of the input list.
- The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists (this also means you cannot use a set).

### Example:

```python
def remove_duplicates(nums):
    # Implementation goes here
    pass

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])
```

### Expected Output:

```python
New length: 5
Unique values in list: [0, 1, 2, 3, 4]
```

### Explanation:
The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].

-----------------------------------------------------------------------------------------



## 12. Max Profit (**Interview Question**)

### You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day. You are allowed to buy one share of the stock on one day and sell it on a later day.

### Task:
Write a function called `max_profit` that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

- Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

### Constraints:
- Each element of the input list is a positive integer representing the stock price for a specific day.

### Example:
```python
def max_profit(prices):
    # Implementation goes here
    pass

prices = [7, 1, 5, 3, 6, 4]    # Input
profit = max_profit(prices)    # Function Call
profit = 5                     # Output
```

### Explanation:
The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.

-----------------------------------------------------------------------------------------

