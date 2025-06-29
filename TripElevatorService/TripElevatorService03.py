#=======================================================================
# App: TripElevatorService with Class
# Summary: Service in Python for check Trips Elevators
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

import random

#=======================================================================
# Block for Class
#=======================================================================

class TrypElevatorService:
    def __init__(self, iFloorCurrent, bTripException):
        self.iFloorCurrent = iFloorCurrent
        self.bTripException = False

    def TrypElevatorInputFloor(self, iFloorCurrent):
        iFloorNext = -1

        sMessage = "You are in: {iFloorCurrent} What floor do you want to go? (0-80): "
        iFloorNext = int(input(sMessage))
        if iFloorCurrent == iFloorNext:
            print("Piii	♫ ♫  You are already on {iFloorCurrent} floor. Please choose a different floor.")
            return self.TrypElevatorInputFloor(iFloorCurrent)
        
        if iFloorNext < 0 or iFloorNext > 80:
            print("The floor is out of range. Please enter a valid floor (0-80).")
            return self.TrypElevatorInputFloor(iFloorCurrent)  

        for iFloorCurrent in range(iFloorCurrent, iFloorNext+1):
            print(f"The Elevator is moving from floor {iFloorCurrent} to floor {iFloorCurrent}.")
            self.iFloorCurrent = iFloorNext+1
        print(f"The Elevator has arrived at floor {iFloorCurrent}.")
        return iFloorCurrent

    def TrypElevator(floor):
        print(f"Trace: The Elevator is on floor {floor}.")

        bSmoking = random.choice([True, False]) 
        print("Trace: Smoking:", bSmoking)

        iWeight = random.randint(70,800)
        print("Trace: Weight:", iWeight)

        iVelocity = random.randint(0,10)
        print("Trace: Velocity:", iVelocity)

        iTemperature = random.randint(-5,40)
        print("Trace: Temperature:", iTemperature)

        bTripException = ElevatorChecking(bSmoking, iWeight, iVelocity, iTemperature) 

    def ElevatorChecking(bSmoking, iWeight, iVelocity, iTemperature):
        if bSmoking:
            print("Trace: One Person is smoking. Elevator cannot operate. Smoking:", bSmoking)
            return True # The IoT did not repair the situation. True = There is Exception

        if iWeight > 750:
            print("Trace: Weight limit exceeded. Elevator cannot operate. Weight:", iWeight)
            print("Trace: Warning please use the stairs until the Weight is below 750 kg.")
            return False # The IoT repaired the situation. False = Not Exception

        if iVelocity > 8:
            print("Trace: Velocity out of range. Elevator cannot operate. Velocity:", iVelocity)
            print("Trace: Warning, The Elevator is moving more slowly")
            return False # The IoT repared the situation. False = Not Exception

        if iTemperature > 35:
            print("Trace: Temperature out of range. Elevator cannot operate. Temperature:", iTemperature)
            return True # The IoT did not repair the situation. True = There is Exception

#=======================================================================
# Main Program
#=======================================================================

iFloorCurrent = 0
bTripException = False
Elevator01 = TrypElevatorService(iFloorCurrent,bTripException)

iFloorCurrent = Elevator01.TrypElevatorInputFloor(iFloorCurrent)

print(f"The Elevator has arrived at floor {iFloorCurrent}.")

sMessage = "Trace: The Elevator goes to the zero floor."
print(sMessage)  

sMessage = "Trace: The Elevator has the gate open and it is stopped."
print(sMessage)

# End Program        
