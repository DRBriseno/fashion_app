from fastfashion import Fast_Fashion
from fashion import Fashion
from haute_couture import Haute_Couture
from pret_a_porter import Pret_a_Porter
from readywear import Ready_Wear
from fastfashion import Fast_Fashion
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

                elif isinstance(fashion, Fast_Fashion):
                    fashion.veryTrendy()
                    fashion.getMaxInventory()
                    fashion.getPerceivedStockValue()

                elif isinstance(fashion, Ready_Wear):
                    fashion.thisSeason()
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


        #-----------------------------------#

        #running sell fashion with (remove)

          #def sellFashion(self, Fashion):
        #'''Removes fashion out closet'''
        #Fashion.getInfo()
        #self.__money += float(Fashion.getValue())
        #self.closet.remove(Fashion)

        #returns error (working on solution)

        #Traceback (most recent call last):
  #File "person.py", line 135, in <module>
    #Sara.sellFashion(chanel_Street)
  #File "person.py", line 89, in sellFashion
    #self.closet.remove(Fashion)
#ValueError: list.remove(x): x not in list



        #running sell fashion with (pop)


    #def sellFashion(self, Fashion):
        #'''Removes fashion out closet'''
        #Fashion.getInfo()
        #self.__money += float(Fashion.getValue())
        #self.closet.pop(Fashion)

        #returns error (working on solution)

        #File "person.py", line 147, in <module>
    #Sara.sellFashion(chanel_p)
  #File "person.py", line 103, in sellFashion
    #self.closet.pop(Fashion)
#TypeError: 'Pret_a_Porter' object cannot be interpreted as an integer




    def sellFashion(self, Fashion):
        """Removes fashion out of closet"""
        Fashion.getInfo()
        self.__money +=(Fashion.getValue())
        self.closet.append(Fashion)


if __name__ == "__main__":
    os.system("clear")


    chanel = Haute_Couture(79834, "Chanel", "Haute Couture", "2021", 427, 20000, False, True)
    dior = Haute_Couture(68970, "Dior", "Haute Couture", "1987", 43, 12000, True, False)
    chanel_p = Pret_a_Porter(7998, "Chanel", "Prêt-à-Porter", "2019", 20000, 300000, True)
    dior_p = Pret_a_Porter(11499, "Dior", "Prêt-à-Porter", "2020", 12000, 225000, False)
    chanel_Street = Ready_Wear(400, "Chanel", "fall", 2021, 300000, 550000, True)
    dior_Fast = Fast_Fashion( 75, "Dior", "Spring", "2018", 10000000, 7500000, False)


    Sara = Person("Sara", 3900000)


    chanel.getInfo()
    dior.getInfo()
    chanel_p.getInfo()
    dior_p.getInfo()
    chanel_Street.getInfo()
    dior_Fast.getInfo()


    print("\nCurrent balance: " + Sara.getBalance())


    print("\nSara buys all the haute couture.\n")
    Sara.buyFashion(chanel)
    Sara.buyFashion(dior)
    Sara.buyFashion(chanel_p)
    Sara.buyFashion(dior_p)
    Sara.buyFashion(dior_Fast)
    print("Current balance " + Sara.getBalance() + "\n")
    Sara.getFashions()


    print("\n\nSold some haute couture.\n\n")
    chanel.appreciate()
    dior.appreciate()


    Sara.sellFashion(chanel_p)
    Sara.sellFashion(dior)
    Sara.sellFashion(chanel_Street)
    print("\n")

    
    Sara.getFashions()


    print("\nEnding balance " + Sara.getBalance())
    print("Assets " + Sara.getAssets())