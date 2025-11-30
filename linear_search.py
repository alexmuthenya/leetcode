def linear_search(arr, target):
    """
    Perform a linear search over a list to find the index of a target value.

    Parameters:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        int or None: The index of the target if found, otherwise None.

    Description:
        Linear search checks each element in the list one by one.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    # Iterate through every index in the array
    for i in range(len(arr)):
        # If the element matches the target, return the index
        if arr[i] == target:
            return i

    # If the loop completes, the target was not found
    return None


def verify(index):
    """
    Print the result of the linear search.

    Parameters:
        index (int or None): The returned index from linear_search.
    """

    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list")


# Example usage
arr = [x for x in range(1, 11)]
index = linear_search(arr, 5)
verify(index)
