#=======================================================================
# App: Car and People      (v1)
# Summary: Car and People simulation
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

#=======================================================================
# Block for Class
#=======================================================================
class People:
    def __init__(self, sName):
        self.sName = sName

class Coche:
    def __init__(self, lTurnOn):
        self.lTurnOn = lTurnOn
        print("Coche is TurnOn: ", lTurnOn)

    def Velocity(self, iVelocity: int):          
        self.iVelocity = iVelocity
        print("Coche goes to Velocity: ", iVelocity)

    def Passengers(self, lPeople: list[People]):          
        self.lPeople = lPeople
        print("Coche has the following passengers: ")   

        # First Print
        for oPeople in self.lPeople:
            print(oPeople.sName)

        # Second Print
        print(list(map(lambda oPeople: oPeople.sName, self.lPeople)))


    def Stop(self, lTurnOff):          
        self.lTurnOff = lTurnOff
        print("Coche is Stopped: ", lTurnOff)

#=======================================================================
# Main Program
#=======================================================================

oPeople01 = People("Jorge")
oPeople02 = People("Ana")
oPeople03 = People("Juanito")

lPeople = [oPeople01, oPeople02, oPeople03]

oCoche01 = Coche(True)

oCoche01.Passengers(lPeople)

oCoche01.Velocity(20)

oCoche01.Velocity(40)

# After 1 hour 

oCoche01.Velocity(20)

oCoche01.Velocity(0)

oCoche01.Stop(True)

# End Program        
