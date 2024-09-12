from typing import TypeVar, Generic, Optional


ItemType = TypeVar('ItemType')


class Node_DLL(Generic[ItemType]):
    """
    A class representing a node in a doubly linked list.

    Attributes:
        value (ItemType): The value stored in the node.
        next (Optional[Node_DLL[ItemType]]): The reference to the next node in the list.
        prev (Optional[Node_DLL[ItemType]]): The reference to the previous node in the list.
    """

    def __init__(self, value: ItemType) -> None:
        """
        Initialize a new node with a given value.

        Args:
            value (ItemType): The value to be stored in the node.
        """
        self.value = value
        self.next: Optional[Node_DLL[ItemType]] = None
        self.prev: Optional[Node_DLL[ItemType]] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return f"Node({self.value})"


class DoublyLinkedList(Generic[ItemType]):
    """
    A class representing a doubly linked list.

    Attributes:
        head (Optional[Node_DLL[ItemType]]): The head node of the list.
        tail (Optional[Node_DLL[ItemType]]): The tail node of the list.
        length (int): The number of nodes in the list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty doubly linked list.
        """
        self.head: Optional[Node_DLL[ItemType]] = None
        self.tail: Optional[Node_DLL[ItemType]] = None
        self.length: int = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the doubly linked list.

        Returns:
            str: The string representation of the doubly linked list.
        """
        first_link = "None <-- " if self.length > 0 else ""
        display = f"\n*  {first_link}"
        temp = self.head
        while temp:
            link = "<-->" if temp.next else "-->"
            display += f"{temp} {link} "
            temp = temp.next
        display += f"""None

    . Head: {self.head}
    . Tail: {self.tail}
    . Length: {self.length}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the doubly linked list.
        """
        print(self)

    def empty(self) -> bool:
        """
        Check if the doubly linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.length == 0

    def clear(self) -> None:
        """
        Clear the doubly linked list by resetting head, tail, and length attributes.
        """
        self.head = self.tail = None
        self.length = 0

    def append(self, value: ItemType) -> bool:
        """
        Append a new node with a given value to the end of the list.

        Args:
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully appended.
        """
        new_node = Node_DLL(value)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value: ItemType) -> bool:
        """
        Prepend a new node with a given value to the start of the list.

        Args:
            value (ItemType): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully prepended.
        """
        new_node = Node_DLL(value)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node_DLL[ItemType]]:
        """
        Remove and return the last node from the list.

        Returns:
            Optional[Node_DLL[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.empty():
            return None
        node_to_pop = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            node_to_pop.prev = None
        self.length -= 1
        return node_to_pop

    def pop_first(self) -> Optional[Node_DLL[ItemType]]:
        """
        Remove and return the first node from the list.

        Returns:
            Optional[Node_DLL[ItemType]]: The removed node, or None if the list is empty.
        """
        if self.empty():
            return None
        node_to_pop = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node_to_pop.next = None
        self.length -= 1
        return node_to_pop

    def get(self, index: int) -> Optional[Node_DLL[ItemType]]:
        """
        Retrieve the node at a specific index in the list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Optional[Node_DLL[ItemType]]: The node at the specified index, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            node_to_get = self.head
            for _ in range(index):
                node_to_get = node_to_get.next
        else:
            node_to_get = self.tail
            for _ in range(self.length - 1, index, -1):
                node_to_get = node_to_get.prev
        return node_to_get

    def set_value(self, index: int, value: ItemType) -> bool:
        """
        Set the value of the node at a specific index in the list.

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
        Insert a new node with a given value at a specific index in the list.

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

        new_node = Node_DLL(value)
        node_before = self.get(index - 1)
        node_after = node_before.next

        new_node.prev = node_before
        new_node.next = node_after
        node_before.next = new_node
        node_after.prev = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Node_DLL[ItemType]]:
        """
        Remove and return the node at a specific index in the list.

        Args:
            index (int): The index of the node to remove.

        Returns:
            Optional[Node_DLL[ItemType]]: The removed node, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        node_to_pop = self.get(index)
        node_to_pop.prev.next = node_to_pop.next
        node_to_pop.next.prev = node_to_pop.prev
        node_to_pop.prev = node_to_pop.next = None
        self.length -= 1
        return node_to_pop

    def from_list(self, values: list[ItemType]) -> None:
        """
        Populate the doubly linked list with values from a Python list.

        Args:
            values (list[ItemType]): The list of values to populate the doubly linked list.
        """
        self.clear()  # Clears the existing list
        for value in values:
            self.append(value)

    def to_list(self) -> list[ItemType]:
        """
        Convert the doubly linked list to a Python list.

        Returns:
            list[ItemType]: A list containing all the values from the doubly linked list.
        """
        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        return values


def main():
    # Create a new doubly linked list
    dll = DoublyLinkedList[int]()

    # Test the append method
    print("\n==> Appending values 1, 2, and 3:")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()
    print("-" * 80)

    # Test the prepend method
    print("\n==> Prepending values 0 and -1:")
    dll.prepend(0)
    dll.prepend(-1)
    dll.display()
    print("-" * 80)

    # Test the pop method
    print("\n==> Popping the last element:")
    dll.pop()
    dll.display()
    print("-" * 80)

    # Test the pop_first method
    print("\n==> Popping the first element:")
    dll.pop_first()
    dll.display()
    print("-" * 80)

    # Test the get method
    print("\n==> Getting elements at index 1 and 2:")
    print(f"\n\t. Element at index 1: {dll.get(1)}")
    print(f"\t. Element at index 2: {dll.get(2)}\n")
    print("-" * 80)

    # Test the set_value method
    print("\n==> Setting value of the element at index 1 to 10:")
    dll.set_value(1, 10)
    dll.display()
    print("-" * 80)

    # Test the insert method
    print("\n==> Inserting value 5 at index 1:")
    dll.insert(1, 5)
    dll.display()
    print("-" * 80)

    # Test the remove method
    print("\n==> Removing element at index 2:")
    dll.remove(2)
    dll.display()
    print("-" * 80)

    # Test the clear method
    print("\n==> Clearing the list:")
    dll.clear()
    dll.display()
    print("-" * 80)

    # Test the from_list method
    print("\n==> Creating list from [1, 2, 3, 4, 5]:")
    dll.from_list([1, 2, 3, 4, 5])
    dll.display()
    print("-" * 80)

    # Test the to_list method
    print("\n==> Converting the doubly linked list to a Python list:")
    python_list = dll.to_list()
    print(f"\n\t. Python list: {python_list}\n")
    print("-" * 80)

    # Clear the doubly linked list
    dll.clear()


if __name__ == "__main__":
    main()
