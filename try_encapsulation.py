class animal:
    def __init__(self):
        self.name = " I am spider"
        self._Speed = 50
        self.__weight = 45
        
    def details(self):
        print("name :",self.name)
        print("height :",self._Speed)
        print("weight :",self.__weight)

spider = animal()
cat = animal()

print(self.name)
print(self._speed)
print(self.__speed)