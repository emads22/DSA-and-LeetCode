# 1. Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with O(1) extra memory.

## Example 1:
- **Input**: `s = ["h", "e", "l", "l", "o"]`
- **Output**: `["o", "l", "l", "e", "h"]`

## Example 2:
- **Input**: `s = ["H", "a", "n", "n", "a", "h"]`
- **Output**: `["h", "a", "n", "n", "a", "H"]`

## Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

--------------------------------------------------------------------------------

# 2. Fizz Buzz

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

## Example 1:
- **Input**: `n = 3`
- **Output**: `["1", "2", "Fizz"]`

## Example 2:
- **Input**: `n = 5`
- **Output**: `["1", "2", "Fizz", "4", "Buzz"]`

## Example 3:
- **Input**: `n = 15`
- **Output**: `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`

## Constraints:
- `1 <= n <= 10^4`

--------------------------------------------------------------------------------

# 3. Single Number

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a **linear runtime complexity** and use only **constant extra space**.

## Example 1:
- **Input**: `nums = [2, 2, 1]`
- **Output**: `1`

## Example 2:
- **Input**: `nums = [4, 1, 2, 1, 2]`
- **Output**: `4`

## Example 3:
- **Input**: `nums = [1]`
- **Output**: `1`

## Constraints:
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

## Example 1:
- **Input**: `root = [3, 9, 20, null, null, 15, 7]`
- **Output**: `3`

## Example 2:
- **Input**: `root = [1, null, 2]`
- **Output**: `2`

## Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

--------------------------------------------------------------------------------

# 5. Move Zeroes

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Note**: You must do this **in-place** without making a copy of the array.

## Example 1:
- **Input**: `nums = [0, 1, 0, 3, 12]`
- **Output**: `[1, 3, 12, 0, 0]`

## Example 2:
- **Input**: `nums = [0]`
- **Output**: `[0]`

## Constraints:
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Follow up:
Could you minimize the total number of operations done?

--------------------------------------------------------------------------------

# 6. Sum of Two Integers

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

## Example 1:
- **Input**: `a = 1`, `b = 2`
- **Output**: `3`

## Example 2:
- **Input**: `a = 2`, `b = 3`
- **Output**: `5`

## Constraints:
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

## Example 1:
- **Input:** `root = [1,null,2,3]`  
- **Output:** `[1,3,2]`  

## Example 2:
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`  
- **Output:** `[4,2,6,5,7,1,3,9,8]`  

## Example 3:
- **Input:** `root = []`  
- **Output:** `[]`  

## Example 4:
- **Input:** `root = [1]`  
- **Output:** `[1]`  

## Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** 
- Recursive solution is trivial; could you do it iteratively?

--------------------------------------------------------------------------------
