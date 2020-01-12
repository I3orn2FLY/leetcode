def maxProduct(nums) -> int:
    r = nums[0]
    min_p = nums[0]
    max_p = nums[0]
    for num in nums[1:]:
        min_p, max_p = min([num, num * min_p, num * max_p]), max([num, num * min_p, num * max_p])
        r = max(r, max_p)

    return r



maxProduct([2,3,-2,4])