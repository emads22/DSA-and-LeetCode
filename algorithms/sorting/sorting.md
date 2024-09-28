# Common Sorting Algorithms in Python

### 1. **Bubble Sort**
   - **Description**: Repeatedly compares adjacent elements and swaps them if they are in the wrong order. It has poor performance on large datasets.
   - **Time Complexity**: O(n²)
   - **Space Complexity**: O(1) (in-place)
   - **Best Use Case**: Small datasets or educational purposes.

### 2. **Selection Sort**
   - **Description**: Finds the minimum element from the unsorted part and swaps it with the first unsorted element. Simple but inefficient for large lists.
   - **Time Complexity**: O(n²)
   - **Space Complexity**: O(1) (in-place)
   - **Best Use Case**: Small datasets with a need for minimal memory usage.

### 3. **Insertion Sort**
   - **Description**: Builds the sorted array one element at a time, inserting each new element into its correct position.
   - **Time Complexity**: O(n²)
   - **Space Complexity**: O(1) (in-place)
   - **Best Use Case**: Small or nearly sorted datasets.

### 4. **Merge Sort**
   - **Description**: A divide-and-conquer algorithm that splits the list in half, recursively sorts each half, and merges the sorted halves back together.
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n) (requires additional space for merging)
   - **Best Use Case**: Large datasets, particularly when stability is required.

### 5. **Quick Sort**
   - **Description**: A divide-and-conquer algorithm. It selects a pivot and partitions the list into elements less than and greater than the pivot, then recursively sorts each part.
   - **Time Complexity**: O(n log n) (average), O(n²) (worst case)
   - **Space Complexity**: O(log n) (for recursion stack in best/average case), O(n) (in worst case)
   - **Best Use Case**: Large datasets, but care is needed for worst-case scenarios (e.g., when the list is already sorted).

### 6. **Heap Sort**
   - **Description**: Builds a max-heap from the list, then repeatedly extracts the largest element and restores the heap property.
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(1) (in-place)
   - **Best Use Case**: Large datasets where O(n log n) performance is needed, and space complexity is a concern.

### 7. **Counting Sort**
   - **Description**: A non-comparison-based algorithm that counts the occurrences of each element and uses this count to place elements in their correct positions.
   - **Time Complexity**: O(n + k), where `n` is the number of elements and `k` is the range of input values.
   - **Space Complexity**: O(n + k) (requires an auxiliary array for counting and output)
   - **Best Use Case**: Large datasets with a limited range of integers.

### 8. **Radix Sort**
   - **Description**: A non-comparison-based sorting algorithm that sorts numbers digit by digit, starting from the least significant digit using a stable sub-sorting algorithm (e.g., counting sort).
   - **Time Complexity**: O(d * (n + k)), where `d` is the number of digits, `n` is the number of elements, and `k` is the range of digits (base).
   - **Space Complexity**: O(n + k) (similar to counting sort)
   - **Best Use Case**: Large datasets with integer keys or strings when the range of digits is small.

### 9. **Timsort (Python's Built-in Sort)**
   - **Description**: A hybrid sorting algorithm derived from merge sort and insertion sort. It is the default sorting algorithm in Python’s `sorted()` and `.sort()` methods.
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(n)
   - **Best Use Case**: General-purpose sorting, as it is optimized for real-world data and is highly efficient.
