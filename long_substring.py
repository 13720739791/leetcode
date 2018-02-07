# -*- coding: utf-8 -*-
from collections import deque


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        max_length = 0
        substring = deque()

        for c in s:
            if c not in substring:
                substring.append(c)
            else:
                length = len(substring)
                if length > max_length:
                    max_length = length
                while True:
                    tmp_c = substring.popleft()
                    if tmp_c == c:
                        break
                substring.append(c)

        if substring:
            print substring
            if len(substring) > max_length:
                max_length = len(substring)
        return max_length


c = Solution()
max_length = c.lengthOfLongestSubstring('c')
print max_length