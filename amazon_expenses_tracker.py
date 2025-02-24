"""
This project would be designed to help users track their Amazon expenses. It would allow users to enter the details of each purchase they make, such as the date, item, cost, quantity and any other pertinent information. The project would then use this data to generate reports that show the user’s total spending on Amazon, as well as the average cost.

"""
# Registration (accepting user name and valid password from the terminal)
import re 
import time

def validate_password():
    pattern = "^(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*-]).{6,20}$"
    
    while True:
        password = input("Create a safe password: ")
        if re.match(pattern, password):
            print("Password successfully created!")
            return password
        else:
            print("Invalid password. Try again with a valid password: ")
    

def registration():
    global user_name, password
    user_name = input("Create a name: ")
    password = validate_password()
    print("Registration successful!")
    return user_name, password

# Ask the user to iput his valid german mobile number.
def phone_number():
    pattern = "^(?:\+49[\s-]?|0049[\s-]?|0[\s-]?)[1-9]\d{1,4}(?:[\s-]?\d{2,10})+$"

    
    while True:
        phone = input("Enter your German phone number: ").strip()
        
        if re.match(pattern,phone):
            print("Thank you! Phone number is saved.")
            return phone
        else:
            print("Invalid phone number. Try again (e.g., +4917612345678 or 017612345678): ")
            

# Ask the user to login

def login(user_name, password):
    attempts = 3
    
    for attempt in range(attempts):
        log = input("Enter your username: ")
        pass_word = input("Enter your password: ")

        if (log == user_name and pass_word == password):
            print("Login successful!")
            return True
        else:
            print("Invalid Username or password. Try again: ")
    print("You've used all the attempts. Try again after 5 seconds...")
    
    time.sleep(5)
    
    log = input("Enter your username: ")
    pass_word = input("Enter your password: ")
    
    if (log == user_name and pass_word == password):
        print("Login successful!")
        return True
    else:
        print("Invalid Username or password. Please register again")
        return False
    

user_name, password = registration()
phone = phone_number()
if not login(user_name, password):
    user_name, password = registration()
    login(user_name, password)
    

print(f"Hello {user_name}! Welcome to the Amazon Expense Tracker!")


def options():
    purchases = []
    
    while True:
        print("What would you like to do?")
        print("1.Enter a pirchase.")
        print("2.Generate a report.")
        print("3.Quit.")
        
        choice = input("Select an option (1-3) ")
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print(f"Goodbye {user_name}!")
            break
        else:
            print("invalid choice. Please select a valid option.")
            