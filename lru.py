# -*- coding:utf-8 -*-

from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        self.map = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        value = -1
        if key in self.map:
            value = self.map.get(key)
            self.put(key, self.map.pop(key))
        return value

    def put(self, key, value):
        if key not in self.map:
            if len(self.map) == self.capacity:
                self.map.popitem(last=False)

        self.map[key] = value

obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
print obj.map
print obj.get(2)
obj.put(3, 3)
print obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)





