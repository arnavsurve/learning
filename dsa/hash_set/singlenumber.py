def singleNumber(nums):
    unique_element = 0
    for i in nums:
        unique_element ^= i

    return unique_element

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
