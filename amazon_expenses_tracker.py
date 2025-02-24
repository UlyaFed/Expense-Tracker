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
    
    # General input func with validation.
    def get_input(prompt, validator):
        
        while True:
            value = input(prompt).strip()
            if validator(value):
                return value
            print("invalid input. Please try again.")
    
    # Check if date format is MM/DD/YYYY or MM-DD-YYYY.
    def is_valid_date(date):
        return bool(re.match(r"^(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](\d{4})$",date))
        
    # Check if text is at least 3 characters long.
    def is_valid_string(text):
        return len(text) >= 3
    
    # Check if input is a positive float.
    def is_valid_float(number):
        
        try:
            return float(number) >= 1
        except ValueError:
            return False
        
    #Check if input is a positive integer.
    def is_valid_int(number):
        
        try:
            return int(number) >= 1
        except ValueError:
            return False
    
    while True:
        print("What would you like to do?")
        print("1.Enter a pirchase.")
        print("2.Generate a report.")
        print("3.Quit.")
        
        choice = input("Select an option (1-3) ")
        
        if choice == "1":
            purchase = {
                "date": get_input("Enter date(MM/DD/YYYY): ", is_valid_date).replace("-","/"),
                "item": get_input("Enter item name: ", is_valid_string),
                "total_cost": float(get_input("Enter total cost: ", is_valid_float)),
                "weight_kg": float(get_input("Enter item weight(kg): ", is_valid_float)),
                "quantity": int(get_input("Enter quantity: ",is_valid_int))
            }
            purchases.append(purchase)
            print("Purchase added successfully!")
            
        elif choice == "2":
            if not purchases:
                print("You must enter at least one purchase first.")
            else:
                print("\nPurchase Report:")
                for i, p in enumerate(purchases, 1):
                    print(f"{i}. Date: {p["date"]}, Item: {p["item"]}, Cost: ${p["total_cost"]}, Weight: {p["weight_kg"]}kg, Quantity: {p["quantity"]}") 
                
        elif choice == "3":
            print(f"Goodbye {user_name}!")
            break
        else:
            print("invalid choice. Please select a valid option.")
            
options()