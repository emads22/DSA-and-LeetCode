from typing import TypeVar, Generic, Optional


# Define a TypeVar for the heap items
ItemType = TypeVar('ItemType')


class MaxHeap(Generic[ItemType]):
    """
    A max-heap implementation where the largest element (in term of comparison) is always at the root.

    Attributes:
        heap (list): A list representing the binary heap structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty max-heap.
        """
        self.heap: list[ItemType] = []

    def __repr__(self) -> str:
        """
        Return a concise string representation of the max-heap.

        Returns:
            str: A string representation of the max-heap.
        """
        return f"MaxHeap(Root: {self.peek()})"

    def __str__(self) -> str:
        """
        Return a formatted string representation of the max-heap.

        Returns:
            str: The formatted string representation of the max-heap.
        """
        return f"\n*  {self.heap}\n"

    def display(self) -> None:
        """
        Print the string representation of the max-heap.
        """
        print(str(self))

    def size(self) -> int:
        """
        Get the number of elements in the max-heap.

        Returns:
            int: The number of elements in the max-heap.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Check if the max-heap is empty.

        Returns:
            bool: True if the max-heap is empty, False otherwise.
        """
        return self.size() == 0

    def peek(self) -> Optional[ItemType]:
        """
        Get the maximum value (the root) without removing it.

        Returns:
            Optional[ItemType]: The maximum value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if not self.is_empty() else None

    def _left_child(self, index: int) -> int:
        """
        Calculate the index of the left child of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the left child.
        """
        return (2 * index) + 1

    def _right_child(self, index: int) -> int:
        """
        Calculate the index of the right child of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the right child.
        """
        return (2 * index) + 2

    def _parent(self, index: int) -> int:
        """
        Calculate the index of the parent of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap the elements at the two given indices in the heap.

        Args:
            index1 (int): The index of the first element.
            index2 (int): The index of the second element.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _validate_value(self, value: ItemType) -> bool:
        """
        Validate the value to be inserted into the max-heap.

        This method checks that the value is of a supported type, that it is
        comparable to the existing elements in the heap, and raises a TypeError
        if any checks fail.

        Args:
            value (ItemType): The value to validate for insertion into the heap.

        Raises:
            TypeError: If the value is a non-comparable type, or if it is not of
                        the expected type for insertion into the heap.
        """
        # Exclude non-comparable types such as: list, dict, and set.
        # Accepted comparable types such as: int, float, str, tuple, Custom comparable object (with proper comparison methods implemented).
        excluded_types = (list, dict, set)
        if isinstance(value, excluded_types):
            raise TypeError(f"Cannot insert type: `{type(value).__name__}`")

        # Check if the heap is not empty and ensure the value is of the same type
        # as the existing elements in the heap.
        if self.heap and not isinstance(value, type(self.heap[0])):
            raise TypeError(f"Cannot insert type `{type(value).__name__}`, expected `{type(self.heap[0]).__name__}`")

        # Ensure the value is comparable by checking for required comparison methods.
        comparison_methods = ["__lt__", "__le__", "__gt__", "__ge__", "__eq__"]
        if not all(hasattr(value, method) for method in comparison_methods):
            raise TypeError(f"Cannot insert non-comparable type: `{type(value).__name__}`")

    def _bubble_up(self, index: int) -> None:
        """
        Bubble up the value to restore the max-heap order.

        Args:
            index (int): The index of the element to bubble up.
        """
        # Bubble up the value to restore heap order
        while index > 0:
            parent_idx = self._parent(index)
            if self.heap[index] > self.heap[parent_idx]:
                # Swap if the current value is greater than its parent
                self._swap(index, parent_idx)
                index = parent_idx  # Move up to the parent's index
            else:
                return  # Stop if the current value is in the correct position

    def insert(self, value: ItemType) -> None:
        """
        Insert a new value into the max-heap.

        Args:
            value (ItemType): The value to insert into the heap.
        """
        try:
            self._validate_value(value)
            self.heap.append(value)  # Add the new value at the end of the heap
            # Start bubbling up at the last element
            self._bubble_up(len(self.heap) - 1)
        except TypeError as error:
            print(f"\n\t--- Error inserting '{value}', {error} ---\n")

    def _sink_down(self, index: int) -> None:
        """
        Sink down the element at the given index to restore the max-heap property.

        This method ensures that the element at the provided index moves down the heap until the max-heap
        property (parent >= children) is restored. The method swaps the element with the larger of its
        children if necessary and continues this process until the correct position is found.

        Args:
            index (int): The index of the element to sink down in the heap.
        """
        while index < self.size():
            left_child_idx = self._left_child(index)
            right_child_idx = self._right_child(index)
            max_idx = index  # Assume the current index has the max value
            # Check if the left child exists and is greater than the current element
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[max_idx]:
                max_idx = left_child_idx  # Update max_idx to the left child index
            # Check if the right child exists and is greater than the current max element
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[max_idx]:
                max_idx = right_child_idx  # Update max_idx to the right child index
            # If the current element is not the largest, swap it with the larger child
            if max_idx != index:
                self._swap(max_idx, index)  # Perform the swap
                index = max_idx  # Move to the index of the swapped element and continue
            else:
                # If the element is in the correct position, break the loop
                return

    def remove(self) -> Optional[ItemType]:
        """
        Remove and return the maximum value (the root) from the heap.

        Returns:
            Optional[ItemType]: The maximum value in the heap, or None if the heap is empty.
        """
        if self.is_empty():
            return None  # Return None if the heap is empty
        if self.size() == 1:
            return self.heap.pop()  # If only one element, pop and return it
        # The root of the heap, which is the maximum value
        max_value = self.heap[0]
        # Replace the root with the last element and reduce heap size
        self.heap[0] = self.heap.pop()
        self._sink_down(0)  # Restore heap order by sinking down the new root
        return max_value  # Return the maximum value


