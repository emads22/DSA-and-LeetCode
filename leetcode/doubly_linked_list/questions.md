## 1. Swap First and Last (**Interview Question**)

### Implement the `swap_first_last` method for the `DoublyLinkedList` class. This method should swap the values of the first and last node.

**Note**: that the pointers to the nodes themselves are not swapped - only their values are exchanged.

----------------------------------------------------------------------------------------- 



## 2. Reverse (**Interview Question**)

### Create a new method called `reverse` that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.

----------------------------------------------------------------------------------------- 



## 3. Palindrome Checker (**Interview Question**)

### Write a method called `is_palindrome` to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.

-----------------------------------------------------------------------------------------



## 4. Swap Nodes in Pairs (**Interview Question**)

**HEADS UP: Advanced Challenge**

### Implement a method called `swap_pairs` within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

**Note**: This `DoublyLinkedList` does not have a tail pointer which will make the implementation easier.

#### Example:
```
1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3
```

#### Tips:
- Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

#### Constraints: 
- You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

-----------------------------------------------------------------------------------------

