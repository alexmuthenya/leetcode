def twoSum(nums, target):
    """
    Find two distinct indices in a list whose values add up to the given target.

    This function uses a hash map (dictionary) to store previously seen numbers
    and their indices. For each number, it computes the required complement
    (target - current number) and checks if that complement has already been seen.
    If found, the indices of both numbers are returned.

    Time Complexity:
        O(n) — each element is processed once.

    Space Complexity:
        O(n) — the dictionary stores up to n elements in the worst case.

    Args:
        nums (list[int]): List of integers to search through.
        target (int): The sum we are trying to find.

    Returns:
        list[int] | None: A list containing the indices of the two numbers
        that add up to the target. Returns None if no valid pair exists.
    """
    
    seen = {}  # Maps number -> index where it appeared
    
    for i, num in enumerate(nums):
        complement = target - num  # The value needed to reach the target

        # If the complement exists, we found the solution
        if complement in seen:
            return [seen[complement], i]

        # Store the current number with its index
        seen[num] = i

    # No solution found
    return None


nums = [1, 3, 5, 6, 7]
print(twoSum(nums, 14))  # Output: [3, 4] → because nums[3]=6 and nums[4]=7 → 6+7=13
