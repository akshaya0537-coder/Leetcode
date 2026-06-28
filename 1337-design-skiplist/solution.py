class Skiplist:
    def __init__(self):
        self.l=[]
    def search(self, target: int) -> bool:
        return target in self.l
    def add(self, num: int) -> None:
        self.l.append(num)
    def erase(self, num: int) -> bool:
        if num in self.l:
            self.l.remove(num)
            return True
        else:
            return False


        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
