'''
password checker
'''
password = "dolly106tri"
entered_pass = input("Enter Password: ")

while (entered_pass != password):
    entered_pass = input("Wrong Password! Try again and enter Password: ")
print("Success! That's the password")