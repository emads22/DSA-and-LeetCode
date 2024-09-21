## 1. Kth Smallest Element in an Array (**Interview Question**)

### Given a list of numbers called `nums` and a number `k`. Write a function `find_kth_smallest(nums, k)` to find the kth smallest number in the list.

The list can contain duplicate numbers, and `k` is guaranteed to be within the range of the length of the list.

This function will take the following parameters:

- `nums`: A list of integers.
- `k`: An integer.

This function should return the kth smallest number in `nums`.

#### Example 1:

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_smallest(nums, k))  # Output: 2
```
- In the example above, the function should return 2. If we sort the list, it becomes [1, 2, 3, 4, 5, 6]. The 2nd smallest number is 2, so the function returns 2.

#### Example 2:

```python
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_smallest(nums, k))  # Output: 3
```
- In the example above, the function should return 3. If we sort the list, it becomes [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th smallest number is 3, so the function returns 3.

**Note**: 
- For the purpose of this problem, we assume that duplicate numbers are counted as separate numbers. For example, in the second example above, the two 2s are counted as the 2nd and 3rd smallest numbers, and the two 3s are counted as the 4th and 5th smallest numbers.

- Please write your solution in Python and use a max heap data structure to solve this problem.

- This is a separate function, not a method in the MaxHeap class.

-----------------------------------------------------------------------------------------



## 2. Maximum Element in a Stream (**Interview Question**)

### Write a function named `stream_max` that takes as its input a list of integers (`nums`). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.

More specifically, for each index `i` in the input list, the element at the same index in the output list should be the maximum value among the elements at indices `0` through `i` in the input list.

Use the provided `MaxHeap` class to solve this problem. You should not need to modify the `MaxHeap` class to complete this task.

**Example 1**:

- If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].

- Explanation:

   - At index 0, the maximum number seen so far is 1.
   - At index 1, the maximum number seen so far is 3.
   - At index 2, the maximum number seen so far is still 3.
   - At index 3, the maximum number seen so far is 5.
   - At index 4, the maximum number seen so far is still 5.
   - So, the output list is [1, 3, 3, 5, 5].

**Example 2**:

- If the input list is [7, 2, 4, 6, 1], the function should return [7, 7, 7, 7, 7].

- Explanation:

   - At each index, the maximum number seen so far is 7.
   - So, the output list is [7, 7, 7, 7, 7].

**Constraints**:
- You may assume that the input list does not contain any null or undefined elements.

-----------------------------------------------------------------------------------------
