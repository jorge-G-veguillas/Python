#=======================================================================
# App: Tajamar Aulas      (v1)
# Summary: Manage Rooms of Tajamar College
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

import dataclasses

#=======================================================================
# Block for Class
#=======================================================================

@dataclasses.dataclass
class People:
    sName: str  # Name of the Student       
    iAge: int  # Age of the Student, default is 0   

class Students(People):
    sLevel: str  # Level of the Student (e.g., "Beginner", "Intermediate", "Advanced")

class Teacher(People):
    sSignature: str # Signature of the Teacher (e.g., "Math", "Science") 
      

class Room:
    def __init__(self, lLightTurnOn: bool = False, lComputersOn: bool = False):
        self.lLightTurnOn = lLightTurnOn

    def PeopleRoom(self, oTeacher: Teacher, lStudents: list[Students]): 
        self.oTeacher = oTeacher         
        self.lStudents = lStudents

    def PrintRoom(self):
        print("Teacher and Students in the Room:")
        print(f"Teacher: {self.oTeacher.sName}, Age: {self.oTeacher.iAge}, Signature: {self.oTeacher.sSignature}")
        for oPeople in self.lStudents:
            print("Student Name:", oPeople.sName, "Age:", oPeople.iAge, "Level:", oPeople.sLevel)
 
    
#=======================================================================
# Main Program
#=======================================================================

oTeacher01 = Teacher("Jorge", 40)  
oTeacher01.sSignature = "Math"

oStudent01 = Students("Pedro", 20)
oStudent01.sLevel = "Intermediate"
oStudent02 = Students("Ana", 22)
oStudent02.sLevel = "Intermediate"
oStudent03 = Students("Juan", 24)
oStudent03.sLevel = "Intermediate"

lStudents = [oStudent01, oStudent02, oStudent03]

oRoom01 = Room(True, True)

oRoom01.PeopleRoom(oTeacher01, lStudents)
oRoom01.PrintRoom()

# End Program        
