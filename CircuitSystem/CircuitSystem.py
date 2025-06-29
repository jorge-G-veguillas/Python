#=======================================================================
# App: Circuit System   (v1)
# Summary: System to Control a Circuit System
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

import random

iCircuitCount = -1

#=======================================================================
# Block for Class
#=======================================================================

class Circuit:
    def __init__(self, sName, bBattery, bInterruptor, bLight, oPreviousCircuit=None):
        self.sName = sName
        self.bBattery = bBattery
        self.bLight = bLight
        self.bInterruptor = bInterruptor
        self.oPreviousCircuit = oPreviousCircuit

class MotherBoard:
    def __init__(self, bBattery, bInterruptor):
        self.bBattery = bBattery
        self.bInterruptor = bInterruptor  
        self.lListCircuits = []       


    def FillCircuits(self, iPosition: int, bInterruptor: bool, bLight:bool):
        print(iPosition)
        print(bInterruptor)
        print(bLight)
        print(iCircuitCount)
        #for oCircuit in self.lListCircuits[iPosition:iCircuitCount]:  <--- Me da error
        for oCircuit in self.lListCircuits[0:1000]:
            #print("Circuit Name:", oCircuit.sName, "Battery:", oCircuit.bBattery, "Interruptor:", oCircuit.bInterruptor, "Light:", oCircuit.bLight)
            #print(oCircuit.sName, "\t\t\t", oCircuit.bBattery, "\t\t", oCircuit.bInterruptor, "\t\t\t", oCircuit.bLight) 
            if oCircuit.sName >= iPosition:
                if oCircuit.bInterruptor:
                    oCircuit.bLight = bInterruptor

    def PrintCircuits(self):
        print("Circuit Name\t\tBattery\t\tInterruptor\t\tLight")
        print("============\t\t========\t===========\t\t=====")
        for oCircuit in self.lListCircuits:
            #print("Circuit Name:", oCircuit.sName, "Battery:", oCircuit.bBattery, "Interruptor:", oCircuit.bInterruptor, "Light:", oCircuit.bLight)
            print(oCircuit.sName, "\t\t\t", oCircuit.bBattery, "\t\t", oCircuit.bInterruptor, "\t\t\t", oCircuit.bLight) 

#=======================================================================
# Main Program
#=======================================================================


sType = input("Select the type of MotherBoard (M)anual or (A)utomatic: ").strip().lower()

if sType == "m":
# Manual Mode for the MotherBoard
    oMotherBoard01 = MotherBoard(True, True)
    print("The MotherBoard is powered on.")

    while oMotherBoard01.bBattery and oMotherBoard01.bInterruptor:

        sAnswer = input("Do you want to add a new circuit? (y/n): ").strip().lower()
        if sAnswer == "y":
            #oCircuit01 = Circuit("Light01",(oMotherBoard01.bBattery and oMotherBoard01.bInterruptor), False, False, None)
            iCircuitCount += 1
            #lBateryInterruptor = (oMotherBoard01.bBattery and oMotherBoard01.bInterruptor)
            oMotherBoard01.lListCircuits.append(Circuit(str(iCircuitCount),(oMotherBoard01.bBattery and oMotherBoard01.bInterruptor), False, False, None))
            
            oMotherBoard01.PrintCircuits()

        iAnswer = input(f"Write the number of the Light (from 0 until {iCircuitCount}) to do click on Interruptor: ").strip().lower()
        oMotherBoard01.lListCircuits[int(iAnswer)].bInterruptor = not oMotherBoard01.lListCircuits[int(iAnswer)].bInterruptor
        oMotherBoard01.lListCircuits[int(iAnswer)].bLight = not oMotherBoard01.lListCircuits[int(iAnswer)].bLight

        oMotherBoard01.FillCircuits(iAnswer, oMotherBoard01.lListCircuits[int(iAnswer)].bInterruptor, oMotherBoard01.lListCircuits[int(iAnswer)].bLight)
        oMotherBoard01.PrintCircuits()

        sAnswer = input("Do you want to Turn OFF the MotherBoard? (y/n): ").strip().lower()
        if sAnswer == "y":
            oMotherBoard01.bInterruptor = False


# Automatic Mode for the MotherBoard
""" if sType == "a":
    oMotherBoard01 = MotherBoard(True, True)
    print("The MotherBoard is powered on.")

    oCircuit01 = Circuit("Light01",(oMotherBoard01.bBattery and oMotherBoard01.bInterruptor), False, False, None)
    print(f"The Circuit {oCircuit01.sName} is Added.")

    oMotherBoard01.lListCircuits.append(oCircuit01)

    oMotherBoard01.PrintCircuits()

    while oMotherBoard01.bBattery and oMotherBoard01.bInterruptor:
        oMotherBoard01.bInterruptor = False """

print("\n<<<< The MotherBoard is powered off. >>>>\n")
