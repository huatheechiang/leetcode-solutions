import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.buff = {}

    def insert(self, val: int) -> bool:
        if val not in self.buff: 
            self.buff[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.buff:
            idx_to_remove = self.buff[val]
            self.buff[self.arr[-1]] = idx_to_remove
            self.arr[idx_to_remove] = self.arr[-1]

            self.arr[-1] = val
            self.arr.pop()
            self.buff.pop(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.arr)




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()