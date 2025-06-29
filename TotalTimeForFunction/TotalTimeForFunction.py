#=======================================================================
# App: Total Time For Function   (v1)
# Summary: Function for to know the total time for a function
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

import time

#=======================================================================
# Block for Functions
#=======================================================================

def FunctionToRun():
    sMessage = "Run Function Start!!"
    print(sMessage)

    fTotal = 0
    for iPos in range(0, 1000000):
        fTotal += iPos

    sMessage = "Run Function End!!"
    print(sMessage)

       
#=======================================================================
# Main Program
#=======================================================================

time.localtime()  

start_time = time.time()     
print("Start Time: ", time.localtime(start_time))

FunctionToRun()

end_time = time.time()  # End time
print("End Time: ", time.localtime(end_time))

total_time = end_time - start_time 
print("Total Time for Function: ", total_time)

# End Program               