#Design HashMap : https://leetcode.com/problems/design-hashmap
class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.map = [[] for _ in range(self.size)]
    
    def hash(self, key : int) -> int:
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        for i, (k,v) in enumerate(self.map[h]):
            if k == key:
                self.map[h][i] = (key, value)
                return
        self.map[h].append((key,value))      
        
    def get(self, key: int) -> int:
        h = self.hash(key)
        for k, v in self.map[h]:
            if k == key:
                return v
        return -1        

    def remove(self, key: int) -> None:
        h = self.hash(key)
        self.map[h] = [(k, v) for k, v in self.map[h] if k != key]

# Time Complexity : O(1) average; worst case O(n) if all the key falls into the same bucket
# Space Complexity : O(n) : Need to allocate space only for all the key, value pairs


#Design Hit Counter : https://leetcode.com/problems/design-hit-counter
class HitCounter:

    def __init__(self):
        self.size = 300
        self.time = [0] * self.size
        self.hits = [0] * self.size
        
    def hit(self, timestamp: int) -> None:
        index = timestamp % self.size
        if self.time[index] == timestamp:
            self.hits[index] += 1
        else:
            self.time[index] = timestamp
            self.hits[index] = 1
        
    def getHits(self, timestamp: int) -> int:
        totalHits = 0
        for i in range(self.size):
            if self.time[i] > (timestamp - self.size):
                totalHits += self.hits[i]
        return totalHits

# Time Complexity : O(1) worst case max 300 iterations O(300)
# Space Complexity: O(1) max 300 space required for storage
