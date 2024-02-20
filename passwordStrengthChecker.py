import re

def check_password_strength(password):
   
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit."
    
    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

def main():
    password = input("Hey user, please enter your password: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()