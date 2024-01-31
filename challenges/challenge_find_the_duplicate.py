def find_duplicate(nums):
    sorted_nums = sorted(nums)
    if not isinstance(nums, list) or len(nums) == 1:
        return False
    for i in range(len(sorted_nums)):
        if not isinstance(sorted_nums[i], int):
            return False
        if sorted_nums[i] < 0:
            return False
        if sorted_nums[i] == sorted_nums[i + 1]:
            return print(sorted_nums[i])
    return False


find_duplicate([1, 3, 4, 2, 2])
