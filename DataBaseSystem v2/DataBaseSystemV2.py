#=======================================================================
# App: DataBaseSystem for Training Center   (v2)
# Summary: Service in Python for check Trips Elevators
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

#=======================================================================
# Block for Class
#=======================================================================

class DataBaseSystemTrainingCenter:
    def __init__(self):
        self.DataBaseTraing = []

    # Add Card ========================================================= 
    def addCard(self):
        sMessage = "Input the data for the new card (ID, NAME, AGE, COURSE): "
        print(sMessage) 
        iID = input("ID: ")
        sName = input("Name: ")
        iAge = input("Age: ")
        # Course Selection
        lCourse = []
        sMessage = "Select Course for Student :  (P)ython, (J)ava, (C)Sharp (L)ist (E)xit : "
        sCourse = input(sMessage).lower()
        while sCourse != "e":
            if sCourse == "p":
                lCourse.append("Python")
            if sCourse == "j":
                lCourse.append("Java")
            if sCourse == "c":
                lCourse.append("CSharp")
            if sCourse == "l":
                print(f"List of Courses: {lCourse}")
            sMessage = "Select Course for Student :  (P)ython, (J)ava, (C)Sharp (L)ist (E)xit : "
            sCourse = input(sMessage).lower()

        self.DataBaseTraing.append([iID, sName, iAge, lCourse])

        print(self.DataBaseTraing)

    # Update Card ======================================================
    def updateCard(self):
        lFlagUpdate = False
        iRowCurrent = -1
        sMessage = "Input the ID for update card: "
        print(sMessage) 
        iID = input("ID: ")
        for i in range(len(self.DataBaseTraing)):
            if self.DataBaseTraing[i][0] == iID:
                lFlagUpdate = True
                iRowCurrent = i
                print(f"Card with ID {iID} founded.")
                
        if not lFlagUpdate:
               print(f"Card with ID {iID} not found.")
               return
        
        sMessage = "Input the data for the new card (ID, NAME, AGE, COURSE): "
        print(sMessage) 

        sName = input(f"Name {self.DataBaseTraing[iRowCurrent][1]} New Value: ")
        iAge = input(f"Age {self.DataBaseTraing[iRowCurrent][2]} New Value: ")
        #sCourse = input(f"Course {self.DataBaseTraing[iRowCurrent][3]} New Value: ")

        # Course Selection
        lCourse = []
        sMessage = "Select Course for Student :  (P)ython, (J)ava, (C)Sharp (L)ist (E)xit : "
        sCourse = input(sMessage).lower()
        while sCourse != "e":
            if sCourse == "p":
                lCourse.append("Python")
            if sCourse == "j":
                lCourse.append("Java")
            if sCourse == "c":
                lCourse.append("CSharp")
            if sCourse == "l":
                print(f"List of Courses: {lCourse}")
            sMessage = "Select Course for Student :  (P)ython, (J)ava, (C)Sharp (L)ist (E)xit : "
            sCourse = input(sMessage).lower()
    
        self.DataBaseTraing[iRowCurrent][1] = sName
        self.DataBaseTraing[iRowCurrent][2] = iAge
        self.DataBaseTraing[iRowCurrent][3] = lCourse
        print(f"Card with ID {iID} updated.")
        print(self.DataBaseTraing)

        return
    
    # Delete Card ======================================================
    def deleteCard(self):
        lFlagDelete = False

        sMessage = "Input the ID for delete card: "
        print(sMessage) 
        iID = input("ID: ")
        for i in range(len(self.DataBaseTraing)):
            if self.DataBaseTraing[i][0] == iID:
                lFlagDelete = True
                del self.DataBaseTraing[i]
                print(f"Card with ID {iID} deleted.")
                print(self.DataBaseTraing)

        if not lFlagDelete:
               print(f"Card with ID {iID} not found.")

        return        
        
    # List Cards ======================================================
    def listCard(self):
        print("List of Cards in the Database: ")
        print(self.DataBaseTraing)
        return     
       
#=======================================================================
# Main Program
#=======================================================================

DataBaseSystemTrainingCenter01 = DataBaseSystemTrainingCenter()

sMessage = "Select Action for a Card:  (A)dd, (U)pdate, (D)elete (L)ist (E)xit : "
sAction = input(sMessage).lower()

while sAction != "e":
    if sAction == "a": 
        DataBaseSystemTrainingCenter01.addCard()
    if sAction == "u":
        DataBaseSystemTrainingCenter01.updateCard()
    if sAction == "d":
        DataBaseSystemTrainingCenter01.deleteCard()
    if sAction == "l":
        DataBaseSystemTrainingCenter01.listCard()

    sMessage = "Select Action for a Card:  (A)dd, (U)pdate, (D)elete (L)ist (E)xit : "
    sAction = input(sMessage).lower()

print ("\n<<<< The Database is closed >>>>\n")

# End Program               