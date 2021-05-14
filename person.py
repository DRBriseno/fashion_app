from fashion import Fashion
from haute_couture import Haute_Couture
from pret_a_porter import Pret_a_Porter
import os


class Person():
    def __init__(self, name, money):
        self.__name = name
        self.__money = money
    closet = list() #lists fashion pieces


    def getFashions(self):
        '''Returns all fashions in Person's closet'''
        if not self.closet: # empty list
            print("Sara's has no items in her closet.")


        else:
            print(f"{self.__name}'s Closet: \n++++++++++++++++++++++++++++++")
            for fashion in self.closet:
                print("")
                print(fashion)


                if isinstance(fashion, Haute_Couture):
                    fashion.isVintage()
                    fashion.wasCelebrityOwned()


                elif isinstance(fashion, Pret_a_Porter):
                    fashion.handBeaded()
                    fashion.getMaxInventory()
                    fashion.getPerceivedStockValue()


                print("")

            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

    def getBalance(self):
        '''Balance'''
        return f"${self.__money}"

    
    def getAssets(self):
        '''Assets'''
        assets = self.__money


        for fashion in self.closet:
            assets += fashion.getValue()


        return str(assets)


    def buyFashion(self, Fashion):
        '''Adds fashion into closet'''
        self.__money -= float(Fashion.getValue())
        self.closet.append(Fashion)


    def sellFashion(self, Fashion):
        '''Removes fashion out closet'''
        Fashion.getInfo()
        self.__money += float(Fashion.getValue())
        self.closet.remove(Fashion)


if __name__ == "__main__":
    os.system("clear")


    chanel = Haute_Couture(79834, "Chanel", "Haute Couture", "2021", 427, 20000, False, True)
    dior = Haute_Couture(68970, "Dior", "Haute Couture", "1987", 43, 12000, True, False)
    chanel_p = Pret_a_Porter(7998, "Chanel", "Prêt-à-Porter", "2019", 20000, 300000, True)
    dior_p = Pret_a_Porter(11499, "Dior", "Prêt-à-Porter", "2020", 12000, 225000, False)


    Sara = Person("Sara", 3900000)


    chanel.getInfo()
    dior.getInfo()
    chanel_p.getInfo()
    dior_p.getInfo()


    print("\nCurrent balance: " + Sara.getBalance())


    print("\nSara buys all the haute couture.\n")
    Sara.buyFashion(chanel)
    Sara.buyFashion(dior)
    Sara.buyFashion(chanel_p)
    Sara.buyFashion(dior_p)
    print("Current balance " + Sara.getBalance() + "\n")
    Sara.getFashions()


    print("\n\nSold some haute couture.\n\n")
    chanel.appreciate()
    dior.appreciate()


    Sara.sellFashion(chanel_p)
    Sara.sellFashion(dior)
    print("\n")

    
    Sara.getFashions()


    print("\nEnding balance " + Sara.getBalance())
    print("Assets " + Sara.getAssets())