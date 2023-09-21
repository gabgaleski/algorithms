def find_duplicate(nums):
    if nums is None or len(nums) == 0:
        return False

    order_nums = sorted(nums)
    for i in range(1, len(order_nums)):
        if type(order_nums[i]) != int or order_nums[i] < 0:
            return False

        if order_nums[i] == order_nums[i - 1]:
            return order_nums[i]

    return False


find_duplicate([1, 3, 4, 6, 2])
