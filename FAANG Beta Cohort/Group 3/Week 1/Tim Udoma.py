# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  Trav. Mult, num1, num2. Add, res. list(res). reverse. LL

        num1 = num2 = res = 0

        def trav(node):
            val = 0
            mult = 1

            while node:
                val += (node.val * mult)
                mult *= 10
                node = node.next 
            return val
        num1 = trav(l1)
        num2 = trav(l2)

        res = list(str(num1 + num2))
        res.reverse()

        dummy = ListNode()
        curr = dummy
        for digit in res:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next



# LRU CACHE
import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)