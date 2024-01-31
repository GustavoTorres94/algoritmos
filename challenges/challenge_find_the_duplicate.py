def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) <= 1:
        return False
    sorted_num = sorted(nums)
    for i in range(len(sorted_num) - 1):
        if not isinstance(sorted_num[i], int) or sorted_num[i] < 0:
            return False
        if sorted_num[i] == sorted_num[i + 1]:
            return sorted_num[i]
    return False


find_duplicate(["a", "b"])
