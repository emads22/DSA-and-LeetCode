from typing import TypeVar

# Define a generic type variable that can be used to specify the type of list elements
ItemType = TypeVar('ItemType')


def linear_search(arr: list[ItemType], target: ItemType) -> int:
    """
    Perform a linear search on an array to find the target.

    Parameters:
    arr (list): A list of elements.
    target (int/float): The element to search for in the array.

    Returns:
    int: The index of the target if found, otherwise -1 if the target is not in the array.
    """
    # Loop through each element in the array
    for index, item in enumerate(arr):
        # Check if the current item matches the target
        if item == target:
            return index  # Target found, return the index
    return -1  # Target not found

    # Time complexity: O(n) - The algorithm checks each element until it finds the target.
    # Space complexity: O(1) - Only a constant amount of extra space is used.


def r_linear_search(arr: list[ItemType], target: ItemType) -> int:
    """
    Perform a recursive linear search on an array to find the target.

    Parameters:
    arr (list): A list of elements of type ItemType.
    target (ItemType): The element to search for in the array.

    Returns:
    int: The index of the target if found; otherwise, -1 if the target is not in the array.
    """

    def _r_linear_search(arr: list[ItemType], target: ItemType, index: int) -> int:
        """
        Helper function to perform the recursive search.

        Parameters:
        arr (list): A list of elements of type ItemType.
        target (ItemType): The element to search for in the array.
        index (int): The current index in the array being checked.

        Returns:
        int: The index of the target if found; otherwise, -1 if the target is not in the array.
        """
        # Base case: If the index reaches the length of the array, the target is not found
        if index >= len(arr):
            return -1
        # Check if the current item matches the target
        if arr[index] == target:
            return index  # Target found, return the index
        # Recur for the next index
        return _r_linear_search(arr, target, index + 1)

    return _r_linear_search(arr, target, index=0)

    # Time complexity: O(n) - The algorithm checks each element until it finds the target.
    # Space complexity: O(n) - Due to the recursive call stack.


def main():
    """
    Main function to test the linear_search function with different cases.
    It tests both successful and unsuccessful searches, including edge cases.
    """
    print("\n==> Test case 1: Basic search in an array of integers\n")
    arr1 = [10, 20, 30, 40, 50, 60]
    target1 = 30
    print(f"\t. Iterative Linear Search for `{target1}` in {arr1}:")
    print(f"\t. Index {linear_search(arr1, target1)}\n")
    print(f"\t. Recursive Linear Search for `{target1}` in {arr1}:")
    print(f"\t. Index {r_linear_search(arr1, target1)}\n")
    print("-" * 80)

    print("\n==> Test case 2: Target not present in the array\n")
    target2 = 25
    print(f"\t. Iterative Linear Search for `{target2}` in {arr1}:")
    print(f"\t. Index {linear_search(arr1, target2)} (target not found)\n")
    print(f"\t. Recursive Linear Search for `{target2}` in {arr1}:")
    print(f"\t. Index {r_linear_search(arr1, target2)} (target not found)\n")
    print("-" * 80)

    print("\n==> Test case 3: Searching in an array with strings\n")
    arr2 = ["apple", "banana", "cherry", "date"]
    target3 = "banana"
    print(f"\t. Iterative Linear Search for `{target3}` in {arr2}:")
    print(f"\t. Index {linear_search(arr2, target3)}\n")
    print(f"\t. Recursive Linear Search for `{target3}` in {arr2}:")
    print(f"\t. Index {r_linear_search(arr2, target3)}\n")
    print("-" * 80)

    print("\n==> Test case 4: Searching in an array with mixed types\n")
    arr3 = [1, "two", 3.0, "four"]
    target4 = 3.0
    print(f"\t. Iterative Linear Search for `{target4}` in {arr3}:")
    print(f"\t. Index {linear_search(arr3, target4)}\n")
    print(f"\t. Recursive Linear Search for `{target4}` in {arr3}:")
    print(f"\t. Index {r_linear_search(arr3, target4)}\n")
    print("-" * 80)

    print("\n==> Test case 5: Empty array\n")
    arr4 = []
    target5 = "anything"
    print(f"\t. Iterative Linear Search for `{target5}` in empty array:")
    print(f"\t. Index {linear_search(arr4, target5)} (target not found)\n")
    print(f"\t. Recursive Linear Search for `{target5}` in empty array:")
    print(f"\t. Index {r_linear_search(arr4, target5)} (target not found)\n")
    print("-" * 80)

    print("\n==> Test case 6: Array with multiple occurrences of the target\n")
    arr5 = [5, 10, 15, 10, 20]
    target6 = 10
    print(f"\t. Iterative Linear Search for `{target6}` in {arr5}:")
    print(f"\t. Index {linear_search(arr5, target6)} (first occurrence)\n")
    print(f"\t. Recursive Linear Search for `{target6}` in {arr5}:")
    print(f"\t. Index {r_linear_search(arr5, target6)} (first occurrence)\n")
    print("-" * 80)

    print("\n==> Test case 7: Large array with random numbers\n")
    arr6 = [i for i in range(100)]  # Large array with numbers from 0 to 999
    target7 = 99
    print(f"\t. Iterative Linear Search for `{target7}` in a large array:")
    print(f"\t. Index {linear_search(arr6, target7)}\n")
    print(f"\t. Recursive Linear Search for `{target7}` in a large array:")
    print(f"\t. Index {r_linear_search(arr6, target7)}\n")
    print("-" * 80)

    print("\n==> Test case 8: Special characters in array\n")
    arr7 = ['!', '@', '#', '$', '%']
    target8 = '$'
    print(f"\t. Iterative Linear Search for `{target8}` in {arr7}:")
    print(f"\t. Index {linear_search(arr7, target8)}\n")
    print(f"\t. Recursive Linear Search for `{target8}` in {arr7}:")
    print(f"\t. Index {r_linear_search(arr7, target8)}\n")
    print("-" * 80)


if __name__ == "__main__":
    main()
