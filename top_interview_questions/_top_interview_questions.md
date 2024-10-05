# 1. Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with O(1) extra memory.

### Example 1:
- **Input**: `s = ["h", "e", "l", "l", "o"]`
- **Output**: `["o", "l", "l", "e", "h"]`

### Example 2:
- **Input**: `s = ["H", "a", "n", "n", "a", "h"]`
- **Output**: `["h", "a", "n", "n", "a", "H"]`

### Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

--------------------------------------------------------------------------------

# 2. Fizz Buzz

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### Example 1:
- **Input**: `n = 3`
- **Output**: `["1", "2", "Fizz"]`

### Example 2:
- **Input**: `n = 5`
- **Output**: `["1", "2", "Fizz", "4", "Buzz"]`

### Example 3:
- **Input**: `n = 15`
- **Output**: `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`

### Constraints:
- `1 <= n <= 10^4`

--------------------------------------------------------------------------------

# 3. Single Number

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a **linear runtime complexity** and use only **constant extra space**.

### Example 1:
- **Input**: `nums = [2, 2, 1]`
- **Output**: `1`

### Example 2:
- **Input**: `nums = [4, 1, 2, 1, 2]`
- **Output**: `4`

### Example 3:
- **Input**: `nums = [1]`
- **Output**: `1`

### Constraints:
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

--------------------------------------------------------------------------------

# 4. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```markdown
  3
 / \
9  20 
   / \
  15  7
```

### Example 1:
- **Input**: `root = [3, 9, 20, null, null, 15, 7]`
- **Output**: `3`

### Example 2:
- **Input**: `root = [1, null, 2]`
- **Output**: `2`

### Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

--------------------------------------------------------------------------------

# 5. Move Zeroes

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Note**: You must do this **in-place** without making a copy of the array.

### Example 1:
- **Input**: `nums = [0, 1, 0, 3, 12]`
- **Output**: `[1, 3, 12, 0, 0]`

### Example 2:
- **Input**: `nums = [0]`
- **Output**: `[0]`

### Constraints:
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

### Follow up:
Could you minimize the total number of operations done?

--------------------------------------------------------------------------------

# 6. Sum of Two Integers

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

### Example 1:
- **Input**: `a = 1`, `b = 2`
- **Output**: `3`

### Example 2:
- **Input**: `a = 2`, `b = 3`
- **Output**: `5`

### Constraints:
- `-1000 <= a, b <= 1000`

--------------------------------------------------------------------------------

# 7. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

### Example 1:
- **Input:** head = [1,2,3,4,5]  
- **Output:** [5,4,3,2,1]

### Example 2:
- **Input:** head = [1,2]  
- **Output:** [2,1]

### Example 3:
- **Input:** head = []  
- **Output:** []

### Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

### Follow up: 
- A linked list can be reversed either iteratively or recursively. Could you implement both?

--------------------------------------------------------------------------------

# 8. Delete Node in a Linked List

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will not be given access to the first node of `head`.

All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before `node` should be in the same order.
- All the values after `node` should be in the same order.

### Custom testing:

For the input, you should provide the entire linked list `head` and the node to be given `node`. `node` should not be the last node of the list and should be an actual node in the list. We will build the linked list and pass the node to your function. The output will be the entire list after calling your function.

### Example 1:
- **Input:** head = [4,5,1,9], node = 5  
- **Output:** [4,1,9]  
  **Explanation:** You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

### Example 2:
- **Input:** head = [4,5,1,9], node = 1  
- **Output:** [4,5,9]  
  **Explanation:** You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

### Constraints:
- The number of the nodes in the given list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node.

--------------------------------------------------------------------------------

# 9. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Example 1:
- **Input:** `root = [1,null,2,3]`  
- **Output:** `[1,3,2]`  

### Example 2:
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`  
- **Output:** `[4,2,6,5,7,1,3,9,8]`  

### Example 3:
- **Input:** `root = []`  
- **Output:** `[]`  

### Example 4:
- **Input:** `root = [1]`  
- **Output:** `[1]`  

### Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** 
- Recursive solution is trivial; could you do it iteratively?

--------------------------------------------------------------------------------

# 10. Excel Sheet Column Number

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

- A -> 1
- B -> 2
- C -> 3
- ...
- Z -> 26
- AA -> 27
- AB -> 28
- ...

### Example 1:
- **Input:** `columnTitle = "A"`  
- **Output:** `1`

### Example 2:
- **Input:** `columnTitle = "AB"`  
- **Output:** `28`

### Example 3:
- **Input:** `columnTitle = "ZY"`  
- **Output:** `701`

### Constraints:
- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is in the range ["A", "FXSHRXW"].