class MinHeap(Generic[ItemType]):
    """
    A min-heap implementation where the smallest element (in term of comparison) is always at the root.

    Attributes:
        heap (list): A list representing the binary heap structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty min-heap.
        """
        self.heap: list[ItemType] = []

    def __repr__(self) -> str:
        """
        Return a concise string representation of the min-heap.

        Returns:
            str: A string representation of the min-heap.
        """
        return f"MinHeap(Root: {self.peek()})"

    def __str__(self) -> str:
        """
        Return a formatted string representation of the min-heap.

        Returns:
            str: The formatted string representation of the min-heap.
        """
        return f"\n*  {self.heap}\n"

    def display(self) -> None:
        """
        Print the string representation of the min-heap.
        """
        print(str(self))

    def size(self) -> int:
        """
        Get the number of elements in the min-heap.

        Returns:
            int: The number of elements in the min-heap.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Check if the min-heap is empty.

        Returns:
            bool: True if the min-heap is empty, False otherwise.
        """
        return self.size() == 0

    def peek(self) -> Optional[ItemType]:
        """
        Get the minimum value (the root) without removing it.

        Returns:
            Optional[ItemType]: The minimum value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if not self.is_empty() else None

    def _left_child(self, index: int) -> int:
        """
        Calculate the index of the left child of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the left child.
        """
        return (2 * index) + 1

    def _right_child(self, index: int) -> int:
        """
        Calculate the index of the right child of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the right child.
        """
        return (2 * index) + 2

    def _parent(self, index: int) -> int:
        """
        Calculate the index of the parent of the given node.

        Args:
            index (int): The index of the current node.

        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap the elements at the two given indices in the heap.

        Args:
            index1 (int): The index of the first element.
            index2 (int): The index of the second element.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _validate_value(self, value: ItemType) -> bool:
        """
        Validate the value to be inserted into the min-heap.

        This method checks that the value is of a supported type, that it is
        comparable to the existing elements in the heap, and raises a TypeError
        if any checks fail.

        Args:
            value (ItemType): The value to validate for insertion into the heap.

        Raises:
            TypeError: If the value is a non-comparable type, or if it is not of
                        the expected type for insertion into the heap.
        """
        # Exclude non-comparable types such as: list, dict, and set.
        # Accepted comparable types such as: int, float, str, tuple, Custom comparable object (with proper comparison methods implemented).
        excluded_types = (list, dict, set)
        if isinstance(value, excluded_types):
            raise TypeError(f"Cannot insert type: `{type(value).__name__}`")

        # Check if the heap is not empty and ensure the value is of the same type
        # as the existing elements in the heap.
        if self.heap and not isinstance(value, type(self.heap[0])):
            raise TypeError(f"Cannot insert type `{type(value).__name__}`, expected `{type(self.heap[0]).__name__}`")

        # Ensure the value is comparable by checking for required comparison methods.
        comparison_methods = ["__lt__", "__le__", "__gt__", "__ge__", "__eq__"]
        if not all(hasattr(value, method) for method in comparison_methods):
            raise TypeError(f"Cannot insert non-comparable type: `{type(value).__name__}`")

    def _bubble_up(self, index: int) -> None:
        """
        Bubble up the value to restore the min-heap order.

        Args:
            index (int): The index of the element to bubble up.
        """
        # Bubble up the value to restore heap order
        while index > 0:
            parent_idx = self._parent(index)
            if self.heap[index] < self.heap[parent_idx]:
                # Swap if the current value is smaller than its parent
                self._swap(index, parent_idx)
                index = parent_idx  # Move up to the parent's index
            else:
                return  # Stop if the current value is in the correct position

    def insert(self, value: ItemType) -> None:
        """
        Insert a new value into the min-heap.

        Args:
            value (ItemType): The value to insert into the heap.
        """
        try:
            self._validate_value(value)
            self.heap.append(value)  # Add the new value at the end of the heap
            # Start bubbling up at the last element
            self._bubble_up(len(self.heap) - 1)
        except TypeError as error:
            print(f"\n\t--- Error inserting '{value}', {error} ---\n")

    def _sink_down(self, index: int) -> None:
        """
        Sink down the element at the given index to restore the min-heap property.

        This method ensures that the element at the provided index moves down the heap until the min-heap
        property (parent <= children) is restored. The method swaps the element with the smaller of its
        children if necessary and continues this process until the correct position is found.

        Args:
            index (int): The index of the element to sink down in the heap.
        """
        while index < self.size():
            left_child_idx = self._left_child(index)
            right_child_idx = self._right_child(index)
            min_idx = index  # Assume the current index has the min value
            # Check if the left child exists and is smaller than the current element
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
                min_idx = left_child_idx  # Update min_idx to the left child index
            # Check if the right child exists and is smaller than the current min element
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
                min_idx = right_child_idx  # Update min_idx to the right child index
            # If the current element is not the smallest, swap it with the smaller child
            if min_idx != index:
                self._swap(min_idx, index)  # Perform the swap
                index = min_idx  # Move to the index of the swapped element and continue
            else:
                # If the element is in the correct position, break the loop
                return

    def remove(self) -> Optional[ItemType]:
        """
        Remove and return the minimum value (the root) from the heap.

        Returns:
            Optional[ItemType]: The minimum value in the heap, or None if the heap is empty.
        """
        if self.is_empty():
            return None  # Return None if the heap is empty
        if self.size() == 1:
            return self.heap.pop()  # If only one element, pop and return it
        # The root of the heap, which is the minimum value
        min_value = self.heap[0]
        # Replace the root with the last element and reduce heap size
        self.heap[0] = self.heap.pop()
        self._sink_down(0)  # Restore heap order by sinking down the new root
        return min_value  # Return the minimum value


