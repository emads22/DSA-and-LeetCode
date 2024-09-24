from typing import TypeVar

# Define a generic type variable that can be used to specify the type of list elements
ItemType = TypeVar('ItemType')


def merge(list1: list[ItemType], list2: list[ItemType]) -> list[ItemType]:
    """
    Merge two sorted lists into one sorted list.

    Args:
        list1 (list[ItemType]): The first sorted list.
        list2 (list[ItemType]): The second sorted list.

    Returns:
        list[ItemType]: A single merged list that contains all elements 
                        from list1 and list2 in sorted order.
    """
    combined = []  # List to store the merged result
    i = j = 0  # Pointers to iterate over list1 and list2

    # Merge elements from both lists until one list is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])  # Add element from list1
            i += 1
        else:
            combined.append(list2[j])  # Add element from list2
            j += 1

    # If there are remaining elements in list1, add them to the result
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # If there are remaining elements in list2, add them to the result
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(a_list: list[ItemType]) -> list[ItemType]:
    """
    Perform a merge sort on a list, dividing it into smaller sublists,
    sorting them, and then merging the sorted sublists.

    Args:
        a_list (list[ItemType]): The list to be sorted.

    Returns:
        list[ItemType]: The sorted list.
    """
    # Base case: a list of length 1 is already sorted (or even empty list)
    if len(a_list) <= 1:
        return a_list

    # Find the middle index to divide the list into two halves
    mid_idx = len(a_list) // 2

    # Recursively sort both halves
    left = merge_sort(a_list[:mid_idx])
    right = merge_sort(a_list[mid_idx:])

    # Merge the two sorted halves and return the result
    return merge(left, right)


def main():
    """
    Main function to test the merge_sort function with various cases.
    """
    # Test case 1: Sorting an unsorted list of integers
    print("\n\n==> Test case 1: Sorting an unsorted list of integers\n")
    list1 = [38, 27, 43, 3, 9, 82, 10]
    print(f"  . Original list: {list1}")
    sorted_list1 = merge_sort(list1)
    print(f"  . Sorted list: {sorted_list1}\n")
    print("-" * 60)

    # Test case 2: Sorting a list with negative integers
    print("\n\n==> Test case 2: Sorting a list with negative integers\n")
    list2 = [-3, -1, -7, -5, 2, 6, 4]
    print(f"Original list: {list2}")
    sorted_list2 = merge_sort(list2)
    print(f"Sorted list: {sorted_list2}\n")
    print("-" * 60)

    # Test case 3: Sorting a list that is already sorted
    print("\n\n==> Test case 3: Sorting a list that is already sorted\n")
    list3 = [1, 2, 3, 4, 5, 6]
    print(f"Original list: {list3}")
    sorted_list3 = merge_sort(list3)
    print(f"Sorted list: {sorted_list3}\n")
    print("-" * 60)

    # Test case 4: Sorting a list with duplicate values
    print("\n\n==> Test case 4: Sorting a list with duplicate values\n")
    list4 = [5, 1, 3, 1, 2, 5, 4]
    print(f"Original list: {list4}")
    sorted_list4 = merge_sort(list4)
    print(f"Sorted list: {sorted_list4}\n")
    print("-" * 60)

    # Test case 5: Sorting an empty list
    print("\n\n==> Test case 5: Sorting an empty list\n")
    list5 = []
    print(f"Original list: {list5}")
    sorted_list5 = merge_sort(list5)
    print(f"Sorted list: {sorted_list5}\n")
    print("-" * 60)

    # Test case 6: Sorting a list with only one element
    print("\n\n==> Test case 6: Sorting a list with only one element\n")
    list6 = [42]
    print(f"Original list: {list6}")
    sorted_list6 = merge_sort(list6)
    print(f"Sorted list: {sorted_list6}\n")
    print("-" * 60)


if __name__ == "__main__":
    main()
