#=======================================================================
# App: PerfectCalc
# Summary: An exercise of Calc to learn Python
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

#=======================================================================
# Block for Functions
#=======================================================================
def BasicCalc():
    fNumber = -1
    while fNumber != 0:
            sMessage = "Write a value: "
            fNumber = input(sMessage)
            print(fNumber) 
            # continue...

def ScientificCalc():   
    sMessage = "Buy a Scientific Calc"
    print(sMessage) 

#=======================================================================
# Main Program
#=======================================================================
sMessage = "Wellcome to the Calc"
print(sMessage)

sType = "null"
while sType != "e":
    sType = "(B)asic Calc  OR  (S)cientific Calc  OR  (E)xit -> "
    sType = input(sType).strip().lower()
    if sType == "b":
        BasicCalc()

    if sType == "s":
        ScientificCalc()

sMessage = "Thank you for to work with Calc"
print(sMessage)  

