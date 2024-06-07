class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for i in self.map:
            if key == i[0]:
                i[1] = value
                return None
            
        self.map.append([key, value])
        return None
                
        

    def get(self, key: int) -> int:
        for i in self.map:
            if key == i[0]:
                return i[1] 
        
        return -1
        

    def remove(self, key: int) -> None:
        for i in self.map:
            if i[0] == key:
                self.map.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
