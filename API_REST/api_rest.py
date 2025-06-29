#=======================================================================
# App: API REST with functions   (v1)
# Summary: App for work with GET, POST, PUT, DELETE methods
# Date: June 2025
# Developer: Jorge Gallego Veguillas
#=======================================================================

# import requests

#=======================================================================
# Block for DATA
#=======================================================================

JSON_ALUMNOS = '[{"NOMBRE": "Jorge Gallego Veguillas", "EDAD": 45, "EMAIL": "JGALLEGO@MAIL.COM"}, \
                 {"NOMBRE": "Ana García Garcia", "EDAD": 33, "EMAIL": "AGARCIA@MAIL.COM"}]'

sHEAD = ""

OK =200

#=======================================================================
# Block for Functions
#=======================================================================

def GET(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        print("Response Data:", response.json())
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
       
#=======================================================================
# Main Program
#=======================================================================

sMessage = "Write the URL for GET:"
# input_url = input(sMessage)
input_url = "https://jsonplaceholder.typicode.com/todos"

GET(input_url)

# End Program               