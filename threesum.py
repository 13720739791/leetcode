# -*- coding:utf-8 -*-
# @Time   : 2/22/18 4:00 PM
# @Author : dengwenyue


class Solution(object):

    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            hashmap = {}
            for j in range(i+1, len(nums)):
                item_j = nums[j]
                if (target - item_j) in hashmap:
                    res = [nums[i], target-item_j, item_j]
                    if res not in result:
                        result.append(res)
                else:
                    hashmap[item_j] = j
        return result

    def threeSum1(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            head = i+1
            tail = len(nums) - 1
            while head < tail:
                if nums[head] + nums[tail] == target:
                    res = [nums[i], nums[head], nums[tail]]
                    if res not in result:
                        result.append(res)
                    head += 1
                    tail -= 1
                elif nums[head] + nums[tail] > target:
                    tail -= 1
                else:
                    head += 1

        return result

s = Solution()
print s.threeSum1(nums=[-1,0,1,2,-1,-4])