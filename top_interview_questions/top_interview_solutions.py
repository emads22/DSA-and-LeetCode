from typing import List
from utils import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string, the input string is given as an array of characters s.
        Do not return anything, modify s in-place instead.
        """
        end = len(s)
        mid = end // 2

        for i in range(mid):
            s[i], s[end-1-i] = s[end-1-i], s[i]

    def fizzBuzz(self, n: int) -> List[str]:
        """
        Generate a List of strings representing the FizzBuzz sequence.

        For each number from 1 to n:
        - If the number is divisible by 3, append "Fizz".
        - If the number is divisible by 5, append "Buzz".
        - If the number is divisible by both, append "FizzBuzz".
        - Otherwise, append the number as a string.
        """
        output = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))

        return output

    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number in a List where every other number appears twice.

        Using the XOR operation to identify the unique number in the List, 
        as XOR of two identical numbers is zero and XOR of a number and
        zero is the number itself.
        """
        result = 0

        for num in nums:
            # Using XOR (exclusive OR: `0 ^ 0 = 0` and `1 ^ 1 = 0`, and `0 ^ 1 = 1`)
            result ^= num  # result = result ^ num

        return result

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.
        """
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeroes in the array to the end while maintaining the 
        relative order of the non-zero elements. This is done in-place 
        without making a copy of the array.
        """
        # METHOD 1: Avoids unnecessary checks, does minimal swaps, has fewer conditional checks
        next_non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1

        # # METHOD 2
        # nz = 0  # pointer to position of the next zero
        # for i in range(len(nums)):
        #     # Swap if current is non-zero and nz points to zero
        #     if nums[i] != 0 and nums[nz] == 0:
        #         nums[i], nums[nz] = nums[nz], nums[i]
        #     # Move nz forward if it's non-zero
        #     if nums[nz] != 0:
        #         nz += 1

    def getSum(self, a: int, b: int) -> int:
        """
        Calculate the sum of two integers without using the + or - operators.

        This function uses bitwise operations to achieve the sum. It repeatedly calculates the 
        carry and the sum without carry until there are no carries left.
        """
        while b != 0:
            carry = a & b           # Calculate carry
            a = a ^ b               # Sum without carry
            b = carry << 1          # Shift carry to the left

        return a                     # Return the final sum

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.
        """
        # METHOD 1: ITERATIVE
        before = None  # Initialize 'before' as None, will be the new head
        current = head  # Start traversing from the head

        while current is not None:
            after = current.next  # Store the next node
            current.next = before  # Reverse the current node's pointer
            before = current  # Move 'before' one step forward
            current = after  # Move 'current' one step forward

        # The 'before' pointer will be the new head of the reversed list
        return before

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # # METHOD 2: RECURSIVE
        # # Base case: If the list is empty or has only one node
        # if head is None or head.next is None:
        #     return head
        # # Recursively reverse the rest of the list
        # new_head = self.reverseList(head.next)
        # # Reverse the current node's pointer
        # head.next.next = head
        # head.next = None
        # return new_head

        # Time Complexity: O(n)
        # Space Complexity: O(n)

    def deleteNode(self, node: ListNode) -> None:
        """
        Delete the given node from the linked list.
        Given the node to be deleted node with no access to the first node or head.
        It does not return anything, modifies node in-place instead.
        """
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an in-order traversal of a binary tree.
        """
        # METHOD 1: RECURSIVE
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # # METHOD 2: ITERATIVE
        # if root is None:
        #     return []  # Return an empty list if the tree is empty
        # stack = []  # Stack to keep track of nodes
        # output = []  # List to store the in-order traversal result
        # current = root  # Start with the root node
        # # Continue the loop until there are no nodes left to process
        # while stack or current:
        #     # Traverse to the leftmost node
        #     while current:
        #         stack.append(current)  # Push current node to the stack
        #         current = current.left  # Move to the left child
        #     # Pop the node from the stack (it will be the next node in in-order)
        #     current = stack.pop()
        #     output.append(current.val)  # Add the node's value to the output
        #     # Move to the right subtree
        #     current = current.right
        # return output  # Return the list containing the in-order traversal

    def titleToNumber(self, columnTitle: str) -> int:
        """
        Convert Excel column title to corresponding column number.

        In any base `b` system, when we multiply by `b`, we are shifting the digits left by one place.
        Here we want to "shift" letters in a base-26 system, we are essentially moving to a higher place value, 
        much like we do in decimal when we shift digits left.

        In the context of Excel columns:
        . If we have a current column number represented by the characters we processed so far (let's say we are at "A" = 1), 
          when we add a new letter (e.g., "B"), we need to shift the existing number (1) left to make room for the new character.
        . we do this by multiplying the current number by 26 before adding the value of the new character.
        """

        # METHOD 1: Accumulating the result using base-26 multiplication
        number = 0

        for letter in columnTitle:
            # Calculate the value of each letter ('A' = 1, 'B' = 2, ..., 'Z' = 26)
            value = ord(letter) - ord('A') + 1
            # Shift the current number by multiplying by 26, then add the current letter's value
            number = number * 26 + value

        return number

        # # METHOD 2: Positional calculation using base-26 powers
        # number = 0
        # # Start from the leftmost character, set position to track powers of 26
        # pos = len(columnTitle) - 1
        # for letter in columnTitle:
        #     # Calculate the value of each letter ('A' = 1, 'B' = 2, ..., 'Z' = 26)
        #     value = ord(letter) - ord('A') + 1
        #     # Multiply the value by 26 raised to the power of its position
        #     number += value * (26 ** pos)
        #     # Decrease the position for the next letter
        #     pos -= 1
        # return number

    def reverseBits(self, n: int) -> int:
        """ Reverses the bits of a given 32-bit unsigned integer. """

        # # METHOD 1
        # # Create a list to store binary digits (initialized with '0')
        # # better than str and inefficient concatenation
        # s = ["0"] * 32
        # num = 0
        # i = 0
        # while n != 0:  # Convert the integer to binary
        #     s[i] = str(n % 2)  # Store the least significant bit
        #     n = n // 2  # Divide by 2 to shift right
        #     i += 1  # Move to the next index in the list

        # for bit in s:  # Convert the binary list back to an integer
        #     num = (num * 2) + int(bit)  # Build the integer from binary digits
        # return num

        # # METHOD 2
        # # Create a list to store binary digits (initialized with '0')
        # s = ["0"] * 32
        # num = 0
        # i = 0
        # while n != 0:  # Convert the integer to binary
        #     s[i] = str(n % 2)  # Store the least significant bit
        #     n = n // 2  # Divide by 2 to shift right
        #     i += 1  # Move to the next index in the list
        # # Join the list into a string and convert to an integer
        # return int("".join(s), 2)

        # METHOD 3: efficient
        # Get binary string of n, pad with zeros
        bin_str = bin(abs(n))[2:].zfill(32)
        # Reverse the string and convert back to an integer
        reversed_n = int(bin_str[::-1], 2)

        if n < 0:  # Check if the original number is negative
            return -reversed_n  # Return the negative of the reversed number

        return reversed_n  # Return the reversed number

        # # METHOD 4: Optimized version, most efficient
        # reversed_n = 0  # Initialize the result to 0
        # for _ in range(32):  # Process each bit (32 bits in total)
        #     # Shift reversed_n left by 1 and add the least significant bit of n
        #     # Add the LSB of n to reversed_n
        #     reversed_n = (reversed_n << 1) | (n & 1)
        #     n >>= 1  # Shift n right by 1 to process the next bit
        # return reversed_n  # Return the reversed bits as an integer

    def reverse(self, x: int) -> int:
        """ Reverse the digits of a signed 32-bit integer. """

        is_negative = x < 0  # Check if the number is negative

        # Reverse the string representation of the absolute value of x
        r = str(abs(x))[::-1]

        # Convert the reversed string back to an integer
        r = int(r)

        # Check for overflow; if the reversed integer is out of the 32-bit signed integer bounds
        if r < -2**31 or r > 2**31 - 1:
            return 0  # Return 0 if the reversed integer overflows

        # Restore the sign if the original number was negative and return the result
        return -r if is_negative else r

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in-place.
        The function does not return anything; it modifies the nums array in-place.

        1. Pop and Insert Method:
        - Time Complexity: O(n * k), where n is the length of the array.
        - Space Complexity: O(1) (constant extra space).

        2. Slicing with Reassignment in Loop:
        - Time Complexity: O(n * k), as the list is sliced and reassigned k times.
        - Space Complexity: O(n) (due to slicing creating new lists).

        3. Optimized Slicing:
        - Time Complexity: O(n), as the array is rotated in one slicing operation.
        - Space Complexity: O(n) (due to slicing creating new lists).
        """

        # # METHOD 1: Pop and Insert
        # # Rotate by popping the last element and inserting it at the beginning.
        # # Repeats k times (inefficient for large k).
        # k = k % len(nums)  # Ensure k is within bounds of the array length.
        # for _ in range(k):
        #     # Pop the last element and insert it at the start.
        #     popped = nums.pop()
        #     nums.insert(0, popped)

        # # METHOD 2: Slicing with Reassignment in a Loop
        # # Shift the entire list by one position to the right, repeat k times.
        # # Each iteration reassigns the list using slicing (inefficient for large k).
        # k = k % len(nums)  # Ensure k is within bounds of the array length.
        # while k > 0:
        #     # Take the last element, put it at the front, and adjust the rest of the array.
        #     nums[:] = [nums[-1]] + nums[:-1]
        #     k -= 1

        # METHOD 3: Optimized Slicing
        # The most efficient method which rotates the array using slicing.
        # This operation is done in one step, making it O(n) time complexity.
        k = k % len(nums)  # Ensure k is within bounds of the array length.
        nums[:] = nums[-k:] + nums[:-k]  # Perform the rotation in one step.

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find indices of the two numbers in nums that add up to target.
        """
        # Dict to store numbers and their indices (hash table structure)
        sum_idx = {}

        for idx, num in enumerate(nums):
            # Calculate the required complement and check if it  exists in dict.
            complement = target - num

            if complement in sum_idx:
                # Return the indices if found.
                return [sum_idx[complement], idx]

            # Otherwise store the current number and its index.
            sum_idx[num] = idx

        return []  # Return an empty list if no solution is found

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted linked lists into one sorted linked list."""
        # Create a dummy node to simplify merging
        current = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                # Attach list1 node to merged list
                current.next = list1
                list1 = list1.next  # Advance list1
            else:
                # Attach list2 node to merged list
                current.next = list2
                list2 = list2.next  # Advance list2

            current = current.next  # Move current pointer

        # Attach remaining nodes from non-exhausted list
        current.next = list1 or list2

        # Return merged list starting from the dummy's next
        return dummy.next
