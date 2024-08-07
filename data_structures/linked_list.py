from typing import TypeVar, Generic, Optional

ItemType = TypeVar('ItemType')


class Node(Generic[ItemType]):
    """
    A class representing a node in a linked list.

    Attributes:
        value (ItemType): The value stored in the node.
        next (Optional[Node[ItemType]]): The reference to the next node in the linked list.
    """

    def __init__(self, value: ItemType) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (ItemType): The value to be stored in the node.
        """
        self.value = value
        self.next: Optional[Node[ItemType]] = None


class LinkedList(Generic[ItemType]):
    """
    A class representing a singly linked list.

    Attributes:
        head (Optional[Node[ItemType]]): The head node of the linked list.
        tail (Optional[Node[ItemType]]): The tail node of the linked list.
        length (int): The number of nodes in the linked list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty linked list.
        """
        self.head: Optional[Node[ItemType]] = None
        self.tail: Optional[Node[ItemType]] = None
        self.length: int = 0

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        display = "* "
        if self.length > 0:
            temp = self.head
            while temp:
                display += f"[ {temp.value} ] --> "
                temp = temp.next
            display += f"None\n\n  . Head: [ {self.head.value} ]\n  . Tail: [ {
                self.tail.value} ]\n  . Length: {self.length}\n\n"
        else:
            display += f"[]\n\n  . Head: None\n  . Tail: None\n  . Length: {
                self.length}\n\n"
        return display

    def clear(self) -> None:
        """
        Clear the linked list by resetting head, tail, and length attributes.

        This method removes all nodes from the linked list, effectively making it an empty list.
        """
        self.head = self.tail = None
        self.length = 0

    def append(self, value: ItemType) -> bool:
        """
        Append a new node with a given value to the end of the linked list.

        Args:
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully appended.
        """
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set the new node as both head and tail
            self.head = self.tail = new_node
        else:
            # Append the new node to the end of the list
            self.tail.next = new_node  # self.tail is guaranteed to be not None here
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value: ItemType) -> bool:
        """
        Prepend a new node with a given value to the start of the linked list.

        Args:
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully prepended.
        """
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set the new node as both head and tail
            self.head = self.tail = new_node
        else:
            # Insert the new node at the start of the list
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node[ItemType]]:
        """
        Remove and return the last node from the linked list.

        Returns:
            Optional[Node[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        node_to_pop = self.head
        node_before = None
        while node_to_pop and node_to_pop.next:
            node_before = node_to_pop
            node_to_pop = node_to_pop.next
        self.length -= 1
        if self.length == 0:
            # If the list becomes empty, reset head and tail to None
            self.head = self.tail = None
        else:
            # Disconnect the last node from the list
            node_before.next = None
            self.tail = node_before
        return node_to_pop

    def pop_first(self) -> Optional[Node[ItemType]]:
        """
        Remove and return the first node from the linked list.

        Returns:
            Optional[Node[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        node_to_pop = self.head
        self.length -= 1
        if self.length == 0:
            # If the list becomes empty, reset head and tail to None
            self.head = self.tail = None
        else:
            # Move head to the next node
            self.head = self.head.next
            node_to_pop.next = None  # Disconnect the popped node from the list
        return node_to_pop

    def get(self, index: int) -> Optional[Node[ItemType]]:
        """
        Retrieve the node at a specific index in the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Optional[Node[ItemType]]: The node at the specified index, or None if the index is out of range.
        """
        if self.length == 0 or index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: ItemType) -> bool:
        """
        Set the value of the node at a specific index in the linked list.

        Args:
            index (int): The index of the node to update.
            value (ItemType): The new value to set in the node.

        Returns:
            bool: True if the node value was successfully updated, False otherwise.
        """
        node_to_set = self.get(index)
        if node_to_set:
            node_to_set.value = value
            return True
        return False

    def insert(self, index: int, value: ItemType) -> bool:
        """
        Insert a new node with a given value at a specific index in the linked list.

        Args:
            index (int): The index at which to insert the new node.
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully inserted, False otherwise.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        node_before = self.get(index - 1)
        new_node.next = node_before.next
        node_before.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Node[ItemType]]:
        """
        Remove and return the node at a specific index in the linked list.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Optional[Node[ItemType]]: The removed node, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        node_before = self.get(index - 1)
        node_to_remove = node_before.next
        node_before.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self) -> None:
        """
        Reverse the linked list in place.

        This method reverses the order of the nodes in the linked list.
        After reversal, the head becomes the tail and vice versa.

        Returns:
            None
        """
        current = self.head
        # Swap the head and tail
        self.head, self.tail = self.tail, self.head
        before = after = None

        while current:
            # Temporarily store the next node
            after = current.next
            # Reverse the current node's pointer
            current.next = before
            # Move pointers one position ahead
            before = current
            current = after
