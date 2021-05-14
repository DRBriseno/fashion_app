from fashion import Fashion

class Haute_Couture(Fashion):
    def __init__(self, value, designer, collection, year, maxInventory, demand, isVintage, celebrityOwned):
        super().__init__(value, designer, collection, year, maxInventory, demand)
        self.__vintage = isVintage   #private / only used in this class
        self.__celebrityOwned = celebrityOwned


    def isVintage(self):
        if self.__vintage == True:
            my_str = "This piece is vintage."
            print(my_str.ljust(45) + "|")


    def wasCelebrityOwned(self):
        if self.__celebrityOwned == True:
            my_str = "This piece was owned by a celebrity."
            print(my_str.ljust(45) + "|")
        

