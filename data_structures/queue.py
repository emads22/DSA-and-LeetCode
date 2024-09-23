from typing import TypeVar, Generic, Optional


ItemType = TypeVar('ItemType')


class Node_LL(Generic[ItemType]):
    """
    A class representing a node in a queue represented as a linked list.

    Attributes:
        value (ItemType): The value stored in the node.
        next (Optional[Node_LL[ItemType]]): The reference to the next node in the linked list.
    """

    def __init__(self, value: ItemType) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (ItemType): The value to be stored in the node.
        """
        self.value = value
        self.next: Optional[Node_LL[ItemType]] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return f"({self.value})"


class Queue(Generic[ItemType]):
    """
    A class representing a queue implemented as a linked list.

    Attributes:
        first (Optional[Node_LL[ItemType]]): The first node of the queue.
        last (Optional[Node_LL[ItemType]]): The last node of the queue.
        length (int): The number of nodes in the queue.
    """

    def __init__(self) -> None:
        """
        Initialize an empty queue represented as a linked list.
        """
        self.first: Optional[Node_LL[ItemType]] = None
        self.last: Optional[Node_LL[ItemType]] = None
        self.length: int = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the Queue for debugging.

        Returns:
            str: A detailed string representation of the queue, including the first, last, and length.
        """
        return f"Queue(First: {self.first}, Last: {self.last}, Length: {self.length})"  
            
    def __str__(self) -> str:
        """
        Return a human-readable string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        display = "\n*         <-- IN"
        runner = ""
        temp = self.first
        while temp:
            runner = f"\n  | {temp} |" + runner
            temp = temp.next
        else:
            if runner == "":
                runner = "\n  |      |"
        display += runner + f"""
  |      |
          --> OUT


  . First: {self.first}
  . Last: {self.last}
  . Length: {self.length}
"""
        return display
    
    # Forward reference using a string
    def __iter__(self) -> 'Queue[ItemType]':
        """
        Initialize the iterator for the queue.

        Returns:
            Queue[ItemType]: The queue itself, as it will be iterated node by node.
        """
        self._current = self.first  # Set the current node to the first node in the queue
        return self

    def __next__(self) -> ItemType:
        """
        Return the next value in the queue during iteration.

        Returns:
            ItemType: The value of the current node in the iteration.

        Raises:
            StopIteration: When there are no more nodes to iterate over.
        """
        if self._current is None:
            raise StopIteration  # No more nodes to iterate, stop the iteration
        current_value = self._current.value  # Store the current node's value
        self._current = self._current.next  # Move to the next node in the queue
        return current_value  # Return the stored value

    def display(self) -> None:
        """
        Print the string representation of the queue.
        """
        print(str(self))

    def empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.length == 0

    def clear(self) -> None:
        """
        Clear the queue by resetting first, last, and length attributes.

        This method removes all nodes from the queue (linked list), effectively making it an empty queue.
        """
        self.first = self.last = None
        self.length = 0

    def enqueue(self, value: ItemType) -> None:
        """
        Add a new value to the end of the queue.

        Args:
            value (ItemType): The value to be added to the queue.
        """
        new_node = Node_LL(value)
        if self.empty():
            # If the queue is empty, the new node becomes both the first and last node.
            self.first = self.last = new_node
        else:
            # Link the last node's next reference to the new node and update the last node.
            self.last.next = new_node
            self.last = new_node
        # Increment the length of the queue as a new node has been added.
        self.length += 1

    def dequeue(self) -> Optional[Node_LL[ItemType]]:
        """
        Remove and return the value from the front of the queue.

        Returns:
            Optional[Node_LL[ItemType]]: The node that was dequeued from the front of the queue, or None if the queue is empty.
        """
        if self.empty():
            return None  # if the queue is empty.
        # Store the first node to return after removing it from the queue.
        node_to_dequeue = self.first
        if self.length == 1:
            # If the queue has only one node, reset both first and last references to None.
            self.first = self.last = None
        else:
            # Update the first reference to the next node in the queue.
            self.first = self.first.next
            # Detach the dequeued node from the queue.
            node_to_dequeue.next = None
        # Decrement the length of the queue as a node has been removed.
        self.length -= 1
        return node_to_dequeue

    


def main():
    # Create a queue of integers
    q = Queue[int]()

    # Test enqueue operation
    print("\n==> Test: enqueue operation")
    print("\n______ Enqueueing elements: 10, 20, 30 ______")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    print("-" * 80)

    # Test dequeue operation
    print("\n==> Test: dequeue operation")
    dequeued = q.dequeue()
    print(f"\n\t. Dequeued value: {dequeued}")
    q.display()
    print("-" * 80)

    # Test empty check
    print("\n==> Test: empty check")
    print(f"\n\t. Is the queue empty? {q.empty()}\n")
    print("-" * 80)

    # Test clear operation
    print("\n==> Test: clear operation")
    q.clear()
    q.display()
    print("-" * 80)

    # Test enqueue after clear
    print("\n==> Test: enqueue after clear\n")
    print("\n______ Enqueueing elements: 40, 50 ______")
    q.enqueue(40)
    q.enqueue(50)
    q.display()
    print("-" * 80)

    # Test empty check after enqueue
    print("\n==> Test: empty check after enqueue")
    print(f"\n\t. Is the queue empty? {q.empty()}\n")
    print("-" * 80)

    # Test dequeue after re-enqueue
    print("\n==> Test: dequeue after re-enqueue\n")
    while not q.empty():
        dequeued = q.dequeue()
        print(f"\n______ Dequeued value: {dequeued} ______")
        q.display()
    print("-" * 80)

    # Test empty check after dequeuing all elements
    print("\n==> Test: empty check after dequeuing all elements")
    print(f"\n\t. Is the queue empty? {q.empty()}\n")
    print("-" * 80)

    # Test iteration
    print("\n==> Test: iteration\n")
    print("\n1-\tEnqueue elements: 60, 70, 80")
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.display()

    print("2-\tIterate over queue elements:\n")
    for item in q:
        print(f"\t. Item: {item}")

    # Clear the queue and attempt to iterate over it
    print("\n3-\tClear the queue:")
    q.clear()
    q.display()
    print("4-\tAttempt to iterate over an empty queue:\n")
    if q.empty():
        print("\t. None")
    else:
        for item in q:
            # This block should not output anything as the queue is empty
            print(f"\t. Item: {item}")

    print("\n", "-" * 80)


if __name__ == "__main__":
    main()
