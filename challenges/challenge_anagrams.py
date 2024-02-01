def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    arr1 = list(first_string.lower())
    arr2 = list(second_string.lower())

    arr1_sorted = quick_sort(arr1)
    arr2_sorted = quick_sort(arr2)

    str1_sorted = "".join(arr1_sorted)
    str2_sorted = "".join(arr2_sorted)

    return str1_sorted, str2_sorted, str1_sorted == str2_sorted


print(is_anagram("amor", ""))
