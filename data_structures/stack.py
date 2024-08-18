from typing import TypeVar, Generic, Optional


ItemType = TypeVar('ItemType')


class Node_LL(Generic[ItemType]):
    """
    A class representing a node in a stack represented as a linked list.

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


class Stack(Generic[ItemType]):

    """
    A class representing a stack.

    Attributes:
        top (Optional[Node_LL[ItemType]]): The head node of the stack.
        height (int): The number of nodes in the stack.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack represented as a linked list.
        """
        self.top: Optional[Node_LL[ItemType]] = None
        self.height: int = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        display = "\n\n*         <-- IN\n          --> OUT"
        runner = ""
        temp = self.top
        while temp:
            runner += f"\n  | {temp} |"
            temp = temp.next
        else:
            if runner == "":
                runner += f"\n  |     |"
        display += runner + f"""
  |_____|

  . Top: {self.top}
  . Height: {self.height}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the stack.
        """
        print(self)

    def empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.height == 0

    def clear(self) -> None:
        """
        Clear the stack by resetting top and height attributes.

        This method removes all nodes from the stack (linked list), effectively making it an empty stack.
        """
        self.top = None
        self.height = 0

    def push(self, value: ItemType) -> bool:
        """
        Push a new value onto the stack.

        Args:
            value (ItemType): The value to be added to the stack.

        Returns:
            bool: True indicating the value was successfully pushed onto the stack.
        """
        new_node = Node_LL(value)
        if self.empty():
            # If the stack is empty, the new node becomes the top node.
            self.top = new_node
        else:
            # Link the new node to the current top node and update the top.
            new_node.next = self.top
            self.top = new_node
        # Increment the height of the stack as a new node has been added.
        self.height += 1
        return True

    def pop(self) -> Optional[Node_LL[ItemType]]:
        """
        Pop the top value from the stack.

        Returns:
            Optional[Node_LL[ItemType]]: The node that was popped from the stack, or None if the stack is empty.
        """
        if self.empty():
            return None  # if the stack is empty.
        # Store the top node to return after removing it from the stack.
        node_to_pop = self.top
        # Update the top to the next node in the stack.
        self.top = self.top.next
        # Detach the popped node from the stack.
        node_to_pop.next = None
        # Decrement the height of the stack as a node has been removed.
        self.height -= 1
        return node_to_pop