--------------------------------------------------------------------------------

# 11. Reverse Bits

Reverse the bits of a given 32-bit unsigned integer.

## Note:
In some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. This should not affect your implementation, as the integer's internal binary representation is the same, whether signed or unsigned.

- In Java, the compiler uses 2's complement notation for signed integers. Therefore, for example:
  - Input: `-3` (signed integer)
  - Output: `-1073741825` (signed integer)

### Example 1:
- **Input:** `n = 00000010100101000001111010011100`  
- **Output:** `964176192` (Binary: `00111001011110000010100101000000`)  
- **Explanation:** The input binary string represents the unsigned integer `43261596`, which is reversed to give `964176192`.

### Example 2:
- **Input:** `n = 11111111111111111111111111111101`  
- **Output:** `3221225471` (Binary: `10111111111111111111111111111111`)  
- **Explanation:** The input binary string represents the unsigned integer `4294967293`, which is reversed to give `3221225471`.

### Constraints:
- The input must be a binary string of length 32.

### Follow-up:
How would you optimize the function if it is called many times?

--------------------------------------------------------------------------------

# 12. Reverse Integer

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [(-2)^31, 2^31 - 1], then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Example 1:
- **Input:** `x = 123`  
- **Output:** `321`

### Example 2:
- **Input:** `x = -123`  
- **Output:** `-321`

### Example 3:
- **Input:** `x = 120`  
- **Output:** `21`

### Constraints:
- ((-2)^31) <= x <= (2^31 - 1)

--------------------------------------------------------------------------------

# 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example:
- 2 is written as **II** in Roman numeral (I + I).
- 12 is written as **XII** (X + II).
- 27 is written as **XXVII** (XX + V + II).

Roman numerals are usually written from largest to smallest from left to right. However, there are exceptions for specific numbers:
- The numeral for four is not **IIII** but **IV** (5 - 1).
- The numeral for nine is **IX** (10 - 1).
- There are six instances where subtraction is used:
  - **I** can be placed before **V** (5) and **X** (10) to make 4 and 9.
  - **X** can be placed before **L** (50) and **C** (100) to make 40 and 90.
  - **C** can be placed before **D** (500) and **M** (1000) to make 400 and 900.

Given a Roman numeral, convert it to an integer.

### Example 1:
- **Input:** `s = "III"`  
- **Output:** `3`  
- **Explanation:** III = 3.

### Example 2:
- **Input:** `s = "LVIII"`  
- **Output:** `58`  
- **Explanation:** L = 50, V = 5, III = 3.

### Example 3:
- **Input:** `s = "MCMXCIV"`  
- **Output:** `1994`  
- **Explanation:** M = 1000, CM = 900, XC = 90, and IV = 4.

### Constraints:
- 1 <= s.length <= 15
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999].

--------------------------------------------------------------------------------

# 14. Rotate Array

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1:
- **Input:**  `nums = [1,2,3,4,5,6,7]`, `k = 3`  
- **Output:**  `[5,6,7,1,2,3,4]`  
- **Explanation:**  
    - Rotate 1 step to the right: `[7,1,2,3,4,5,6]`  
    - Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`  
    - Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

### Example 2:
- **Input:**  `nums = [-1,-100,3,99]`, `k = 2`  
- **Output:**  `[3,99,-1,-100]`  
- **Explanation:**  
    - Rotate 1 step to the right: `[99,-1,-100,3]`  
    - Rotate 2 steps to the right: `[3,99,-1,-100]`

### Constraints:
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

### Follow-up:
- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem. 
- Could you do it in-place with O(1) extra space?

--------------------------------------------------------------------------------

# Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:

- **Input:**  `nums = [2,7,11,15]`, `target = 9`  
- **Output:**  `[0,1]`  
- **Explanation:**  
    - Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2:

- **Input:**  `nums = [3,2,4]`, `target = 6`  
- **Output:**  `[1,2]`

### Example 3:

- **Input:**  `nums = [3,3]`, `target = 6`  
- **Output:**  `[0,1]`

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

### Follow-up:
- Can you come up with an algorithm that is less than O(n²) time complexity?

--------------------------------------------------------------------------------

# Merge Two Sorted Lists

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1:

- **Input:**  `list1 = [1,2,4]`, `list2 = [1,3,4]`  
- **Output:**  `[1,1,2,3,4,4]`

### Example 2:

- **Input:**  `list1 = []`, `list2 = []`  
- **Output:**  `[]`

### Example 3:

- **Input:**  `list1 = []`, `list2 = [0]`  
- **Output:**  `[0]`

### Constraints:
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

--------------------------------------------------------------------------------
