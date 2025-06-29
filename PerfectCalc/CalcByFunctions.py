#=======================================================================
# App: PerfectCalc
# Summary: An exercise of Calc to learn Python
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

dictionaryCalc = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y
}

#=======================================================================
# Block for Functions
#=======================================================================
def addCalc(x, y):
    return x + y

#=======================================================================
# Main Program
#=======================================================================
sMessage = "Wellcome to the Calc"
print(sMessage)

addResult = addCalc(5, 3)
print(f"The result of adding 5 and 3 is: {addResult}")

sFunction = addCalc
addResult = sFunction(7, 8)
print(f"The result of adding 5 and 3 is: {addResult}")

sOption = input("Select Operation: Add, Subtract, Multiply, Divide, Exit:").lower().strip()

while sOption != "exit":
    dictionaryCalc.get(sOption, lambda x, y: "Invalid operation")  # Default to invalid operation if not found
    if sOption in dictionaryCalc:
        try:
            fNumber1 = float(input("Enter first number: "))
            fNumber2 = float(input("Enter second number: "))
            result = dictionaryCalc[sOption](fNumber1, fNumber2)
            print(f"The result of {sOption}ing {fNumber1} and {fNumber2} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    sOption = input("Select Operation: Add, Subtract, Multiply, Divide, Exit:").lower().strip()       

sMessage = "\n<<<< Thank you for to work with Calc >>>> \n"
print(sMessage)  

