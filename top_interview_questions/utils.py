from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        """Initialize a tree node with a value and optional left and right children."""
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None

    def __str__(self) -> str:
        """Return a string representation of the tree."""
        return str(self._list) if hasattr(self, "_list") else "None"

    def build_from_list(self, values: List[Optional[int]]) -> None:
        """Build a binary tree from a list representation."""
        if not values:
            return
        # Save the list representation for display
        self._list = values
        # Create the root of the tree
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while i < len(values):
            # Get the next node from the queue
            current = queue.pop(0)
            # Insert the left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            # Insert the right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        """Initialize a list node with a value and optional next element."""
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None

    def __str__(self) -> str:
        """Return a string representation of the linked list."""
        return str(self._list) if hasattr(self, "_list") else "None"

        # # Alternatively
        # if self.head is None:
        #     return "None"
        # current = self.head
        # result = []
        # while current:
        #     result.append(str(current.val))
        #     current = current.next
        # return " -> ".join(result)

    def build_from_list(self, values: List[Optional[int]]) -> None:
        """Build a linked list from a list representation."""
        if not values:
            return
        # Save the list representation for display
        self._list = values
        # Create the root of the tree
        self.head = ListNode(values[0])  # Initialize head with the first value
        current = self.head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next

    def to_list(self) -> List[Optional[int]]:
        """Convert the linked list back to a Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.val)  # Append the value of the current node
            current = current.next      # Move to the next node
        return result

    def get_node(self, value: int) -> Optional[ListNode]:
        """
        Retrieve the node with the specified value.
        """
        current = self.head
        while current:
            if current.val == value:
                return current
            current = current.next  # Move to the next node
        return None


def int_to_bin(n: int, num_bits: int = 32):
    """ Convert an integer to its binary representation as a 32-bit string. """
    # Handle the case for zero explicitly
    if n == 0:
        return "0".zfill(num_bits)  # Ensure it returns a padded zero string
    # Convert the absolute integer to binary and remove the '0b' prefix, then pad with zeros to ensure it has num_bits length
    bin_str = bin(abs(n))[2:].zfill(num_bits)
    # If the number is negative, perform two's complement conversion
    if n < 0:
        # Invert the bits: change '0' to '1' and '1' to '0'
        inverted = "".join("1" if bit == "0" else "0" for bit in bin_str)
        # Convert the inverted binary string back to an integer, add 1 for two's complement
        inverted = int(inverted, 2) + 1
        # Convert the resulting integer back to a binary string and pad with zeros
        bin_str = bin(inverted)[2:].zfill(num_bits)
    return bin_str


def bin_to_int(binary: str, num_bits: int = 32) -> int:
    """
    Convert a binary string in two's complement representation to a signed integer.

    In the context of converting a binary number represented in two's complement form 
    to its signed integer value, the general formula is:

    Signed Integer Value = Unsigned Integer Value - 2^num_bits

    Explanation:
    - Unsigned Integer Value: This is the integer representation of the binary string 
      as if it were a positive number.
    - Two's Complement: In a two's complement representation:
        - If the most significant bit (MSB) is '0', the number is positive, and its 
          integer value remains unchanged.
        - If the MSB is '1', the number is negative. In this case, the unsigned 
          integer value exceeds 2^(num_bits - 1), which means the number is negative 
          when interpreted as a signed integer.
    """
    # Raise a ValueError if the length of the binary string does not match the expected number of bits.
    if len(binary) != num_bits:
        raise ValueError(f"Binary string must be exactly {num_bits} bits.")
    # Convert the binary string to its unsigned integer equivalent using base 2.
    # This gives us the decimal representation of the binary number as if it were positive.
    unsigned_value = int(binary, 2)
    # Check if the most significant bit (MSB) is 1 (indicating a negative number)
    if binary[0] == '1':
        # The subtraction converts this high positive value to the corresponding negative value, so return the adjusted integer value in two's complement form
        return unsigned_value - (2 ** num_bits)
        # Alternatively from the rule:
        # - 1 << num_bits ==> 1 * 2^num_bits and 1 >> num_bits ==> 1 / 2^num_bits
        # return unsigned_value - (1 << num_bits)
    else:  # If the MSB is '0', it's a non-negative number
        return unsigned_value
