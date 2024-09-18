from typing import TypeVar, Generic, Optional


ItemType = TypeVar('ItemType')


class StaticArray(Generic[ItemType]):
    """
    A class representing a statically-sized array.
    Provides common array operations such as appending, prepending, 
    insertion, deletion, and more, with fixed size behavior.
    """

    def __init__(self, size: int) -> None:
        """
        Initialize a StaticArray with a fixed size.

        Args:
            size (int): The size of the array.
        """
        self.data: list[Optional[ItemType]] = [
            None] * size  # Initialize with None
        self.size: int = size
        self.length: int = 0

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the array, useful for debugging.

        Returns:
            str: A string representation of the array, including data, length, and size.
        """
        return f"StaticArray(data={self.data}, length={self.length}, size={self.size})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the array, suitable for end-users.

        Returns:
            str: A user-friendly string representation of the array.
        """
        return f"""
*  {self.data}

\t. Length: {self.length}
\t. Size: {self.size}
"""

    def display(self) -> None:
        """
        Print the string representation of the array using __str__.
        """
        print(str(self))

    def empty(self) -> bool:
        """
        Check if the array is empty.

        Returns:
            bool: True if the array is empty, False otherwise.
        """
        return self.length == 0

    def full(self) -> bool:
        """
        Check if the array is full.

        Returns:
            bool: True if the array is full, False otherwise.
        """
        return self.length == self.size

    def clear(self) -> None:
        """
        Clear the array by setting all elements to None.
        """
        self.data[:] = [None] * self.size
        self.length = 0

    def append(self, value: ItemType) -> None:
        """
        Append an item to the end of the array.

        Args:
            value (ItemType): The value to append.

        Raises:
            IndexError: If the array is already full.
        """
        if self.full():
            raise IndexError("Cannot append to a full array")
        self.data[self.length] = value
        self.length += 1

    def prepend(self, value: ItemType) -> None:
        """
        Insert an item at the beginning of the array.

        Args:
            value (ItemType): The value to prepend.

        Raises:
            IndexError: If the array is already full.
        """
        if self.full():
            raise IndexError("Cannot prepend to a full array")
        self.insert(0, value)

    def pop(self) -> ItemType:
        """
        Remove and return the last item of the array.

        Returns:
            ItemType: The removed item.

        Raises:
            IndexError: If the array is empty.
        """
        if self.empty():
            raise IndexError("Pop from an empty array")
        # Retrieve the last item
        last_item = self.data[self.length - 1]
        # Set the last position to None
        self.data[self.length - 1] = None
        # Decrease the length of the array
        self.length -= 1
        return last_item

    def pop_first(self) -> ItemType:
        """
        Remove and return the first item of the array.

        Returns:
            ItemType: The removed item.

        Raises:
            IndexError: If the array is empty.
        """
        if self.empty():
            raise IndexError("Cannot pop from an empty array")
        return self.delete(0)

    def get(self, index: int) -> ItemType:
        """
        Get an item at a given index.

        Args:
            index (int): The index of the item.

        Returns:
            ItemType: The item at the given index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        return self.data[index]

    def set_(self, index: int, value: ItemType) -> None:
        """
        Set the value at a given index.

        Args:
            index (int): The index to set the value at.
            value (ItemType): The value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        # Check if the index is within the valid range
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        # Set the value at the specified index
        self.data[index] = value

    def insert(self, index: int, value: ItemType) -> None:
        """
        Insert an item at a given index in the array.

        Args:
            index (int): The index to insert the value at.
            value (ItemType): The value to insert.

        Raises:
            ValueError: If the array is full or the index is invalid for the current array state.
        """
        # Check if the array is full and cannot accommodate more items
        if self.full():
            raise ValueError("Cannot insert into a full array")
        # Check if the index is within the valid range
        if index < 0 or index >= self.length:
            raise ValueError("Invalid index for insert")
        # Shift elements to the right to make space for the new item
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        # Insert the new item at the specified index
        self.data[index] = value
        self.length += 1

    def delete(self, index: int) -> ItemType:
        """
        Delete an item at a given index.

        Args:
            index (int): The index of the item to delete.

        Returns:
            ItemType: The deleted item.

        Raises:
            IndexError: If the index is out of range or the array is empty.
        """
        if self.empty():
            raise IndexError("Cannot delete from an empty array")
        to_delete = self.data[index]
        # Shift elements to the left to fill the gap created by deletion
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        # Set the last element to None after shifting
        self.data[self.length - 1] = None
        self.length -= 1
        return to_delete

    def remove(self, value: ItemType) -> None:
        """
        Remove all occurrences of a value from the array.

        Args:
            value (ItemType): The value to remove.

        Raises:
            ValueError: If the value is not found in the array.
        """
        removed = False
        # Iterate from the end to the start to handle shifts correctly
        for i in range(self.length - 1, -1, -1):
            if self.data[i] == value:
                # Remove the item and mark as removed
                self.delete(i)
                removed = True
        # Raise an error if the value was not found
        if not removed:
            raise ValueError(f"Value {value} not found in the array")

    def reverse(self) -> None:
        """
        Reverse the array in place.
        """
        if self.empty():
            return
        # Reverse only the filled portion of the array
        self.data[:self.length] = self.data[:self.length][::-1]


