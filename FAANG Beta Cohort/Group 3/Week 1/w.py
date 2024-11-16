# 1. Add Two Numbers https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add result.next as the node before the first digit / beginning of the node list, no need to trace back after forming list
        result = ListNode()
        nextNode = ListNode()
        result.next = nextNode

        # pointers for looping through l1 and l2
        l1Pointer = l1
        l2Pointer = l2

        # use this to store of need move up 10 to next digit
        addup = 0

        # set flag to determin if move to next digit
        ifMove = True
        
        # loop through l1 and l2
        while(ifMove):      
            # this means the end of both l1 and l2
            if(l1Pointer == None and l2Pointer == None):
                # only need to check if there is 1o moved up from last digit
                # if so, add a new node, and store the moved up 10
                if addup > 0:
                    nextNode.next = ListNode()
                    nextNode.next.val = addup
                ifMove = False

            # if l1 and l2 both has next node
            elif(l1Pointer != None and l2Pointer != None):
                # calculate the digit with the current digit in l1 and l2, and the moved up 10
                tmp = l1Pointer.val + l2Pointer.val + addup
                # store if there is a moved up 10
                addup = tmp//10
                # create a new node for the current digit calculation results
                nextNode.next = ListNode()
                # move to the new node as current node
                nextNode = nextNode.next
                # set digit value
                nextNode.val = tmp%10
                # move to next digit in l1 and l2
                l1Pointer = l1Pointer.next
                l2Pointer = l2Pointer.next

            # if only l1 has next node
            elif(l1Pointer != None and l2Pointer == None):
                tmp = l1Pointer.val + addup
                addup = tmp//10
                nextNode.next = ListNode()
                nextNode = nextNode.next
                nextNode.val = tmp%10
                l1Pointer = l1Pointer.next

            # if only l2 has next node
            elif(l1Pointer == None and l2Pointer != None):
                tmp = l2Pointer.val + addup
                addup = tmp//10
                nextNode.next = ListNode()
                nextNode = nextNode.next
                nextNode.val = tmp%10
                l2Pointer = l2Pointer.next

            else:
                print('error!')
    
        return result.next.next

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 2. LRU Cache https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    # this solution is based on python 3.7+
    # the dict is order by the sequence key-value pairs are added, 
    # which resloved the need for double linked list for storing order
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}

    def get(self, key: int) -> int:
        # if the key is in map
        if(key in self.cacheMap):
            # pop will return the value
            # delete the key value pair then add back
            # this will refresh the order of the map
            # make the key value pair the most recently used/ newly added
            resultValue = self.cacheMap.pop(key)
            self.cacheMap[key] = resultValue
            return resultValue
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # since update the value for an exising key will not update the order
        # so need to check if the key is in map
        # if so, delete the key value pair using pop first
        if key in self.cacheMap:
            self.cacheMap.pop(key)

        # then add the value
        self.cacheMap[key] = value

        # now check the size of the map
        # if it is over capacity, delete the 
        if(len(self.cacheMap) > self.capacity):
            self.cacheMap.pop(next(iter(self.cacheMap)))

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
