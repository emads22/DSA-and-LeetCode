## 1. Find Middle Node (**Interview Question**)

### Implement the `find_middle_node` method for the `LinkedList` class

**Note:** This `LinkedList` implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

#### Requirements:
- The method should use a two-pointer approach, where one pointer (`slow`) moves one node at a time and the other pointer (`fast`) moves two nodes at a time.
- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
- The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
- The method should only traverse the linked list once. In other words, you can only use one loop.

-----------------------------------------------------------------------------------------



## 2. Has Loop (**Interview Question**) 

### Write a method called `has_loop` that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

You are required to use **Floyd's cycle-finding algorithm** (also known as the "tortoise and the hare" algorithm) to detect the loop.

This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

The method should follow these guidelines:

1. **Create two pointers, slow and fast**, both initially pointing to the head of the linked list.

2. **Traverse the list** with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

3. **Check for a loop**:
   - If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return `True`.
   - If the fast pointer reaches the end of the list or encounters a `None` value, it means there is no loop in the list. In this case, the method should return `False`.

**Note:** If your Linked List contains a loop, it indicates a flaw in its implementation.

-----------------------------------------------------------------------------------------



## 3. Find Kth Node From End (**Interview Question**) 

### Implement the `find_kth_from_end` function, which takes the `LinkedList` (ll) and an integer `k` as input, and returns the k-th node from the end of the linked list **without using the length**.

- Given this LinkedList:

```
1 -> 2 -> 3 -> 4
```

- If `k=1`, then return the first node from the end (the last node), which contains the value of `4`.
- If `k=2`, then return the second node from the end, which contains the value of `3`, etc.
- If the index is out of bounds, the program should return `None`.

#### The `find_kth_from_end` function should follow these requirements:

1. The function should utilize two pointers, `slow` and `fast`, initialized to the head of the linked list.

2. The `fast` pointer should move `k` nodes ahead in the list.

3. If the `fast` pointer becomes `None` before moving `k` nodes, the function should return `None`, as the list is shorter than `k` nodes.

4. The `slow` and `fast` pointers should then move forward in the list at the same time until the `fast` pointer reaches the end of the list.

5. The function should return the `slow` pointer, which will be at the k-th position from the end of the list.

**Note:** This is a separate function that is not a method within the `LinkedList` class. 

-----------------------------------------------------------------------------------------



## 4. Partition List (**Interview Question**)
  
**HEADS UP: Advanced Challenge**

### Implement the `partition_list` member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

**Note:** 
This linked list class does NOT have a tail which will make this method easier to implement.  
The original relative order of the nodes should be preserved.

### Details:
The function `partition_list` takes an integer `x` as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.

### Example 1:
- **Input:**  
   - Linked List: `3 -> 8 -> 5 -> 10 -> 2 -> 1`  
   - x: `5`

- **Process:** 
   - Values less than 5: `3, 2, 1`  
   - Values greater than or equal to 5: `8, 5, 10`

- **Output:**  
   - Linked List: `3 -> 2 -> 1 -> 8 -> 5 -> 10`


### Example 2:
- **Input:**  
   - Linked List: `1 -> 4 -> 3 -> 2 -> 5 -> 2`  
   - x: `3`

- **Process:**  
   - Values less than 3: `1, 2, 2`  
   - Values greater than or equal to 3: `4, 3, 5`

- **Output:**  
   - Linked List: `1 -> 2 -> 2 -> 4 -> 3 -> 5`


#### Tips:
- While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.
- Use dummy nodes to simplify the handling of the heads of these chains.
- After processing the entire list, connect the two chains to get the desired arrangement.

#### Constraints:
- The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.
- You must solve the problem **without modifying the values** in the list's nodes (i.e., only the nodes' next pointers may be changed).

-----------------------------------------------------------------------------------------



## 5. Remove Duplicates (**Interview Question**)

### Implement a method called `remove_duplicates()` within the `LinkedList` class that removes all duplicate values from the list.

You are given a singly linked list that contains integer values, where some of these values may be duplicated.

**Note:** This linked list class does NOT have a tail, which will make this method easier to implement.

Your method should not create a new list, but rather modify the existing list **in-place**, preserving the relative order of the nodes.

#### You can implement the `remove_duplicates()` method in two different ways:

1. **Using a Set**:
   - This approach will have a time complexity of **O(n)**, where `n` is the number of nodes in the linked list.
   - You are allowed to use the provided `Set` data structure in your implementation.

2. **Without using a Set**:
   - This approach will have a time complexity of **O(n^2)**, where `n` is the number of nodes in the linked list.
   - You are not allowed to use any additional data structures for this implementation.

#### Method Signature:
```python
def remove_duplicates(self):
```

#### Example:
- **Input**:
```
LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
```

- **Output**:
```
LinkedList: 1 -> 2 -> 3 -> 4 -> 5
```

-----------------------------------------------------------------------------------------



## 6. Binary to Decimal (**Interview Question**)

### Implement the `binary_to_decimal` method for the `LinkedList` class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. The `LinkedList` class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.

The `binary_to_decimal` method should start from the head of the linked list and use each node's value to calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:

    To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power equivalent to the position of the digit, counting from right to left starting from 0, and all the results are summed together to get the decimal number.

The `binary_to_decimal` method should return this calculated decimal number.

#### Examples
Consider the binary number `101`. If this number is represented as a linked list, the head of the linked list will contain the digit `1`, the next node will contain `0`, and the last node will contain `1`. When we apply the `binary_to_decimal` method on this linked list, the method should return the number `5`, which is the decimal equivalent of binary `101`.

Similarly, for a linked list representing the binary number `1101`, the `binary_to_decimal` method should return the number `13`.

#### Example Code
Here's how you can create these linked lists and call the `binary_to_decimal` method:

```python
# Create a linked list for binary number 101
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 5
 
# Create a linked list for binary number 1101
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
 
# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 13
```

-----------------------------------------------------------------------------------------



## 7. Reverse Between (**Interview Question**)  

**HEADS UP: Advanced Challenge**

### Implement a method `reverse_between` within the LinkedList class that reverses the nodes of the linked list from `start_index` to `end_index` (inclusive using 0-based indexing) in one pass and in-place.

You are given a singly linked list and two integers `start_index` and `end_index`.

**Note:** The Linked List does not have a tail which will make the implementation easier.

**Assumption:** You can assume that `start_index` and `end_index` are not out of bounds.

#### Input
- The method `reverse_between` takes two integer inputs `start_index` and `end_index`.

- The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds).

#### Output
- The method should modify the linked list in-place by reversing the nodes from `start_index` to `end_index`.

- If the linked list is empty or has only one node, the method should return `None`.

#### Example
- Suppose the linked list is `1 -> 2 -> 3 -> 4 -> 5`, and `start_index = 2` and `end_index = 4`. Then, the method should modify the linked list to `1 -> 2 -> 5 -> 4 -> 3`.

#### Constraints
- The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).

-----------------------------------------------------------------------------------------