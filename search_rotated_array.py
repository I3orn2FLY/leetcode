def find_pivot(nums, val, start, end):
    mid = (start + end) // 2
    if end - start == 1:
        return start

    if end - start == 2:
        if nums[start + 1] > nums[start]:
            return start
        else:
            return start + 1

    if nums[mid - 1] > nums[mid]:
        return mid
    elif val > nums[mid]:
        return find_pivot(nums, val, start, mid + 1)
    else:
        return find_pivot(nums, val, mid, end)

def find_target(nums, val, start, end):
    mid = (start + end) // 2
    if start == end - 1:
        if nums[start] == val:
            return start
        else:
            return -1

    if start > end - 1:
        return -1

    if val == nums[mid]:
        return mid
    elif val > nums[mid]:
        return find_target(nums, val, mid + 1, end)
    else:
        return find_target(nums, val, start, mid)


def search(nums, target: int) -> int:
    if not nums:
        return -1

    if nums[0] == target:
        return 0

    if nums[-1] == target:
        return len(nums) - 1

    if len(nums) < 3:
        return -1

    if len(nums) == 3:
        if nums[1] == target:
            return 1
        else:
            return -1

    mid = len(nums) // 2
    if nums[-1] > nums[0]:
        return find_target(nums, target, 0, len(nums))

    if nums[-1] > nums[mid] and nums[0] > nums[mid]:
        pivot = find_pivot(nums, nums[0], 0, len(nums))
    else:
        pivot = find_pivot(nums, nums[0], 0, len(nums))

    # pivot = 4

    offset = find_target(nums[pivot:] + nums[:pivot], target, 0, len(nums))

    if offset == -1:
        return offset

    return (pivot + offset) % len(nums)


search([3,4,5,6,7,8,1,2], 7)

