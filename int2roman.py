# -*- coding:utf-8 -*-
# @Time   : 2/22/18 3:24 PM
# @Author : dengwenyue


class Solution(object):
    def intToRoman(self, num):
        thousand_list = ["", "M", "MM", "MMM"]
        hundred_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ten_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        unit_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        roman_str = thousand_list[num/1000] + hundred_list[(num % 1000)/100] + \
                    ten_list[(num % 100)/10] + unit_list[num % 10]
        return roman_str
