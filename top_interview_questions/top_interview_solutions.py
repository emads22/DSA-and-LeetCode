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
        next_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1

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
