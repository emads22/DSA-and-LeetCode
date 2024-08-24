from typing import TypeVar, Generic, Optional


# Define a generic type for the items in the hash table
ItemType = TypeVar('ItemType')


class HashTable(Generic[ItemType]):
    """
    A simple hash table implementation using separate chaining to handle collisions.

    Attributes:
        size (int): The size of the hash table.
        data_map (list): The internal list that stores the hash table's data.
    """

    def __init__(self, size: int) -> None:
        """
        Initialize the hash table with a specified size.

        Args:
            size (int): The size of the hash table.
        """
        self.size: int = size
        # Initialize the data map with None values
        self.data_map: list = [None] * self.size

    def __repr__(self) -> str:
        """
        Return a string representation of the hash table.

        Returns:
            str: The formatted string representing the hash table.
        """
        display = "________\n"
        for idx, value in enumerate(self.data_map):
            display += f"{idx} | {value}\n"
        if self.size == 0:
            display += "  | \n"
        display += "________\n"
        return display

    def display(self) -> None:
        """
        Print the current state of the hash table.
        """
        print(self)

    def empty(self) -> bool:
        """
        Check if the hash table is empty.

        Returns:
            bool: True if the hash table is empty, False otherwise.
        """
        return self.size == 0

    def __hash__(self, key: 'ItemType') -> int:
        """
        Compute the hash value for a given key.

        Args:
            key (ItemType): The key to hash. It can be a string or an integer.

        Returns:
            int: The computed hash value.

        Raises:
            TypeError: If the key is not a string or an integer.
        """
        if isinstance(key, str):
            hash_value = 0  # Initialize the hash value for strings
            prime = 31  # Prime number used as a multiplier to reduce collisions
            # Iterate over each character in the string
            for i, char in enumerate(key):
                # Update hash_value: multiply the current hash by prime and add ASCII value of the character
                # Taking modulo by self.size to keep the hash value within the range
                hash_value = (hash_value * prime + ord(char)) % self.size
        elif isinstance(key, int):
            prime = 31  # Prime number used for bitwise operations to enhance distribution
            hash_value = key  # Start with the integer key itself
            # Apply bitwise XOR `^` and shift operations `>>` to mix the bits of the integer
            # This helps in spreading the hash values more evenly
            hash_value = (hash_value ^ (hash_value >> 16)) * prime
            hash_value = (hash_value ^ (hash_value >> 16)) % self.size
        else:
            # If the key is not a string or an integer, raise a TypeError
            raise TypeError(
                "\n\n--- Key must be a string or an integer. ---\n\n")
        # Return the computed hash value
        return hash_value

    def set_item(self, key: ItemType, value: ItemType) -> None:
        """
        Insert a key-value pair into the hash table.

        Args:
            key (ItemType): The key to insert.
            value (ItemType): The value associated with the key.
        """
        index = self.__hash__(key)  # Compute the hash index for the key
        if self.data_map[index] is None:
            # Initialize a list at the index if it's empty
            self.data_map[index] = []
        # Append the key-value pair to the list at the index
        self.data_map[index].append([key, value])

    def get_item(self, key: ItemType) -> Optional[ItemType]:
        """
        Retrieve a value from the hash table based on its key.

        Args:
            key (ItemType): The key whose value is to be retrieved.

        Returns:
            Optional[ItemType]: The value associated with the key if found, or None if the key is not in the table.
        """
        # METHOD 1
        index = self.__hash__(key)  # Compute the hash index for the key
        if self.data_map[index] is not None:
            # Iterate over the pairs in the list at the index to find the matching key
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]  # Return the value if the key matches
        return None  # Return None if the key is not found

        # # METHOD 2
        # index = self.__hash__(key)  # Compute the hash index for the key
        # if self.data_map[index] is not None:
        #     # Iterate over the list at the index to find the matching key using indexing
        #     for i in range(len(self.data_map[index])):
        #         if self.data_map[index][i][0] == key:
        #             return self.data_map[index][i][1]  # Return the value if the key matches
        # return None  # Return None if the key is not found
