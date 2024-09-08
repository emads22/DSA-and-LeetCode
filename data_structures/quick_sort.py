from typing import TypeVar

# Define a generic type variable that can be used to specify the type of list elements
ItemType = TypeVar('ItemType')


def pivot(a_list: list[ItemType], pivot_idx: int, end_idx: int) -> int:
    """
    Rearranges elements in a sublist based on the pivot value, which is the element at pivot_idx.
    All elements smaller than the pivot are moved to the left, and all larger elements to the right.

    Args:
        a_list (list[ItemType]): The list of elements to be sorted.
        pivot_idx (int): The index of the pivot element.
        end_idx (int): The last index of the sublist to be processed.

    Returns:
        int: The new index of the pivot element after rearrangement.
    """
    swap_idx = pivot_idx  # The index where the next smaller element will be placed
    # Loop through the sublist to compare each element with the pivot
    for i in range(pivot_idx + 1, end_idx + 1):
        # If an element is smaller than the pivot, move it to the left of the pivot
        if a_list[i] < a_list[pivot_idx]:
            swap_idx += 1
            a_list[swap_idx], a_list[i] = a_list[i], a_list[swap_idx]
    # Swap the pivot element with the element at swap_idx to position it correctly but only if the pivot is not already in its correct position
    if swap_idx != pivot_idx:
        a_list[pivot_idx], a_list[swap_idx] = a_list[swap_idx], a_list[pivot_idx]
    return swap_idx  # Return the updated index of the pivot


def quick_sort(a_list: list[ItemType]) -> list[ItemType]:
    """
    Sorts a list using the QuickSort algorithm. This function serves as the main entry point
    and uses a helper function to perform the recursive sorting.

    Args:
        a_list (list[ItemType]): The list of elements to be sorted.

    Returns:
        list[ItemType]: The sorted list.
    """

    def _quick_sort(a_list: list[ItemType], start_idx: int, end_idx: int) -> list[ItemType]:
        """
        A recursive helper function to perform the QuickSort algorithm. It divides the list into
        sublists around a pivot, and recursively sorts the sublists.

        Args:
            a_list (list[ItemType]): The list of elements to be sorted.
            start_idx (int): The starting index of the sublist to be sorted.
            end_idx (int): The ending index of the sublist to be sorted.

        Returns:
            list[ItemType]: The sorted sublist.
        """
        if start_idx < end_idx:
            # Partition the list and find the pivot's correct position
            pivot_idx = pivot(a_list, start_idx, end_idx)
            # Recursively sort the sublist before the pivot
            _quick_sort(a_list, start_idx, pivot_idx - 1)
            # Recursively sort the sublist after the pivot
            _quick_sort(a_list, pivot_idx + 1, end_idx)
        return a_list  # Return the sorted list

    # Call the helper function on the entire list and return the sorted list
    return _quick_sort(a_list, 0, len(a_list) - 1)


def main():
    """
    Main function to test the quick_sort function with various cases.
    """
    # Test case 1: Sorting an unsorted list of integers
    print("\n\n==> Test case 1: Sorting an unsorted list of integers\n")
    list1 = [45, 12, 78, 23, 56, 89, 34]
    print(f"  . Original list: {list1}")
    sorted_list1 = quick_sort(list1)
    print(f"  . Sorted list: {sorted_list1}\n")
    print("-" * 60)

    # Test case 2: Sorting a list with negative integers
    print("\n\n==> Test case 2: Sorting a list with negative integers\n")
    list2 = [-12, 5, -9, 7, 0, -2, 3]
    print(f"Original list: {list2}")
    sorted_list2 = quick_sort(list2)
    print(f"Sorted list: {sorted_list2}\n")
    print("-" * 60)

    # Test case 3: Sorting a list that is already sorted
    print("\n\n==> Test case 3: Sorting a list that is already sorted\n")
    list3 = [10, 20, 30, 40, 50, 60]
    print(f"Original list: {list3}")
    sorted_list3 = quick_sort(list3)
    print(f"Sorted list: {sorted_list3}\n")
    print("-" * 60)

    # Test case 4: Sorting a list with duplicate values
    print("\n\n==> Test case 4: Sorting a list with duplicate values\n")
    list4 = [8, 2, 4, 2, 7, 6, 6]
    print(f"Original list: {list4}")
    sorted_list4 = quick_sort(list4)
    print(f"Sorted list: {sorted_list4}\n")
    print("-" * 60)

    # Test case 5: Sorting an empty list
    print("\n\n==> Test case 5: Sorting an empty list\n")
    list5 = []
    print(f"Original list: {list5}")
    sorted_list5 = quick_sort(list5)
    print(f"Sorted list: {sorted_list5}\n")
    print("-" * 60)

    # Test case 6: Sorting a list with only one element
    print("\n\n==> Test case 6: Sorting a list with only one element\n")
    list6 = [99]
    print(f"Original list: {list6}")
    sorted_list6 = quick_sort(list6)
    print(f"Sorted list: {sorted_list6}\n")
    print("-" * 60)


if __name__ == "__main__":
    main()
