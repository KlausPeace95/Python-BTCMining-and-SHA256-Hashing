# THIS IS A SIGN-UP LOGIN PROGRAM USING sha256
from hashlib import sha256


# Sign-Up Logic

user = input('Enter Your Username: ')
email = input('Enter Your Email: ')
password = input('Enter Your Password: ')
passconfirm = input('Confirm your password: ')


while passconfirm != password:
    print("Passwords do not match!")
    password = input('Enter Your Password: ')
    passconfirm = input('Confirm your password: ')

print(f"Welcome, {user}!")

logins = input('Enter Your Username or Email: ')
while logins != user and logins != email:
    print("Oops! Wrong username or email")
    logins = input('Enter Your Username or Email: ')

pwd = input('Enter Your Password: ')

while sha256(pwd.encode("ascii")).hexdigest() != sha256(password.encode("ascii")).hexdigest():
    print("Oops! Wrong password!")
    pwd = input('Enter Your Password: ')


print(f"Thank you for logging in correctly {logins}")
