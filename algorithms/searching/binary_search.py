from typing import TypeVar

# Define a generic type variable that can be used to specify the type of list elements
ItemType = TypeVar('ItemType')


def binary_search(arr: list[ItemType], target: ItemType) -> int:
    """
    Perform a binary search on a sorted array to find the target.

    Parameters:
    arr (list): A list of elements sorted in ascending order.
    target (int/float): The element to search for in the array.

    Returns:
    int: The index of the target if found, otherwise -1 if the target is not in the array.
    """
    # Define the start and end indices
    start, end = 0, len(arr) - 1
    # Loop until the search space is exhausted
    while start <= end:
        mid = (start + end) // 2  # Find the middle index
        # If target is smaller, ignore the end half
        if target < arr[mid]:
            end = mid - 1
        # If target is greater, ignore the start half
        elif target > arr[mid]:
            start = mid + 1
        # Check if the target is at the middle
        else:  # arr[mid] == target
            return mid  # Target found, return the index
    return -1  # Target not found

    # Time complexity: O(log n) - The search space is halved with each iteration.
    # Space complexity: O(1) - Only a constant amount of extra space is used.


def r_binary_search(arr: list[ItemType], target: ItemType) -> int:
    """
    Perform a recursive binary search on a sorted array to find the target.

    Parameters:
    arr (list[ItemType]): A list of elements sorted in ascending order.
    target (ItemType): The element to search for in the array.

    Returns:
    int: The index of the target if found; otherwise, -1 if the target is not in the array.
    """
    def _binary_search(arr: list[ItemType], target: ItemType, start: int, end: int) -> int:
        """
        Helper function to perform the binary search recursively.

        Parameters:
        arr (list[ItemType]): The array to search within.
        target (ItemType): The target element to find.
        start (int): The starting index of the current search range.
        end (int): The ending index of the current search range.

        Returns:
        int: The index of the target if found; otherwise, -1.
        """
        # Base case: If the search range is invalid, return -1
        if start > end:
            return -1
        # Calculate the middle index of the current search range
        mid = (start + end) // 2
        # If the target is less than the middle element, search in the left half
        if target < arr[mid]:
            return _binary_search(arr, target, start, mid - 1)
        # If the target is greater than the middle element, search in the right half
        elif target > arr[mid]:
            return _binary_search(arr, target, mid + 1, end)
        # If the target is equal to the middle element, return the middle index
        else:
            return mid
    # Start the binary search with the entire range of the array
    return _binary_search(arr, target, 0, len(arr) - 1)

    # Time complexity: O(log n) - The search space is halved with each recursive call.
    # Space complexity: O(log n) - Due to the recursion stack in the worst case.


def main():
    """
    Main function to test the binary_search function with different cases.
    It tests both successful and unsuccessful searches, including edge cases.
    """
    print("\n==> Test case 1: Basic search in a sorted array\n")
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target1 = 5
    print(f"\t. Iterative Search for `{target1}` in {arr1}:")
    print(f"\t. Index {binary_search(arr1, target1)}\n")
    print(f"\t. Recursive Search for `{target1}` in {arr1}:")
    print(f"\t. Index {r_binary_search(arr1, target1)}\n")
    print("-" * 80)

    print("\n==> Test case 2: Target not in the array\n")
    target2 = 10
    print(f"\t. Iterative Search for `{target2}` in {arr1}:")
    print(f"\t. Index {binary_search(arr1, target2)} (target not found)\n")
    print(f"\t. Recursive Search for `{target2}` in {arr1}:")
    print(f"\t. Index {r_binary_search(arr1, target2)} (target not found)\n")
    print("-" * 80)

    print("\n==> Test case 3: Empty array\n")
    arr2 = []
    target3 = 1
    print(f"\t. Iterative Search for `{target3}` in empty array:")
    print(f"\t. Index {binary_search(arr2, target3)} (target not found)\n")
    print(f"\t. Recursive Search for `{target3}` in empty array:")
    print(f"\t. Index {r_binary_search(arr2, target3)} (target not found)\n")
    print("-" * 80)

    print("\n==> Test case 4: One element, target present\n")
    arr3 = [42]
    target4 = 42
    print(f"\t. Iterative Search for `{target4}` in {arr3}:")
    print(f"\t. Index {binary_search(arr3, target4)}\n")
    print(f"\t. Recursive Search for `{target4}` in {arr3}:")
    print(f"\t. Index {r_binary_search(arr3, target4)}\n")
    print("-" * 80)

    print("\n==> Test case 5: One element, target not present\n")
    target5 = 99
    print(f"\t. Iterative Search for `{target5}` in {arr3}:")
    print(f"\t. Index {binary_search(arr3, target5)} (target not found)\n")
    print(f"\t. Recursive Search for `{target5}` in {arr3}:")
    print(f"\t. Index {r_binary_search(arr3, target5)} (target not found)\n")
    print("-" * 80)

    print("\n==> Test case 6: Array with negative numbers\n")
    arr4 = [-10, -5, 0, 5, 10]
    target6 = -5
    print(f"\t. Iterative Search for `{target6}` in {arr4}:")
    print(f"\t. Index {binary_search(arr4, target6)}\n")
    print(f"\t. Recursive Search for `{target6}` in {arr4}:")
    print(f"\t. Index {r_binary_search(arr4, target6)}\n")
    print("-" * 80)

    print("\n==> Test case 7: Array with duplicate elements (binary search will return any valid index)\n")
    arr5 = [2, 4, 4, 4, 6, 8]
    target7 = 4
    print(f"\t. Iterative Search for `{target7}` in {arr5}:")
    print(f"\t. Index {binary_search(arr5, target7)
                       } (one of the occurrences)\n")
    print(f"\t. Recursive Search for `{target7}` in {arr5}:")
    print(f"\t. Index {r_binary_search(
        arr5, target7)} (one of the occurrences)\n")
    print("-" * 80)


if __name__ == "__main__":
    main()
