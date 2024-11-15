class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Add Two Numbers https://leetcode.com/problems/add-two-numbers/description/
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummyHead = ListNode()
    tail = dummyHead

    while l1 or l2 or carry:
        total = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
        digit = total % 10
        carry = total // 10
        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = dummyHead.next
    dummyHead.next = None
    return result

# LRU Cache https://leetcode.com/problems/lru-cache/description/
class LRUCache:
    # Least recently used caching refers to a particular caching algorithm
    # designed to keep the most recent accessed data ranked by time
    # the time is often represented by an "age bit" from lowest being the
    # least recently used and highest being the most recently used item.

    def __init__(self, capacity: int):
        # use a map to represent a ranked list
        self.capacity = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.map[key] = self.map.pop(key)
        return self.map.get(key) if key in self.map else -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        if len(self.map) == self.capacity:
            self.map.pop(next(iter(self.map)))
        self.map[key] = value

def __main__():
    # Q1 test cases
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    result = addTwoNumbers(l1, l2)
    while(result):
        print(result.val)
        result = result.next if result.next is not None else None

if __name__ == "__main__":
    __main__()