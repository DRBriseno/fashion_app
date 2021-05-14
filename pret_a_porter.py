from fashion import Fashion

class Pret_a_Porter(Fashion):

    def __init__(self, value, designer, collection, year, maxInventory, demand, handBeaded):
        super().__init__(value, designer, collection, year, maxInventory, demand)
        self.__handBeaded = handBeaded #private / only used in this class
    

    def handBeaded(self):
        if self.__handBeaded == True:
            my_str = "This piece is hand beaded."
            print(my_str.ljust(45) + "|")

        else:
            my_str = "This piece is not hand beaded."
            print(my_str.ljust(45) + "|")