def main():
    print("\n\n1.\tTest: MaxHeap\n")
    # Create an instance of MaxHeap
    print("\n==> Creating an instance of MaxHeap...")

    heap = MaxHeap[int]()

    heap.display()
    print("-" * 40)

    # Insert values into the heap
    print("\n==> Inserting the values (10, 20, 5, 15, 30) into the heap...")
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(15)
    heap.insert(30)
    # Display the heap
    heap.display()
    print("-" * 40)

    # Remove the maximum value from the heap
    print("\n==> Removing the maximum value...\n")
    max_value = heap.remove()
    # Display the heap after removal
    heap.display()
    # Display removed value
    print(f"\t. Removed value: {max_value}\n")
    print("-" * 40)

    # Peek at the maximum value
    print(f"\n==> Current maximum value: {heap.peek()}\n")
    print("-" * 40)

    # Check the size of the heap
    print(f"\n==> Size of the heap: {heap.size()}\n")
    print("-" * 40)

    # Check if the heap is empty
    print(f"\n==> Is the heap empty? {'Yes' if heap.is_empty() else 'No'}\n")
    print("-" * 80)

    print("\n\n\n\n2.\tTest: MinHeap\n")

    # Create an instance of MinHeap
    print("\n==> Creating an instance of MinHeap...")
    heap = MinHeap[int]()
    heap.display()
    print("-" * 40)

    # Insert values into the heap
    print("\n==> Inserting the values (40, 50, 6, 16, 60) into the heap...")
    heap.insert(40)
    heap.insert(50)
    heap.insert(6)
    heap.insert(16)
    heap.insert(60)
    # Display the heap
    heap.display()
    print("-" * 40)

    # Remove the minimum value from the heap
    print("\n==> Removing the minimum value...\n")
    min_value = heap.remove()
    # Display the heap after removal
    heap.display()
    # Display removed value
    print(f"\t. Removed value: {min_value}\n")
    print("-" * 40)

    # Peek at the minimum value
    print(f"\n==> Current minimum value: {heap.peek()}\n")
    print("-" * 40)

    # Check the size of the heap
    print(f"\n==> Size of the heap: {heap.size()}\n")
    print("-" * 40)

    # Check if the heap is empty
    print(f"\n==> Is the heap empty? {'Yes' if heap.is_empty() else 'No'}\n")
    print("-" * 80)


if __name__ == "__main__":
    main()
