def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    for num in nums:
        if num == 7:
            return True
    else:
        return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
print("should be true", any7([2, 3, 4, 5, 6, 7, 8, 9]))
