#=======================================================================
# App: MailCheck
# Summary: Apps for check an email address
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================
 
sMail = input("Enter your email address: ").lower()

# Spaces ===========================================================
iTotalAt = sMail.count(" ")
print("Number of ' ':", iTotalAt)
if iTotalAt != 0:
        print("Error!! The Email have spaces")
        quit()

# Number Ats ===========================================================
iTotalAt = sMail.count("@")
print("Number of '@':", iTotalAt)
if iTotalAt != 1:
        print("Error!! The Email must to have one @")
        quit()

# Mail must start with a letter ========================================
if sMail[0].isdigit():
        print("Error!! Mail start with Number", sFirstPosition) 
        quit()  

# Check last 4 characters ==============================================
sLastString = sMail[-4:]
print("Last 4 characters:", sLastString)

sFirstPosition = sLastString[:1]
print("First position:", sFirstPosition)
if sFirstPosition != ".":
    print("Error!! the 4 position must to be '.'")
    quit()

# Position At ==========================================================       
iPositionAt = sMail.find("@")
print("Position of '@':", iPositionAt)

# Fix Mail =============================================================   
sPreviousAt = sMail[:iPositionAt]
sAfterAt = sMail[iPositionAt+1:]
sFirstPosition = sMail[:1]  

# Show Parts of Email ==================================================
print("Previous '@':", sPreviousAt)
print("After '@':", sAfterAt)   
print("First position:", sFirstPosition)

print("The Email is OK. Sending...", sFirstPosition)
# End Program    