class DynamicArray(Generic[ItemType]):
    """
    A generic implementation of a dynamic array (list) that supports
    common operations such as appending, inserting, deleting, and retrieving
    elements.
    """

    def __init__(self) -> None:
        """
        Initialize an empty array.
        """
        self.data: list[ItemType] = []
        self.length: int = 0

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the array, useful for debugging.
        """
        return f"DynamicArray(data={self.data}, length={self.length})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the array, suitable for end-users.
        """
        return f"""\n*  {self.data}\t\t. Length: {self.length}
"""

    def display(self) -> None:
        """
        Print the string representation of the array using __str__.
        """
        print(str(self))

    def empty(self) -> bool:
        """
        Check if the array is empty.

        Returns:
            bool: True if the array is empty, False otherwise.
        """
        return self.length == 0

    def clear(self) -> None:
        """
        Clear the array, removing all elements.
        """
        self.data.clear()
        self.length = 0

    def append(self, value: ItemType) -> None:
        """
        Append an item to the end of the array.

        Args:
            value (ItemType): The value to append.
        """
        self.data.append(value)
        self.length += 1

    def prepend(self, value: ItemType) -> None:
        """
        Insert an item at the beginning of the array.

        Args:
            value (ItemType): The value to prepend.
        """
        self.insert(0, value)

    def pop(self) -> ItemType:
        """
        Remove and return the last item of the array.

        Returns:
            ItemType: The removed item.

        Raises:
            IndexError: If the array is empty.
        """
        if self.empty():
            raise IndexError("pop from empty array")
        self.length -= 1
        return self.data.pop()

    def pop_first(self) -> ItemType:
        """
        Remove and return the first item of the array.

        Returns:
            ItemType: The removed item.

        Raises:
            IndexError: If the array is empty.
        """
        return self.delete(0)

    def get(self, index: int) -> ItemType:
        """
        Get an item at a given index.

        Args:
            index (int): The index of the item.

        Returns:
            ItemType: The item at the given index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= self.length or index < 0:
            raise IndexError("index out of range")
        return self.data[index]

    def set_(self, index: int, value: ItemType) -> None:
        """
        Set the value at a given index.

        Args:
            index (int): The index to set the value at.
            value (ItemType): The value to set.

        Raises:
            IndexError: If the index is out of range.
        """
        # Check if the index is within the valid range
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        # Set the value at the specified index
        self.data[index] = value

    def insert(self, index: int, value: ItemType) -> None:
        """
        Insert an item at a given index.

        Args:
            index (int): The index to insert the item at.
            value (ItemType): The item to insert.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        # Handle appending to the end of the array
        if index == self.length:
            self.append(value)
            return
        # Resize the array if necessary
        self.data.append(self.data[-1])
        # Shift elements to the right
        for i in range(self.length - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        # Insert the value at the correct index
        self.data[index] = value
        self.length += 1

    def delete(self, index: int) -> ItemType:
        """
        Delete an item at a given index.

        Args:
            index (int): The index of the item to delete.

        Returns:
            ItemType: The deleted item.

        Raises:
            IndexError: If the index is out of range or the array is empty.
        """
        if self.empty():
            raise IndexError("Cannot delete from an empty array")
        to_delete = self.get(index)
        # Shift elements to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.pop()  # Remove the last element
        return to_delete

    def remove(self, value: ItemType) -> None:
        """
        Remove all occurrences of a value from the array.

        Args:
            value (ItemType): The value to remove.

        Raises:
            ValueError: If no occurrences of the value are found.
        """
        removed = False
        # Iterate from the end to the start to handle shifts correctly
        for i in range(self.length - 1, -1, -1):
            if self.data[i] == value:
                # Remove the item and mark as removed
                self.delete(i)
                removed = True
        # Raise an error if the value was not found
        if not removed:
            raise ValueError(f"Value {value} not found in the array")

    def reverse(self) -> None:
        """
        Reverse the array in place.
        """
        if self.empty():
            return
        self.data[:] = self.data[::-1]


def main():

    # # Uncomment to test STATIC ARRAY
    # array = StaticArray[int](6)  # Create an instance of the Array

    # Uncomment to test DYNAMIC ARRAY
    array = DynamicArray[int]()  # Create an instance of the Array

    print(f"\n==> Creating new instance `{repr(array)}`...")
    array.display()
    print("-" * 80)

    # Testing append and display
    print("\n==> Testing append():")
    print(f"\n\t- Appending elements 10, 20, and 30...")
    array.append(10)
    array.append(20)
    array.append(30)
    array.display()
    print("-" * 80)

    # Testing prepend
    print("\n==> Testing prepend():")
    print(f"\n\t- Prepending element 5...")
    array.prepend(5)
    array.display()
    print("-" * 80)

    # Testing get
    print("\n==> Testing get():")
    try:
        print(f"\n\t- Element at index 2:\t{array.get(2)}\n")
    except IndexError as e:
        print(f"{e}\n")
    print("-" * 80)

    # Testing set_
    print("\n==> Testing set_():")
    print(f"\n\t. Setting element at index 2 with 25...")
    array.set_(2, 25)
    array.display()
    print("-" * 80)

    # Testing insert
    print("\n==> Testing insert():")
    print(f"\n\t- Inserting value 15 at index 1...")
    array.insert(1, 15)
    array.display()
    print("-" * 80)

    # Testing pop
    print("\n==> Testing pop():")
    popped_value = array.pop()
    print(f"\n\t- Popped value:\t{popped_value}")
    array.display()
    print("-" * 80)

    # Testing pop_first
    print("\n==> Testing pop_first():")
    popped_first = array.pop_first()
    print(f"\n\t- Popped first value:\t{popped_first}")
    array.display()
    print("-" * 80)

    # Testing reverse
    print("\n==> Testing reverse():")
    array.reverse()
    array.display()
    print("-" * 80)

    # Testing delete
    print("\n==> Testing delete():")
    deleted_value = array.delete(1)
    print(f"\n\t- Deleted value at index 1:\t{deleted_value}")
    array.display()
    print("-" * 80)

    # Testing remove
    print("\n==> Testing remove():")
    array.append(25)
    array.append(25)
    print("\n\t- Array before removing value 25:")
    array.display()
    array.remove(25)
    print("\t- Array after removing value 25:")
    array.display()
    print("-" * 80)

    # Testing clear
    print("\n==> Testing clear():")
    array.clear()
    print("\n\t- Array after clearing:")
    array.display()
    print("-" * 80)


if __name__ == "__main__":
    main()
