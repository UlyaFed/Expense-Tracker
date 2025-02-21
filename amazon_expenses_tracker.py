"""
This project would be designed to help users track their Amazon expenses. It would allow users to enter the details of each purchase they make, such as the date, item, cost, quantity and any other pertinent information. The project would then use this data to generate reports that show the user’s total spending on Amazon, as well as the average cost.

"""
# Registration (accepting user name and valid password from the terminal)

import re 

def validate_password():
    pattern = "^(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*-]).{6,20}$"
    
    while True:
        password = input("Create a safe password: ")
        
        if re.match(pattern, password):
            print("Password successfully created!")
            break
        else:
            print(input("Invalid password. Try again with a valid password: "))
    

user_name = input("Create a name: ")
validate_password()
