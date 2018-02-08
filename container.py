# -*- coding:utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        max_area = 0

        while 0 <= head < tail <= (len(height)-1):
            max_area = max(max_area, min(height[head], height[tail])*(tail-head))

            if height[head] < height[tail]:
                head += 1

            else:
                tail -= 1

        return max_area
