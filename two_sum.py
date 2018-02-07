# -*- coding:utf-8 -*-
from copy import deepcopy

class Solution(object):

    def twoSum(self, nums, target):
        tmp_nums = deepcopy(nums)
        tmp_nums.sort()
        half_target = target / 2
        i = 0
        while 1:
            num = tmp_nums[i]
            if num > half_target:
                return []
            else:
                if num * 2 == target:
                    tmp_nums[i] = -1
                    if num in tmp_nums:
                        first = nums.index(num)
                        nums[first] = -1
                        second = nums.index(num)
                        return [first, second]
                elif (target - num) in nums:
                    return [nums.index(num), nums.index(target-num)]
                else:
                    i += 1


s = Solution()
print s.twoSum([3, 3], 6)
