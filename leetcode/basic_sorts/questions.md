## 1. Bubble Sort of Linked List (**Interview Question**)

### Implement the `bubble_sort` method within the `LinkedList` class. The `bubble_sort` method should sort the elements of the linked list in ascending order based on their values. The sorting should be done in-place, meaning you should not create a new linked list but rather modify the existing one.

**Requirements:**

- The `bubble_sort` method should iterate through the linked list, comparing each pair of adjacent nodes and swapping their values if they are in the wrong order. This process should repeat until the entire list is sorted.
- The method must handle linked lists of any length, including empty lists and lists with only one element. In cases where the list is empty or contains only one element, the method should simply return without making any changes.
- You should not use any external libraries or built-in sorting functions to implement the sorting logic.
- Optimize the `bubble_sort` method to stop early if the list becomes sorted before going through all the iterations.

**Hints:**

- You can use a loop to iterate through the list multiple times, each time moving the largest unsorted value to its correct position in the sorted portion of the list.
- To swap the values of two nodes, you can directly swap their value attributes without changing their position in the list.
- Consider using a marker or a pointer to keep track of the portion of the list that is already sorted, to avoid unnecessary comparisons and swaps.

**Input:**

- The `LinkedList` object containing a linked list with unsorted elements (`self`).

**Output:**

- None. The method sorts the linked list in place.

**Method Description:**

- If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
- The bubble sort algorithm works by repeatedly iterating through the unsorted part of the list, comparing adjacent elements and swapping them if they are in the wrong order.
- The method starts with the entire linked list being the unsorted part of the list.
- For each pass through the unsorted part of the list, the method iterates through each pair of adjacent elements and swaps them if they are in the wrong order.
- After each pass, the largest element in the unsorted part of the list will "bubble up" to the end of the list.
- The method continues iterating through the unsorted part of the list until no swaps are made during a pass.
- After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.

**Constraints:**

- The linked list can contain duplicates.
- The method should be implemented in the `LinkedList` class.
- The method should not use any additional data structures to sort the linked list.

-----------------------------------------------------------------------------------------



## 2. Selection Sort of Linked List (**Interview Question**)

### Write a `selection_sort()` method in the `LinkedList` class that will sort the elements of a linked list in ascending order using the selection sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.

**Input:**

- The `LinkedList` object containing a linked list with unsorted elements (`self`).

**Output:**

- None. The method sorts the linked list in place.

**Method Description:**

- If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
- The selection sort algorithm works by repeatedly finding the smallest element in the unsorted part of the list and swapping it with the first element in the unsorted part of the list.
- The method starts with the entire linked list being the unsorted part of the list.
- For each pass through the unsorted part of the list, the method iterates through each element to find the smallest element in the unsorted part of the list. Once the smallest element is found, it is swapped with the first element in the unsorted part of the list.
- After each pass, the smallest element in the unsorted part of the list will be at the beginning of the unsorted part of the list.
- The method continues iterating through the unsorted part of the list until the entire list is sorted.
- After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.

**Constraints:**

- The linked list can contain duplicates.
- The method should be implemented in the `LinkedList` class.
- The method should not use any additional data structures to sort the linked list.

-----------------------------------------------------------------------------------------



## 3.  (**Interview Question**)

### 

-----------------------------------------------------------------------------------------
