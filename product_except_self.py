def productExceptSelf(nums):
    L = len(nums)
    if L == 1:
        return [1]

    if L == 2:
        return [nums[1], nums[0]]

    output = [1] * L

    for i in range(len(nums) - 2, -1, -1):
        output[i] = output[i + 1] * nums[i + 1]

    left_product = 1

    for i in range(1, L):
        left_product *= nums[i - 1]
        output[i] *= left_product

    return output

print(productExceptSelf([1,2,3,4]))