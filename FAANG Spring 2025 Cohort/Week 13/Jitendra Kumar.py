#Design Parking System : https://leetcode.com/problems/design-parking-system/description/
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:
        if self.spots[carType - 1] > 0:
            self.spots[carType - 1] -= 1
            return True
        return False

# Time Complexity : O(1) Need to iterate in loop over all elements.
# Space Complexity : O(1) : Need to allocate space for all the n elements


#LRU Cache : https://leetcode.com/problems/lru-cache/description
class DLinkedNode:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cache = dict()
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head      

    def _add_node(self, node : DLinkedNode) -> None:
        node.next =  self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next  = node

    def _remove_node(self, node : DLinkedNode) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def _move_to_head(self, node : DLinkedNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)

# Time Complexity : O(1)
# Space Complexity: O(Capacity of the cache)
