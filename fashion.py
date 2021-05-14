class Fashion():
    def __init__(self, value, designer, collection, year, maxInventory, demand):
        self.__value = value #private / used only in the class, not in subclass
        self.__designer = designer
        self.__collection = collection
        self.__year = year
        self.__maxInventory = maxInventory
        self.__demand = demand

    def getValue(self):
        '''Returns value Prêt_à_Porter piece'''
        return self.__value

    def getInfo(self):
        '''Returns Fashion information'''
        print(f"{self.__designer} {self.__collection} {self.__year} is valued at ${self.__value}")
        return

    def appreciate(self):
        '''Calculates value of Fashion at appreciated value'''
        self.__value -= int(self.__value * 1.35) 

    def getMaxInventory(self):
        '''Returns max available inventory of Haute Couture'''
        my_str = f"The maximum inventory availabe for this piece is {self.__maxInventory}"
        print(my_str.ljust(45) + "|")
    
    def getPerceivedStockValue(self):
        '''Calculates and prints the percieved stock value of a fashion piece.'''
        perceivedStockValue = int(self.__maxInventory / self.__demand)
        my_str = f"This piece has {perceivedStockValue} percieved stock value"
        print(my_str.ljust(45) + "|")

    def __str__ (self):
        my_str = f"{self.__designer} {self.__collection} {self.__year} is valued at ${self.__value}"
        return my_str.ljust(45) + "|"