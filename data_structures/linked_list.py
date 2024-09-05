from typing import TypeVar, Generic, Optional


ItemType = TypeVar('ItemType')


class Node_LL(Generic[ItemType]):
    """
    A class representing a node in a linked list.

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
        return f"Node({self.value})"


class LinkedList(Generic[ItemType]):
    """
    A class representing a singly linked list.

    Attributes:
        head (Optional[Node_LL[ItemType]]): The head node of the linked list.
        tail (Optional[Node_LL[ItemType]]): The tail node of the linked list.
        length (int): The number of nodes in the linked list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty linked list.
        """
        self.head: Optional[Node_LL[ItemType]] = None
        self.tail: Optional[Node_LL[ItemType]] = None
        self.length: int = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        display = "\n*  "
        temp = self.head
        while temp:
            display += f"{temp} --> "
            temp = temp.next
        display += f"""None

    . Head: {self.head}
    . Tail: {self.tail}
    . Length: {self.length}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the linked list.
        """
        print(self)

    def empty(self) -> bool:
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.length == 0

    def clear(self) -> None:
        """
        Clear the linked list by resetting head, tail, and length attributes.

        This method removes all nodes from the linked list, effectively making it an empty list.
        """
        self.head = self.tail = None
        self.length = 0

    def from_list(self, items: list[ItemType]) -> None:
        """
        Initialize the linked list from a Python list.

        Args:
            items (list[ItemType]): The list of values to convert into a linked list.
        """
        # Reset the list before creating from the list
        self.head = None
        self.tail = None
        self.length = 0

        for item in items:
            self.append(item)

    def to_list(self) -> list[ItemType]:
        """
        Convert the linked list to a Python list.

        Returns:
            list[ItemType]: A list of values from the linked list.
        """
        items = []  # Initialize an empty list
        current = self.head
        # Iterates through the linked list starting from self.head
        while current:
            # Append the value of each node to the items list
            items.append(current.value)
            current = current.next
        return items  # Return the items list

    def append(self, value: ItemType) -> bool:
        """
        Append a new node with a given value to the end of the linked list.

        Args:
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully appended.
        """
        new_node = Node_LL(value)
        if self.empty():
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
        new_node = Node_LL(value)
        if self.empty():
            # If the list is empty, set the new node as both head and tail
            self.head = self.tail = new_node
        else:
            # Insert the new node at the start of the list
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node_LL[ItemType]]:
        """
        Remove and return the last node from the linked list.

        Returns:
            Optional[Node_LL[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.empty():
            return None
        node_before = node_to_pop = self.head
        while node_to_pop.next:
            node_before = node_to_pop
            node_to_pop = node_to_pop.next
        # Disconnect the last node from the list
        node_before.next = None
        self.tail = node_before
        self.length -= 1
        if self.empty():
            # If the list becomes empty, reset head and tail to None
            self.head = self.tail = None
        return node_to_pop

    def pop_first(self) -> Optional[Node_LL[ItemType]]:
        """
        Remove and return the first node from the linked list.

        Returns:
            Optional[Node_LL[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.empty():
            return None
        node_to_pop = self.head
        if self.length == 1:
            # If there is only one node in the list, reset head and tail to None
            self.head = self.tail = None
        else:
            # Move head to the next node
            self.head = self.head.next
        node_to_pop.next = None  # Disconnect the popped node from the list
        self.length -= 1
        return node_to_pop

    def get(self, index: int) -> Optional[Node_LL[ItemType]]:
        """
        Retrieve the node at a specific index in the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Optional[Node_LL[ItemType]]: The node at the specified index, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        node_to_get = self.head
        for _ in range(index):
            node_to_get = node_to_get.next
        return node_to_get

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
        new_node = Node_LL(value)
        node_before = self.get(index - 1)
        new_node.next = node_before.next
        node_before.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Node_LL[ItemType]]:
        """
        Remove and return the node at a specific index in the linked list.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Optional[Node_LL[ItemType]]: The removed node, or None if the index is out of range.
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

def main() -> None:
    # Create a new linked list
    linked_list = LinkedList[int]()
    
    print("==> Initial empty linked list:")
    linked_list.display()
    print("-" * 40)

    # Test appending nodes
    print("==> Appending values 1, 2, 3, 4, 5:")
    for i in range(1, 6):
        linked_list.append(i)
    linked_list.display()
    print("-" * 40)

    # Test prepending nodes
    print("==> Prepending values 0, -1, -2:")
    for i in range(0, -3, -1):
        linked_list.prepend(i)
    linked_list.display()
    print("-" * 40)

    # Test removing nodes
    print("==> Removing the last node:")
    linked_list.pop()
    linked_list.display()
    print("-" * 40)

    print("==> Removing the first node:")
    linked_list.pop_first()
    linked_list.display()
    print("-" * 40)

    # Test inserting nodes at specific positions
    print("==> Inserting values 10 at index 0 and 20 at index 3:")
    linked_list.insert(0, 10)
    linked_list.insert(3, 20)
    linked_list.display()
    print("-" * 40)

    # Test getting and setting values
    print("==> Getting value at index 2:")
    node = linked_list.get(2)
    print(f"\n*  Node at index 2: {node}\n")
    print("-" * 40)

    print("==> Setting value at index 2 to 99:")
    linked_list.set_value(2, 99)
    linked_list.display()
    print("-" * 40)

    # Test removing nodes by index
    print("==> Removing node at index 1:")
    linked_list.remove(1)
    linked_list.display()
    print("-" * 40)

    # Test reversing the linked list
    print("==> Reversing the linked list:")
    linked_list.reverse()
    linked_list.display()
    print("-" * 40)

    # Test converting to a Python list
    print("==> Converting linked list to a Python list:")
    python_list = linked_list.to_list()
    print("\n* ", python_list, "\n")
    print("-" * 40)

    # Test clearing the linked list
    print("==> Clearing the linked list:")
    linked_list.clear()
    linked_list.display()
    print("-" * 40)

if __name__ == "__main__":
    main()
