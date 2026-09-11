
import re
# Function to check if a password is valid
def is_valid_password(password):
# Check the length of the password
    if 6 <= len(password) <= 12:
# Check if the password matches all the criteria using regular
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False
# Accept input from the user as comma-separated passwords
passwords = input("Enter passwords separated by commas: ").split(',')
print("Entered passwords:", passwords)
# Initialize a list to store valid passwords
valid_passwords = []
# Iterate through the passwords and check their validity
for psw in passwords:
    if is_valid_password(psw):
        valid_passwords.append(psw)
    else:
        print(f"Invalid password: {psw}")
        break
# Print the valid passwords 
print(f'Valid passwords: ' + ', '.join(valid_passwords))
