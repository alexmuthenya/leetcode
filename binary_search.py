def binary_search(arr, target):
    """
    Perform a binary search on a sorted list to find the index of a target value.

    Parameters:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        int or None: The index of the target if found, otherwise None.
    """

    # Ensure the array is sorted before searching
    arr.sort()

    first = 0                   # Start of the search range
    last = len(arr) - 1         # End of the search range

    while first <= last:
        midpoint = (first + last) // 2     # Middle index

        # Check if the midpoint is the target
        if arr[midpoint] == target:
            return midpoint

        # If target is larger, search in the right half
        elif arr[midpoint] < target:
            first = midpoint + 1

        # Otherwise, search in the left half
        else:
            last = midpoint - 1

    # Target not found
    return None


def verify(index):
    """
    Print the result of the binary search.

    Parameters:
        index (int or None): The returned index from binary_search.
    """
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list")


# Example usage
arr = [x for x in range(1, 11)]
index = binary_search(arr, 5)
verify(index)
