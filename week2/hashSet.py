class MyHashSet:

    def __init__(self):
        self.hashSet = {}
        """
        Initialize your data structure here.
        """
        

    def add(self, key: int) -> None:
        self.hashSet[key] = key

    def remove(self, key: int) -> None:
        if key in self.hashSet.keys():
            del self.hashSet[key]

    def contains(self, key: int) -> bool:
        if key in self.hashSet.keys():
            return True
        else:
            return False
        """
        Returns true if this set contains the specified element
        """