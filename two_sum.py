def twoSum(nums, target):

    for index, num in enumerate(nums):
        minuend = target - num
        try:
            minuend_index = nums.index(minuend)
        except:
            continue
        if minuend in nums and minuend_index != index:
            return [minuend_index, index ]
            

print(twoSum(nums=[3,2,3], target=6))