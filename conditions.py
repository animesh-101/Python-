# Understanding how the conditional statements work in python.

#This variable will be used to verify the name and password.
user_name = "Animesh Raj"
password = "12345"

#This will be used for user input
name_inp = input("Enter Name :  ")
pass_inp = input("Enter Password :  ")


#now using if-else to verify the user data.
if name_inp.lower()==user_name.lower() and  password == pass_inp:
    print("Access Granted...")

else:
    print("Invalid Username and Password.!")


