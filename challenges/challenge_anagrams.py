def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def is_anagram(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        raise TypeError("As entradas devem ser strings")

    if len(first_string) == 0 or len(second_string) == 0:
        return False

    str1_sorted = "".join(bubble_sort(list(first_string.lower())))
    str2_sorted = "".join(bubble_sort(list(second_string.lower())))

    return str1_sorted, str2_sorted, str1_sorted == str2_sorted
