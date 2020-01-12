def find_val_left(nums, val, start, end, L):
    mid = (start + end) // 2

    if start >= end:
        return -1
    if start == end - 1:
        if nums[mid] == val:
            return val
        else:
            return -1
    if mid == 0:
        prev = val + 1
    else:
        prev = nums[mid]

    if prev == val:
        if end - start == 2:
            return mid - 1
        return find_val_left(nums, val, start, mid + 1, L)

    if nums[mid] == val:
        return mid
    elif nums[mid] > val:
        return find_val_left(nums, val, start, mid, L)
    else:
        return find_val_left(nums, val, mid + 1, end, L)


def find_val_right(nums, val, start, end, L):
    mid = (start + end) // 2

    if start >= end:
        return -1

    if start == end - 1:
        if nums[mid] == val:
            return val
        else:
            return -1
    if mid == L - 1:
        next = val - 1
    else:
        next = nums[mid + 1]

    if next == val:
        if end - start == 2:
            return mid + 1
        return find_val_right(nums, val, mid, end, L)

    if nums[mid] == val:
        return mid
    elif nums[mid] > val:
        return find_val_right(nums, val, start, mid, L)
    else:
        return find_val_right(nums, val, mid + 1, end, L)


def searchRange(nums, target):
    L = len(nums)
    if L == 0:
        return [-1, -1]

    if L == 1:
        if nums[0] == 8:
            return [0, 0]

    left = find_val_left(nums, target, 0, L, L)

    if left == -1:
        return [-1, -1]

    if left == L - 1:
        return [left, left]

    right = find_val_right(nums, target, 0, L, L)

    return [left, right]


searchRange([5, 7, 7, 8, 8, 10], 8)
