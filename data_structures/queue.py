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
    A class representing a queue.

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
        Return a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        display = "\n\n*         <-- IN"
        runner = ""
        temp = self.first
        while temp:
            runner = f"\n  | {temp} |" + runner
            temp = temp.next
        else:
            if runner == "":
                runner = "\n  |     |"
        display += runner + f"""
  |     |
          --> OUT


  . First: {self.first}
  . Last: {self.last}
  . Length: {self.length}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the queue.
        """
        print(self)

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

    def enqueue(self, value: ItemType) -> bool:
        """
        Add a new value to the end of the queue.

        Args:
            value (ItemType): The value to be added to the queue.

        Returns:
            bool: True indicating the value was successfully added to the queue.
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
        return True

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
