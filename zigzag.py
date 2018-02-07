# -*- coding:utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        news = ''
        interval = numRows * 2 - 2
        if numRows == 1:
            return s
        for i in range(numRows):
            print news
            if i == 0 or i == (numRows -1):
                index = i
                while True:
                    if index > len(s)-1:
                        break
                    news += s[index]
                    index += interval

            else:
                index = i
                if index > len(s) - 1:
                    return news
                news += s[index]
                while True:

                    if (index + interval - 2 * i) > len(s) - 1:
                        break
                    index += interval - 2 * i
                    news += s[index]
                    if (index + 2 * i) > len(s) -1:
                        break
                    index += 2 * i
                    news += s[index]

        return news

s = Solution()
news = s.convert("P", 3)
print news




