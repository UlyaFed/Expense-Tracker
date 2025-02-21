"""
This project would be designed to help users track their Amazon expenses. It would allow users to enter the details of each purchase they make, such as the date, item, cost, quantity and any other pertinent information. The project would then use this data to generate reports that show the user’s total spending on Amazon, as well as the average cost.

"""
# Registration (accepting user name and valid password from the terminal)
import re 

def validate_password():
    pattern = "^(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*-]).{6,20}$"
    
    while True:
        
        if re.match(pattern, password):
            print("Password successfully created!")
            break
        else:
            print(input("Invalid password. Try again with a valid password: "))
    

user_name = input("Create a name: ")
password = input("Create a safe password: ")
validate_password()

# Ask the user to iput his valid german mobile number.
def phone_number():
    pattern = "^(?:\+49[\s-]?|0049[\s-]?|0[\s-]?)[1-9]\d{1,4}(?:[\s-]?\d{2,10})+$"

    
    while True:
        phone_number = input("Enter your German phone number: ").strip()
        
        if re.match(pattern,phone_number):
            print("Thank you! Phone number is saved.")
            break
        else:
            print("Invalid phone number. Try again (e.g., +4917612345678 or 017612345678): ")
            
phone_number()

# Ask the user to login
def login():
    attempts = 3
    
    for attempt in range(attempts):
        log = input("Enter your username: ")
        pass_word = input("Enter your password: ")

        if (log == user_name and pass_word == password):
            print("Login successful!")
            return
        else:
            print("Invalid Username or password. Try again: ")
    print("You've used all the attempts. Try again after 5 seconds...")
     
login()