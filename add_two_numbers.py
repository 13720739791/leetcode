# -*- coding:utf-8 -*-


class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        l3 = None
        current_node = None
        carry_bit = 0

        while l1 and l2:
            value = l1.value + l2.value + carry_bit
            if value >= 10:
                carry_bit = 1
                value -= 10
            else:
                carry_bit = 0

            next_node = ListNode(value=value)
            if not l3:
                l3 = next_node
                current_node = l3
            else:
                current_node.next = next_node
            current_node = next_node
            l1 = l1.next
            l2 = l2.next

        while l1.next:
            value = l1.value + carry_bit
            if value >= 10:
                carry_bit = 1
                value -= 10
            else:
                carry_bit = 0
            next_node = ListNode(value=value)
            if not l3:
                l3 = next_node
                current_node = l3
            else:
                current_node.next = next_node
            current_node = next_node
            l1 = l1.next

        while l2.next:
            value = l2.value + carry_bit
            if value >= 10:
                carry_bit = 1
                value -= 10
            else:
                carry_bit = 0
            next_node = ListNode(value=value)
            if not l3:
                l3 = next_node
                current_node = l3
            else:
                current_node.next = next_node
            current_node = next_node
            l2 = l2.next

        return l3











