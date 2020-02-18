class MyHashMap:

    def __init__(self):
        self.MyHashMap = {}
        """
        Initialize your data structure here.
        """
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key] = value
        
        """
        value will always be non-negative.
        """
        
        
    def get(self, key: int) -> int:
        if key in self.MyHashMap.keys():
            return self.MyHashMap[key]
        else:
            return -1
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        

    def remove(self, key: int) -> None:
        if key in self.MyHashMap.keys():
            del self.MyHashMap[key]
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """