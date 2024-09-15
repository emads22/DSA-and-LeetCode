from typing import Optional


class MaxHeap:
    """
    A max-heap implementation where the largest integer is always at the root.

    Attributes:
        heap (list): A list representing the binary heap structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty max-heap.
        """
        self.heap: list[int] = [
        ]  # Explicitly declare the heap as a list of integers

    def __repr__(self) -> str:
        """
        Return a string representation of the max-heap.

        Returns:
            str: The string representation of the max-heap.
        """
        return f"\n*  {self.heap}\n"

    def display(self) -> None:
        """
        Print the string representation of the max-heap.
        """
        print(self)

    def size(self) -> int:
        """
        Get the number of elements in the max-heap.

        Returns:
            int: The number of elements in the max-heap.
        """
        return len(self.heap)

    def empty(self) -> bool:
        """
        Check if the max-heap is empty.

        Returns:
            bool: True if the max-heap is empty, False otherwise.
        """
        return self.size() == 0

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

    def insert(self, value: int) -> None:
        """
        Insert a new value into the max-heap.

        Args:
            value (int): The value to insert into the heap.
        """
        # Only integers are inserted into the MaxHeap
        if not isinstance(value, int):
            raise TypeError(
                "\n\n--- Only integers can be inserted into the MaxHeap. ---\n\n")
        self.heap.append(value)  # Add the new value at the end of the heap
        idx = len(self.heap) - 1  # Start at the last element
        # Bubble up the value to restore heap order
        while idx > 0:
            parent_idx = self._parent(idx)
            if self.heap[idx] > self.heap[parent_idx]:
                # Swap if the current value is greater than its parent
                self._swap(idx, parent_idx)
            idx = parent_idx  # Move up to the parent's index

    def remove(self) -> Optional[int]:
        """
        Remove and return the maximum value (the root) from the heap.

        Returns:
            Optional[int]: The maximum value in the heap, or None if the heap is empty.
        """
        if self.empty():
            return None  # Return None if the heap is empty
        if self.size() == 1:
            return self.heap.pop()  # If only one element, pop and return it
        # The root of the heap, which is the maximum value
        max_value = self.heap[0]
        # Replace the root with the last element and reduce heap size
        self.heap[0] = self.heap.pop()
        self._sink_down(0)  # Restore heap order by sinking down the new root
        return max_value  # Return the maximum value

    def peek(self) -> Optional[int]:
        """
        Get the maximum value (the root) without removing it.

        Returns:
            Optional[int]: The maximum value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if not self.empty() else None


class MinHeap:
    """
    A min-heap implementation where the smallest integer is always at the root.

    Attributes:
        heap (list): A list representing the binary heap structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty min-heap.
        """
        self.heap: list[int] = [
        ]  # Explicitly declare the heap as a list of integers

    def __repr__(self) -> str:
        """
        Return a string representation of the min-heap.

        Returns:
            str: The string representation of the min-heap.
        """
        return f"\n*  {self.heap}\n"

    def display(self) -> None:
        """
        Print the string representation of the min-heap.
        """
        print(self)

    def size(self) -> int:
        """
        Get the number of elements in the min-heap.

        Returns:
            int: The number of elements in the min-heap.
        """
        return len(self.heap)

    def empty(self) -> bool:
        """
        Check if the min-heap is empty.

        Returns:
            bool: True if the min-heap is empty, False otherwise.
        """
        return self.size() == 0

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

    def insert(self, value: int) -> None:
        """
        Insert a new value into the min-heap.

        Args:
            value (int): The value to insert into the heap.
        """
        # Only integers are inserted into the MinHeap
        if not isinstance(value, int):
            raise TypeError(
                "\n\n--- Only integers can be inserted into the MinHeap. ---\n\n")
        self.heap.append(value)  # Add the new value at the end of the heap
        idx = len(self.heap) - 1  # Start at the last element
        # Bubble up the value to restore heap order
        while idx > 0:
            parent_idx = self._parent(idx)
            if self.heap[idx] < self.heap[parent_idx]:
                # Swap if the current value is smaller than its parent
                self._swap(idx, parent_idx)
            idx = parent_idx  # Move up to the parent's index

    def remove(self) -> Optional[int]:
        """
        Remove and return the minimum value (the root) from the heap.

        Returns:
            Optional[int]: The minimum value in the heap, or None if the heap is empty.
        """
        if self.empty():
            return None  # Return None if the heap is empty
        if self.size() == 1:
            return self.heap.pop()  # If only one element, pop and return it
        # The root of the heap, which is the minimum value
        min_value = self.heap[0]
        # Replace the root with the last element and reduce heap size
        self.heap[0] = self.heap.pop()
        self._sink_down(0)  # Restore heap order by sinking down the new root
        return min_value  # Return the minimum value

    def peek(self) -> Optional[int]:
        """
        Get the minimum value (the root) without removing it.

        Returns:
            Optional[int]: The minimum value in the heap, or None if the heap is empty.
        """
        return self.heap[0] if not self.empty() else None


def main():
    print("\n\n1.\tTest: MaxHeap\n")
    # Create an instance of MaxHeap
    print("\n==> Creating an instance of MaxHeap...")
    heap = MaxHeap()
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
    print(f"\n==> Current maximum value (peek): {heap.peek()}\n")
    print("-" * 40)

    # Check the size of the heap
    print(f"\n==> Size of the heap: {heap.size()}\n")
    print("-" * 40)

    # Check if the heap is empty
    print(f"\n==> Is the heap empty? {'Yes' if heap.empty() else 'No'}\n")
    print("-" * 80)

    print("\n\n\n\n2.\tTest: MinHeap\n")

    # Create an instance of MinHeap
    print("\n==> Creating an instance of MinHeap...")
    heap = MinHeap()
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
    print(f"\n==> Current minimum value (peek): {heap.peek()}\n")
    print("-" * 40)

    # Check the size of the heap
    print(f"\n==> Size of the heap: {heap.size()}\n")
    print("-" * 40)

    # Check if the heap is empty
    print(f"\n==> Is the heap empty? {'Yes' if heap.empty() else 'No'}\n")
    print("-" * 80)


if __name__ == "__main__":
    main()
