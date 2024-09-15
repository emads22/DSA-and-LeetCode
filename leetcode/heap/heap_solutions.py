import sys
from pathlib import Path

# Get the absolute path of the main_project directory
main_project_path = Path(__file__).resolve().parent.parent.parent

# Add the main_project directory to sys.path
sys.path.append(str(main_project_path))


from data_structures import MaxHeap


class Solution:
    """
    A class that provides solutions for operations on a max-heap.
    """

    def find_kth_smallest(self, nums: list[int], k: int) -> int:
        """
        Finds the kth smallest number in a list using a max-heap.

        Args:
            nums (list[int]): The list of integers to search.
            k (int): The position (1-based) of the smallest number to find.

        Returns:
            int: The kth smallest number in the list.
        """
        # # METHOD 1
        # # Create a max-heap to store elements.
        # max_heap = MaxHeap()
        # # Insert all numbers into the max-heap.
        # for num in nums:
        #     max_heap.insert(num)
        # # Remove elements from the heap until only k smallest elements remain.
        # for _ in range(max_heap.size() - k):
        #     max_heap.remove()
        # # The kth smallest element will now be at the root of the max-heap.
        # return max_heap.heap[0]

        # Time Complexity:
        #     O(n log n): Where n is the number of elements in nums.
        #     - Insertion: O(n log n) for inserting n elements into the max-heap.
        #     - Removal: O((n - k) log n) for removing the (n - k) largest elements to leave the kth smallest.

        # METHOD 2
        # Create a max-heap to store up to k smallest elements.
        max_heap = MaxHeap()
        # Insert each number into the max-heap.
        for num in nums:
            max_heap.insert(num)
            # If the heap size exceeds k, remove the largest element.
            if max_heap.size() > k:
                max_heap.remove()
        # The kth smallest element is now the root of the max-heap.
        return max_heap.heap[0]

        # Time Complexity:
        #     O(n log k): Where n is the number of elements in nums and k is the size of the heap.
        #     - Insertion: O(n log k) for inserting n elements into a max-heap of size k.
        #     - Removal: O(n log k) since each insertion may trigger a removal when the heap size exceeds k.

    def stream_max(self, nums: list[int]) -> list[int]:
        """
        Computes a list where each element is the maximum number seen so far in the input list.

        Parameters:
        nums (list[int]): A list of integers.

        Returns:
        list[int]: A list of integers where each element is the maximum number seen so far 
                in the input list up to that index.
        """
        # Initialize a max heap
        max_heap = MaxHeap()
        # Initialize an empty output list
        output_list = []
        # Iterate through each number in the input list
        for num in nums:
            # Insert the current number into the max heap
            max_heap.insert(num)
            # The maximum element so far will be at the root of the max heap
            output_list.append(max_heap.heap[0])
        return output_list  # Return the max stream output list


def main():
    solution = Solution()

    # Test: find_kth_smallest
    print("\n==> Test: find_kth_smallest()\n")

    test_cases = {
        # Expected output: 4
        "Basic test 1": {"nums": [7, 10, 4, 3, 20, 15], "k": 2},
        # Expected output: 10
        "Basic test 2": {"nums": [7, 10, 4, 3, 20, 15], "k": 4},
        # Expected output: 3
        "Edge case with smallest element": {"nums": [7, 10, 4, 3, 20, 15], "k": 1},
        # Expected output: 20
        "Edge case with largest element": {"nums": [7, 10, 4, 3, 20, 15], "k": 6},
        # Expected output: 10
        "Large array": {"nums": [15, 10, 4, 8, 30, 12, 22, 5, 17, 3, 20], "k": 5},
        "Single element array": {"nums": [42], "k": 1},  # Expected output: 42
    }

    for case, params in test_cases.items():
        print(
            f"\t- {case}:\n\t\t. nums: {params['nums']} and K: {params['k']}\n")
        print(f"\t\t. Kth smallest: {
              solution.find_kth_smallest(params['nums'], params['k'])}\n")

    print("-" * 80)

    # Test: stream_max
    print("\n==> Test: stream_max()\n")

    solution = Solution()

    test_cases = {
        # Expected output: [1, 2, 3, 4, 5]
        "Simple increasing array": [1, 2, 3, 4, 5],
        # Expected output: [5, 5, 5, 5, 5]
        "Simple decreasing array": [5, 4, 3, 2, 1],
        "Mixed values": [1, 5, 3, 9, 2],  # Expected output: [1, 5, 5, 9, 9]
        # Expected output: [2, 2, 2, 2, 2]
        "Array with duplicates": [2, 2, 2, 2, 2],
        # Expected output: [-1, 3, 3, 7, 7]
        "Mixed positive and negative values": [-1, 3, -5, 7, 0],
        "Single element array": [42],  # Expected output: [42]
    }

    for case, nums in test_cases.items():
        print(f"\t- {case}:\n\t\t. nums: {nums}")
        print(f"\t\t. Stream max: {solution.stream_max(nums)}\n")

    print("-" * 80)


if __name__ == "__main__":
    main()
