from fashion import Fashion

class Fast_Fashion(Fashion):

    def __init__(self, value, designer, collection, year, maxInventory, demand, veryTrendy):
        super().__init__(value, designer, collection, year, maxInventory, demand)
        self.__veryTrendy = veryTrendy #private / only used in this class
    

    def veryTrendy(self):
        if self.__veryTrendy == True:
            my_str = "This piece is currently a very trendy item."
            print(my_str.ljust(45) + "|")

        else:
            my_str = "This piece is not a very trendy item."
            print(my_str.ljust(45) + "|")