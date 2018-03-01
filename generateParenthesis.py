# -*- coding:utf-8 -*-
# @Time   : 3/1/18 3:21 PM
# @Author : dengwenyue


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def generate(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                generate(s+"(", left+1, right)
            if right < left:
                generate(s+")", left, right+1)
        generate()
        return result
