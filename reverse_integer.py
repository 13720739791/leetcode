# -*- coding:utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        result = int(str(abs(x)).rstrip("0")[::-1])
        if result > (2 ** 31):
            return 0
        else:
            if x < 0:
                return -result
            else:
                return result
