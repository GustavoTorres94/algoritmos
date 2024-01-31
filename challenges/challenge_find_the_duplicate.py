def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) <= 1:
        return False
    set_numbers = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in set_numbers:
            return True
        set_numbers.add(num)
    return False


find_duplicate([1, 3, 4, 2, 2])
