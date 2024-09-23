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
    A class representing a stack implemented as a linked list.

    Attributes:
        top (Optional[Node_LL[ItemType]]): The top node of the stack.
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
        Return a string representation of the Stack for debugging.

        Returns:
            str: A detailed string representation of the stack, including the top and height.
        """
        return f"Stack(Top: {self.top}, Height: {self.height})"

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        display = "\n*         <-- IN\n          --> OUT"
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
        print(str(self))

    def is_empty(self) -> bool:
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

    def push(self, value: ItemType) -> None:
        """
        Push a new value onto the stack.

        Args:
            value (ItemType): The value to be added to the stack.
        """
        new_node = Node_LL(value)
        if self.is_empty():
            # If the stack is empty, the new node becomes the top node.
            self.top = new_node
        else:
            # Link the new node to the current top node and update the top.
            new_node.next = self.top
            self.top = new_node
        # Increment the height of the stack as a new node has been added.
        self.height += 1

    def pop(self) -> Optional[Node_LL[ItemType]]:
        """
        Pop the top value from the stack.

        Returns:
            Optional[Node_LL[ItemType]]: The node that was popped from the stack, or None if the stack is empty.
        """
        if self.is_empty():
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

    def peek(self) -> Optional[ItemType]:
        """
        Peek at the top value of the stack without removing it.

        Returns:
            Optional[ItemType]: The value at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.top.value


class StackList(Generic[ItemType]):
    """
    A class representing a stack implemented as a list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.stack_list: list = []

    def __repr__(self) -> str:
        """
        Return a string representation of the Stack for debugging.

        Returns:
            str: A detailed string representation of the stack, including the top and height.
        """
        return f"Stack(Top: {self.peek()}, Height: {self.height()})"

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the stack.
        """
        display = "\n*         <-- IN\n          --> OUT"
        runner = ""
        for element in self.stack_list:
            runner = f"\n  | {element} |" + runner
        else:
            if runner == "":
                runner += f"\n  |   |"
        display += runner + f"""
  |___|

  . Top: {self.peek()}
  . Height: {self.height()}
"""
        return display

    def display(self) -> None:
        """
        Print the string representation of the stack.
        """
        print(str(self))

    def height(self) -> int:
        return len(self.stack_list)

    def peek(self) -> Optional[ItemType]:
        """
        Return the top element of the stack without removing it.
        """
        if self.height() > 0:
            return self.stack_list[-1]
        return None

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return self.height() == 0

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        """
        self.stack_list.clear()

    def push(self, value: ItemType) -> None:
        """
        Push an element onto the stack.
        """
        self.stack_list.append(value)

    def pop(self) -> Optional[ItemType]:
        """
        Remove and return the top element of the stack.
        """
        if self.is_empty():
            return None
        return self.stack_list.pop()

def main() -> None:
    """
    Test the Stack class by performing various operations.
    """
    # Uncomment to create a new stack implemented as LinkedList
    stack = Stack[int]()
    # Uncomment to create a new stack implemented as list
    # stack = StackList[int]()
    
    print("\n==> New stack created.")

    # Display the empty stack
    stack.display()
    print("-" * 80)

    # Push elements onto the stack
    print("\n==> Test: Push elements onto the stack...\n")
    for i in range(1, 6):
        print(f"______ Pushing {i} onto the stack ______")
        stack.push(i)
        stack.display()
    print("-" * 80)

    # Peek the top element
    print("\n==> Test: Peek the top element...")
    top_element = stack.peek()
    print(f"\n\t. Peeking top element: {top_element}\n")
    print("-" * 80)

    # Pop elements from the stack
    print("\n==> Test: Pop elements from the stack...\n")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"______ Popped: {popped} ______")
        stack.display()
    print("-" * 80)

    # Clear the stack
    print("\n==> Test: Clear the stack...")
    stack.clear()
    stack.display()
    print("-" * 80)

    # Attempt to pop from the empty stack
    print("\n==> Test: Attempt to pop from the empty stack...")
    popped = stack.pop()
    print(f"\n\t. Attempted to pop from empty stack: {popped}\n")
    print("-" * 80)


if __name__ == "__main__":
    main()
