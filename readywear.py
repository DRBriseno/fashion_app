from fashion import Fashion

class Ready_Wear(Fashion):

    def __init__(self, value, designer, collection, year, maxInventory, demand, thisSeason):
        super().__init__(value, designer, collection, year, maxInventory, demand)
        self.__thisSeason = thisSeason #private / only used in this class
    

    def thisSeason(self):
        if self.__thisSeason == True:
            my_str = "This piece is from a collection in this season."
            print(my_str.ljust(45) + "|")

        else:
            my_str = "This piece is from a collection from a previous season."
            print(my_str.ljust(45) + "|")