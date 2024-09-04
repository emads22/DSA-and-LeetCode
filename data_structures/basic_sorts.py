
def bubble_sort(my_list: list) -> list:
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate from the last element down to the second element
    for i in range(len(my_list) - 1, 0, -1):
        # Iterate through the unsorted portion of the list
        for j in range(i):
            # Swap elements if the current element is greater than the next
            if my_list[j] > my_list[i]:
                my_list[j], my_list[i] = my_list[i], my_list[j]
    return my_list


def selection_sort(my_list: list) -> list:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate over the list, leaving the last element since it will be sorted automatically
    for i in range(len(my_list) - 1):
        min_idx = i  # Assume the current index has the smallest value
        # Iterate through the remaining unsorted elements
        for j in range(i + 1, len(my_list)):
            # Update min_idx if a smaller element is found
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        # Swap the smallest found element with the first unsorted element
        if min_idx != i:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list


def insertion_sort(my_list: list) -> list:
    """
    Sorts a list in ascending order using the insertion sort algorithm.

    Args:
        my_list (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # METHOD 1: Using a forward comparison
    # Iterate over the list starting from the second element
    for i in range(1, len(my_list)):
        j = i
        # Compare the current element with the previous elements and swap if necessary
        while my_list[j] < my_list[j - 1] and j > 0:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j -= 1
    return my_list

    # # METHOD 2: Using a backward comparison
    # # Iterate over the list starting from the second element
    # for i in range(1, len(my_list)):
    #     j = i - 1
    #     # Compare the current element with the previous elements and swap if necessary
    #     while my_list[j] > my_list[j + 1] and j >= 0:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #         j -= 1
    # return my_list
