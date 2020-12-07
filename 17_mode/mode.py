def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    nums_dict = {num: nums.count(num) for num in set(nums)}
    max_value = max(nums_dict.values())
    max_key = [key for key, value in nums_dict.items() if value == max_value]
    return max_key[0]
        
