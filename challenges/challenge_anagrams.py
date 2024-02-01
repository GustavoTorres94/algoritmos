def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    arr1 = list(first_string.lower())
    arr2 = list(second_string.lower())

    merge_sort(arr1)
    merge_sort(arr2)

    str1_sorted = "".join(arr1)
    str2_sorted = "".join(arr2)

    return str1_sorted, str2_sorted, str1_sorted == str2_sorted


is_anagram("amor", "roma")
