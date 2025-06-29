#=======================================================================
# App: Cards for PETS   (v1)
# Summary: Program for Card for PETS
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

import random

#=======================================================================
# Block for Class
#=======================================================================

class PETCard:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.age = 0

    # Add Card ======================================================
    def addCard(self, name, species, age):
        self.name = name
        self.species = species      
        self.age = age
        return True
    
    # Ramdom Number =================================================
    def RamdomCard(self):
        iRamdom = random.randint(1,7)
        return iRamdom

    # List Cards ======================================================
    def listCard(self):
        print(f"Card added: {self.name}, {self.species}, {self.age}")
        return True
       
#=======================================================================
# Main Program
#=======================================================================

PETCard01 = PETCard()
PETCard02 = PETCard()

lReturn = PETCard01.addCard("Keko", "Cat", 15)
lReturn = PETCard02.addCard("Tobi", "Bot", 1)

iPetCard1 = PETCard01.RamdomCard()
iPetCard2 = PETCard02.RamdomCard()

if iPetCard1>iPetCard2:
    print(f" {PETCard01.name} Wins")
else:
    if iPetCard2>iPetCard1:
        print(f" {PETCard02.name} Wins")
    else:
        print(f" {PETCard01.name} and {PETCard02.name} are equal")

# End Program               