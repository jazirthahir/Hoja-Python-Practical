class Animal:
    def __init__(self):
        self.name = " I am spider"
        self._Speed = 50
        self.__weight = 45
        
    def details(self):
        print("name :", self.name)
        print("height :", self._Speed)
        
    def get_weight(self):
        return self.__weight

spider = Animal()
cat = Animal()

print(self.name)
print(self._speed)
print(self.get_weight)