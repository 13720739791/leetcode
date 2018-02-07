# -*- coding:utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        max_str = ''
        if not s or length == 1:
            return s
        for i in range(length+1):
            for j in range(i):
                if len(s[i:j]) <= len(max_str):
                    break
                if self.is_palindrome(s[i:j]):
                    if len(s[i:j]) > len(max_str):
                        max_str = s[i:j]
        return max_str

    def is_palindrome(self, s):
        reverse_s = s[::-1]
        if reverse_s == s:
            return True
        else:
            return False

s = Solution()
print s.longestPalindrome('babadada')
